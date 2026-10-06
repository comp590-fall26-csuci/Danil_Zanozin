CC      = gcc
SRC     := 590MakefileLab
CFLAGS  := -Wall -Wextra -I$(SRC)/headers
LDLIBS  := -lm
OBJS    := main.o fibonacci.o
TARGET  := fibonacci
 
.PHONY: all run clean
 
all: $(TARGET)
 
$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $@ $(LDLIBS)
 
%.o: $(SRC)/%.c $(SRC)/headers/fibonacci.h
	$(CC) $(CFLAGS) -c $< -o $@
 
run: $(TARGET)
	./$(TARGET)
 
clean:
	rm -f $(OBJS) $(TARGET)
 
