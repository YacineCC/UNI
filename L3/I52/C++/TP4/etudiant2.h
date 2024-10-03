#ifndef ETUDIANT2_H
#define ETUDIANT2_H
#include "matiere.h"
#include "etudiant1.h"
class Etudiant2 : public Etudiant1
{
	private:
		Matiere* mat;
	
	public:
		Etudiant2();
		Etudiant2(string, string, uint, uint, Matiere*);
		Etudiant2(Etudiant2&);
		~Etudiant2();
		void Affic();
		float Moyenne();
		Etudiant2& operator=(Etudiant2&);

};

#endif
