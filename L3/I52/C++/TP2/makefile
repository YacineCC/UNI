CFLAG=-Wall -g

main.exe: main.o complexe.o
	g++ $(CFLAG) main.o complexe.o -o main.exe
main.o: main.cc complexe.h
	g++ $(CFLAG) -c main.cc
complexe.o: complexe.cc complexe.h
	g++ $(CFLAG) -c complexe.cc
