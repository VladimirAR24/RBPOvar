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
    uint16_t version;          // версия формата
    uint16_t headerSize;       // размер заголовка
    uint32_t payloadSize;      // размер блока данных в байтах
    uint32_t frameId;          // номер кадра
    uint64_t timestampMs;      // время кадра в миллисекундах
    uint16_t sensorCount;      // количество значений int16_t в payload
    uint16_t reserved;         // резерв
};
#pragma pack(pop)

static constexpr const char EXPECTED_MAGIC[4] = {'E', 'V', 'T', '1'};
static constexpr uint16_t EXPECTED_VERSION = 1;
static constexpr uint32_t MAX_PAYLOAD_SIZE = 1024 * 1024; // 1 МБ

bool readExact(std::ifstream& file, char* buffer, std::size_t size) {
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

    auto minmax = std::minmax_element(values.begin(), values.end());
    long long sum = std::accumulate(values.begin(), values.end(), 0LL);
    double avg = static_cast<double>(sum) / static_cast<double>(values.size());

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

    if (header.payloadSize == 0) {
        std::cerr << "Error: empty payload in frame " << frameIndex << "\n";
        return false;
    }

    if (header.payloadSize > MAX_PAYLOAD_SIZE) {
        std::cerr << "Error: payload is too large in frame " << frameIndex << "\n";
        return false;
    }

    const uint32_t expectedPayloadSize =
        static_cast<uint32_t>(header.sensorCount) * sizeof(int16_t);

    if (header.payloadSize != expectedPayloadSize) {
        std::cerr << "Error: payload size does not match sensor count in frame "
                  << frameIndex << "\n";
        std::cerr << "  payloadSize: " << header.payloadSize << "\n";
        std::cerr << "  expected:    " << expectedPayloadSize << "\n";
        return false;
    }

    return true;
}

#ifdef DEMO_BUGS

void parsePayloadWithBugs(const FrameHeader& header, const std::vector<char>& payload) {
    // Демонстрационная уязвимая версия для ЛР:
    // 1. Используется ручное выделение памяти.
    // 2. Нет проверки минимального количества значений.
    // 3. Специально отсутствует free(), чтобы Valgrind нашёл утечку памяти.
    //
    // Этот режим нужен только для демонстрации "до исправления".

    char* rawBuffer = static_cast<char*>(std::malloc(header.payloadSize));
    if (rawBuffer == nullptr) {
        std::cerr << "Error: malloc failed\n";
        return;
    }

    std::memcpy(rawBuffer, payload.data(), header.payloadSize);

    int16_t* values = reinterpret_cast<int16_t*>(rawBuffer);

    // Потенциальный invalid read:
    // если sensorCount < 4, обращение values[3] выходит за пределы буфера.
    std::cout << "  demo value[3]: " << values[3] << "\n";

    // Утечка памяти специально оставлена для Valgrind:
    // std::free(rawBuffer);
}

#endif

bool parsePayloadSafe(const FrameHeader& header,
                      const std::vector<char>& payload,
                      std::vector<int16_t>& values) {
    if (payload.size() != header.payloadSize) {
        std::cerr << "Error: payload buffer size mismatch\n";
        return false;
    }

    if (header.sensorCount == 0) {
        std::cerr << "Error: sensor count is zero\n";
        return false;
    }

    values.resize(header.sensorCount);

    std::memcpy(
        values.data(),
        payload.data(),
        static_cast<std::size_t>(header.sensorCount) * sizeof(int16_t)
    );

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
        FrameHeader header{};

        file.read(reinterpret_cast<char*>(&header), sizeof(FrameHeader));

        if (file.eof() && file.gcount() == 0) {
            break;
        }

        if (file.gcount() != static_cast<std::streamsize>(sizeof(FrameHeader))) {
            std::cerr << "Error: truncated header at frame " << frameIndex << "\n";
            return 2;
        }

#ifdef DEMO_BUGS
        // В уязвимом режиме часть проверок намеренно пропускается.
        // Это нужно, чтобы AFL++ и Valgrind могли найти проблемы.
        if (!isValidMagic(header)) {
            std::cerr << "Warning: invalid magic, frame skipped\n";
            return 3;
        }
#else
        if (!validateHeader(header, frameIndex)) {
            return 3;
        }
#endif

        std::vector<char> payload(header.payloadSize);

        if (!readExact(file, payload.data(), payload.size())) {
            std::cerr << "Error: truncated payload at frame " << frameIndex << "\n";
            return 4;
        }

        printHeader(header);

#ifdef DEMO_BUGS
        parsePayloadWithBugs(header, payload);
#else
        std::vector<int16_t> values;

        if (!parsePayloadSafe(header, payload, values)) {
            return 5;
        }

        printStatistics(values);
#endif

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