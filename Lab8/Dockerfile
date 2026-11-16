FROM docker.io/library/debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR app

COPY lab3/Makefile lab3/test_fibonacci.c ./
COPY lab3/headers/ ./headers/
COPY lab3/590MakefileLab/ ./590MakefileLab

RUN make clean && make

CMD ["./test_fibonacci"]
