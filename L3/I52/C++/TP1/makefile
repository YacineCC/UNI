
main.exe: main.o echangiste.o complexe.o
	g++ main.o echangiste.o complexe.o -o main.exe

main.o: main.cc echangiste.h complexe.h
	g++ -c main.cc
echangiste.o: echangiste.cc echangiste.h complexe.h
	g++ -c echangiste.cc 
complexe.o: complexe.cc complexe.h
	g++ -c complexe.cc

