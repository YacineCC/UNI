#include "etudiant.h"
#include "personne.h"


Etudiant::Etudiant():Personne()
{
	cursus = ""
}


Etudiant::~Etudiant()
{
	cursus = "";
}

Etudiant::Etudiant(const Etudiant& E):Personne(E)
{
	cursus = E.cursus;
}
/*
Etudiant& Etudiant::operator=(const Etudiant& E)
{
	Personne::=
	cursus = E.cursus;
}
*/

Etudiant::Etudiant(string n, string p, uint a, string c):Personne(n, p, a)
{
	cursus = c;
}
	
	



