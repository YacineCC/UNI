CFLAGS=-Wall -g

main.exe: main.o saison.o episode.o serie.o
	g++ $(CFLAGS) main.o episode.o saison.o serie.o -o main.exe

main.o: main.cc episode.h serie.h saison.h
	g++ $(CFLAGS) -c main.cc

saison.o: saison.cc saison.h episode.h
	g++ $(CFLAGS) -c saison.cc

episode.o: episode.cc episode.h serie.h
	g++ $(CFLAGS) -c episode.cc


serie.o: serie.cc serie.h
	g++ $(CFLAGS) -c serie.cc 
