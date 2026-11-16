CC      = gcc
SRC     := 590MakefileLab
CFLAGS  := -Wall -Wextra -I$(SRC)/headers -Iheaders
LDLIBS  := -lm
OBJS    := main.o fibonacci.o
TARGET  := fibonacci
TEST_OBJS := test_fibonacci.o fibonacci.o
TEST_TARGET := test_fibonacci

.PHONY: all run test clean

all: $(TARGET) $(TEST_TARGET)

$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $@ $(LDLIBS)

$(TEST_TARGET): $(TEST_OBJS)
	$(CC) $(TEST_OBJS) -o $@ $(LDLIBS)

test_fibonacci.o: test_fibonacci.c headers/utest.h $(SRC)/headers/fibonacci.h
	$(CC) $(CFLAGS) -c $< -o $@

%.o: $(SRC)/%.c $(SRC)/headers/fibonacci.h
	$(CC) $(CFLAGS) -c $< -o $@

run: $(TARGET)
	./$(TARGET)

test: $(TEST_TARGET)
	./$(TEST_TARGET)

clean:
	rm -f $(OBJS) test_fibonacci.o $(TARGET) $(TEST_TARGET)
