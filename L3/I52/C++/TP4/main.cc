#include "professeur.h"
#include "etudiant1.h"
#include "etudiant2.h"
int main()
{	
	/*
    Personne kaz("Miller", "Kazuhira", 38);
    kaz.Affic();
    cout<<endl;
    kaz.Viellir();
    kaz.Affic();
    cout<<endl;
	Professeur profAmrane("Professeur","Amrane", "Amazigh", 29);
	profAmrane.Affic();
	profAmrane.Travailler(98);
	profAmrane.Affic();
	Etudiant1 etudMathis("Sedkaoui", "Mathis", 21, 5);
	float notes[5] = {15.2, 17.3,19.4,12,14};
	
	etudMathis.AjouterNotes(notes);
	
	etudMathis.Affic();
	cout<<etudMathis.Moyenne()<<endl;
	*/
	/*
	Personne dori("Gray", "Dorian", 30);
	dori.Affic();
	cout<<endl;
	dori.Viellir();
	dori.Affic();
	cout<<endl;
	
	Professeur rog("Titulaire", "Rogue", "Serverus", 50);
	rog.Travailler(200);
	rog.Affic();
	
	Etudiant1 potte("Potter", "Harry", 15, 4);
	Etudiant1 mathis;
	

	mathis = potte;
	float notes[4] = {12, 9, 15, 14};
	mathis.AjouterNotes(notes);
	mathis.Affic();
	cout<<mathis.Moyenne()<<endl;
	*/
	/*
	Matiere* maters = new Matiere[5];
	maters[0] = Matiere("TAG", 9);
	maters[1] = Matiere("POO/IHM", 8);
	maters[2] = Matiere("COMP/THEO.LANG", 9);
	maters[3] = Matiere("ANGLAIS", 3);
	maters[4] = Matiere("E-SPORT", 1);
	float notes[5] = {16, 18, 17, 19, 20};
	
	Etudiant2 Yacine("Haouas", "Yacine", 20, 5, maters);
	Yacine.AjouterNotes(notes);
	Yacine.Affic();
	cout<<"moyenne : "<<Yacine.Moyenne()<<endl;
	
	Etudiant2 YacineClone;
	
	YacineClone = Yacine;

	YacineClone.Affic();
	*/
	Matiere* matieres = new Matiere[4];
	matieres[0] = Matiere("Magie", 3);
	matieres[1] = Matiere("Potion", 2);
	matieres[2] = Matiere("Divination", 4);
	matieres[3] = Matiere("Info", 1);
	Etudiant2 Potte("Potter", "Harry", 15, 4, matieres);
	float notes[4] = {12, 9, 15, 14};
	Potte.AjouterNotes(notes);
	Potte.Affic();
	cout<<"Moyenne Potte : "<<Potte.Moyenne()<<endl;

	
    return 0;
}
