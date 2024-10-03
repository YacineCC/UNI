CFLAG=-Wall -g
all: Prog.exe

Prog.exe: main.o Tableau.o
	gcc $(CFLAG) -o Prog.exe main.o Tableau.o

Tableau.o: Tableau.c
	gcc $(CFLAG) -c Tableau.c

main.o: main.c
	gcc $(CFLAG) -c main.c



clean:
	rm *.o
