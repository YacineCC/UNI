CFLAGS=-Wall -g


main: main.o professeur.o personne.o etudiant1.o matiere.o etudiant2.o
	g++ $(CFLAGS) main.o personne.o professeur.o etudiant1.o matiere.o etudiant2.o -o main

main.o: main.cc  personne.h personne.h etudiant1.h matiere.h etudiant2.h
	g++ $(CFLAGS) -c main.cc

professeur.o: professeur.cc professeur.h 
	g++ $(CFLAGS) -c professeur.cc

personne.o: personne.cc personne.h
	g++ $(CFLAGS) -c personne.cc

etudiant1.o: etudiant1.cc etudiant1.h
	g++ $(CFLAGS) -c etudiant1.cc

matiere.o: matiere.cc matiere.h
	g++ $(CFLAGS) -c matiere.cc

etudiant2.o: etudiant2.cc etudiant2.h
	g++ $(CFLAGS) -c etudiant2.cc
