#ifndef ETUDIANT1_H
#define ETUDIANT1_H
#include "personne.h"
class Etudiant1 : public Personne
{
	private:
		uint nb;
		float* notes;
	public:
		Etudiant1();
		Etudiant1(string, string, uint, uint);
		Etudiant1(const Etudiant1&);
		~Etudiant1();
		void AjouterNotes(float*);
		void Affic();
		float Moyenne();
		Etudiant1& operator=(const Etudiant1&);
		float* GetNotes();
		uint GetNb();
		
};

#endif 
