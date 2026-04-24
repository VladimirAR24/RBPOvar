FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1
ENV AFL_SKIP_CPUFREQ=1

RUN apt-get update && apt-get install -y \
    build-essential \
    clang \
    valgrind \
    afl++ \
    python3 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY main.cpp .
COPY generate_samples.py .

RUN python3 generate_samples.py

RUN g++ -std=c++17 -g -O0 -Wall -Wextra main.cpp -o telemetry_parser

RUN g++ -std=c++17 -g -O0 -Wall -Wextra -DDEMO_BUGS main.cpp -o telemetry_parser_buggy

RUN afl-clang++ -std=c++17 -g -O0 -fsanitize=address main.cpp -o telemetry_parser_afl

CMD ["./telemetry_parser", "input/valid.evt"]