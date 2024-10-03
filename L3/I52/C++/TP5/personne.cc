#include "personne.h"
#include <iostream>



Personne::Personne()
{
	prenom = "";
	nom = "";
	age = -1;
}

Personne::Personne(const Personne& P)
{
	prenom = P.prenom;
	nom = P.nom;
	age = P.age;
}

Personne& Personne::operator=(const Personne& P)
{
	prenom = P.prenom;
	nom = P.nom;
	return *this;
}

Personne::~Personne()
{
	prenom = "";
	nom = "";
	age = -1;
}

Personne::Personne(string n, string p, uint a)
{
	prenom = p;
	nom = n;
	age = a;
}

ostream& operator<<(ostream& o, const Personne& P)
{
	o<<P.nom<<' '<<P.prenom<<endl;
	return o;
}
