SHELL=/usr/bin/bash
INCLUDE_P=$(HOME)/UNI/libs/Tableau/
CFLAG=-Wall -g -I$(INCLUDE_P) -L$(INCLUDE_P)

all: prog.exe

prog.exe: main.o
	gcc $(CFLAG) -o prog.exe main.o -ltableau

main.o: main.c
	gcc $(CFLAG) -c main.c

clean:
	rm *.o
