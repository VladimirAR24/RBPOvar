#include <algorithm>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <string>
#include <vector>

#pragma pack(push, 1)
struct FrameHeader {
    char magic[4];             // "EVT1"
    uint16_t version;          // format version
    uint16_t headerSize;       // header size in bytes
    uint32_t payloadSize;      // payload size in bytes
    uint32_t frameId;          // frame number
    uint64_t timestampMs;      // frame timestamp in milliseconds
    uint16_t sensorCount;      // number of int16_t values in payload
    uint16_t reserved;         // reserved field
};
#pragma pack(pop)

static constexpr char EXPECTED_MAGIC[4] = {'E', 'V', 'T', '1'};
static constexpr uint16_t EXPECTED_VERSION = 1;
static constexpr uint32_t MAX_PAYLOAD_SIZE = 1024 * 1024; // 1 MB
static constexpr std::size_t MAX_FRAMES = 100000;

bool readExact(std::ifstream& file, char* buffer, std::size_t size) {
    if (size == 0) {
        return true;
    }

    file.read(buffer, static_cast<std::streamsize>(size));
    return file.gcount() == static_cast<std::streamsize>(size);
}

bool isValidMagic(const FrameHeader& header) {
    return std::memcmp(header.magic, EXPECTED_MAGIC, sizeof(EXPECTED_MAGIC)) == 0;
}

void printHeader(const FrameHeader& header) {
    std::cout << "Frame #" << header.frameId << "\n";
    std::cout << "  version:      " << header.version << "\n";
    std::cout << "  header size:  " << header.headerSize << " bytes\n";
    std::cout << "  payload size: " << header.payloadSize << " bytes\n";
    std::cout << "  timestamp:    " << header.timestampMs << " ms\n";
    std::cout << "  sensor count: " << header.sensorCount << "\n";
}

void printStatistics(const std::vector<int16_t>& values) {
    if (values.empty()) {
        std::cout << "  no sensor values\n";
        return;
    }

    const auto minmax = std::minmax_element(values.begin(), values.end());
    const long long sum = std::accumulate(values.begin(), values.end(), 0LL);
    const double avg = static_cast<double>(sum) / static_cast<double>(values.size());

    std::cout << "  min value:    " << *minmax.first << "\n";
    std::cout << "  max value:    " << *minmax.second << "\n";
    std::cout << "  avg value:    " << std::fixed << std::setprecision(2) << avg << "\n";
}

bool validateHeader(const FrameHeader& header, std::size_t frameIndex) {
    if (!isValidMagic(header)) {
        std::cerr << "Error: invalid magic in frame " << frameIndex << "\n";
        return false;
    }

    if (header.version != EXPECTED_VERSION) {
        std::cerr << "Error: unsupported version in frame " << frameIndex << "\n";
        return false;
    }

    if (header.headerSize != sizeof(FrameHeader)) {
        std::cerr << "Error: invalid header size in frame " << frameIndex << "\n";
        return false;
    }

    if (header.sensorCount == 0) {
        std::cerr << "Error: sensor count is zero in frame " << frameIndex << "\n";
        return false;
    }

    if (header.payloadSize == 0) {
        std::cerr << "Error: empty payload in frame " << frameIndex << "\n";
        return false;
    }

    if (header.payloadSize > MAX_PAYLOAD_SIZE) {
        std::cerr << "Error: payload is too large in frame " << frameIndex << "\n";
        return false;
    }

    const std::size_t expectedPayloadSize =
        static_cast<std::size_t>(header.sensorCount) * sizeof(int16_t);

    if (expectedPayloadSize > MAX_PAYLOAD_SIZE) {
        std::cerr << "Error: expected payload is too large in frame " << frameIndex << "\n";
        return false;
    }

    if (static_cast<std::size_t>(header.payloadSize) != expectedPayloadSize) {
        std::cerr << "Error: payload size does not match sensor count in frame "
                  << frameIndex << "\n";
        std::cerr << "  payloadSize: " << header.payloadSize << "\n";
        std::cerr << "  expected:    " << expectedPayloadSize << "\n";
        return false;
    }

    return true;
}

bool parsePayloadSafe(const FrameHeader& header,
                      const std::vector<char>& payload,
                      std::vector<int16_t>& values) {
    const std::size_t expectedBytes =
        static_cast<std::size_t>(header.sensorCount) * sizeof(int16_t);

    if (payload.size() != expectedBytes) {
        std::cerr << "Error: payload buffer size mismatch\n";
        return false;
    }

    values.clear();
    values.resize(header.sensorCount);

    std::memcpy(values.data(), payload.data(), expectedBytes);
    return true;
}

int parseFile(const std::string& path) {
    std::ifstream file(path, std::ios::binary);

    if (!file) {
        std::cerr << "Error: cannot open file: " << path << "\n";
        return 1;
    }

    std::cout << "Input file: " << path << "\n\n";

    std::size_t frameIndex = 0;
    std::size_t parsedFrames = 0;

    while (true) {
        if (frameIndex >= MAX_FRAMES) {
            std::cerr << "Error: too many frames\n";
            return 6;
        }

        FrameHeader header{};
        file.read(reinterpret_cast<char*>(&header), sizeof(FrameHeader));

        if (file.eof() && file.gcount() == 0) {
            break;
        }

        if (file.gcount() != static_cast<std::streamsize>(sizeof(FrameHeader))) {
            std::cerr << "Error: truncated header at frame " << frameIndex << "\n";
            return 2;
        }

        if (!validateHeader(header, frameIndex)) {
            return 3;
        }

        std::vector<char> payload(static_cast<std::size_t>(header.payloadSize));

        if (!readExact(file, payload.data(), payload.size())) {
            std::cerr << "Error: truncated payload at frame " << frameIndex << "\n";
            return 4;
        }

        std::vector<int16_t> values;
        if (!parsePayloadSafe(header, payload, values)) {
            return 5;
        }

        printHeader(header);
        printStatistics(values);
        std::cout << "\n";

        ++frameIndex;
        ++parsedFrames;
    }

    std::cout << "Parsed frames: " << parsedFrames << "\n";
    return 0;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage:\n";
        std::cerr << "  " << argv[0] << " <input.evt>\n";
        return 1;
    }

    return parseFile(argv[1]);
}