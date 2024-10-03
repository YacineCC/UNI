CC   := gcc
CFLAGS := -Wall -g
FLEX := flex
LIB  := -lfl

SRC  := mot_le_plus_long.lex
SRCC := mot_le_plus_long.c
BIN  := mot_le_plus_long

all: $(BIN)

$(BIN): $(SRCC)
	$(CC) $(CFLAGS) -o $@ $(SRCC) $(LIB)

$(SRCC): $(SRC)
	$(FLEX) -o $@ $^

clean:
	rm -rf *~ $(SRCC) $(BIN)

.PHONY: all clean
