CFLAGS=-Wall -g

main: main.o personne.o
	g++ $(CFLAGS) main.o personne.o -o main	

main.o: main.cc personne.h
	g++ $(CFLAGS) -c main.cc	

personne.o: personne.cc personne.h
	g++ $(CFLAGS) -c personne.cc
