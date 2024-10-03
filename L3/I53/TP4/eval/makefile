CC = gcc
CFLAGS = -Wall -g
BISON = bison
FLEX = flex

OBJS = parser.o lexer.o
BIN = eval

all: $(BIN)

$(BIN): $(OBJS)
	$(CC) $(CFLAGS) $^ -o $@ -lfl

parser.h : parser.y

parser.c: parser.y
	$(BISON) -d $< -o $@

lexer.c: lexer.lex parser.h
	$(FLEX)  -o $@ $<

%.o : %.c
	$(CC) $(CFLAGS) -c $^

clean:
	rm -f *~ *.o lexer.c parser.[ch] $(BIN)

.PHONY: all clean
