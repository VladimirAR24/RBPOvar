import struct
from pathlib import Path

HEADER_FORMAT = "<4sHHIIQHH"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

def write_frame(file, magic, version, frame_id, timestamp_ms, values):
    payload = struct.pack("<" + "h" * len(values), *values)
    payload_size = len(payload)
    sensor_count = len(values)

    header = struct.pack(
        HEADER_FORMAT,
        magic,
        version,
        HEADER_SIZE,
        payload_size,
        frame_id,
        timestamp_ms,
        sensor_count,
        0
    )

    file.write(header)
    file.write(payload)

def make_valid_file(path):
    with open(path, "wb") as file:
        write_frame(file, b"EVT1", 1, 1, 1713861000123, [100, 120, 140, 160, 180])
        write_frame(file, b"EVT1", 1, 2, 1713861001123, [90, 110, 130, 150, 170])
        write_frame(file, b"EVT1", 1, 3, 1713861002123, [200, 210, 220, 230, 240])

def make_small_payload_file(path):
    with open(path, "wb") as file:
        write_frame(file, b"EVT1", 1, 1, 1713861000123, [777])

def make_corrupted_magic_file(path):
    with open(path, "wb") as file:
        write_frame(file, b"BAD!", 1, 1, 1713861000123, [100, 200, 300])

def main():
    input_dir = Path("input")
    input_dir.mkdir(exist_ok=True)

    make_valid_file(input_dir / "valid.evt")
    make_small_payload_file(input_dir / "small_payload.evt")
    make_corrupted_magic_file(input_dir / "corrupted_magic.evt")

    print("Sample files generated in ./input")

if __name__ == "__main__":
    main()