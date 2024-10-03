CC   := gcc
CFLAGS := -Wall -g
BISON := bison
LIB  := -lfl

SRC  := calculatrice.y
SRCC := calculatrice.c
BIN  := calculatrice

all: $(BIN)

$(BIN): $(SRCC)
	$(CC) $(CFLAGS) -o $@ $(SRCC) $(LIB)

$(SRCC): $(SRC)
	$(BISON) -o $@ $^

clean:
	rm -rf *~ $(SRCC) $(BIN)

.PHONY: all clean
