#include "matiere.h"

Matiere::Matiere()
{
	nom = "";
	coef = -1;
}

Matiere::Matiere(string n, int c)
{
	nom = n;
	coef = c;
}

void Matiere::Affic()
{
	cout<<nom<<" coef: "<<coef<<endl;
}

string Matiere::GetNom()
{
	return nom;
}

int Matiere::GetCoef()
{
	return coef;
}
