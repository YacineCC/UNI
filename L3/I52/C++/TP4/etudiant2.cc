#include "etudiant1.h"
#include "etudiant2.h"
#include "matiere.h"
#include <iostream>
using std::cout;
using std::endl;


Etudiant2::Etudiant2() : Etudiant1()
{
	mat = NULL;
}

Etudiant2::Etudiant2(string n, string p, uint a, uint nbnotes, Matiere* mater) : Etudiant1(n, p, a, nbnotes)
{
	mat = mater;
}

Etudiant2::Etudiant2(Etudiant2& E) : Etudiant1(E)
{
	uint nb = E.GetNb();
	mat = new Matiere[nb];
	for(uint i = 0; i < nb; i++)
	{
		mat[i] = E.mat[i];
	}
}


Etudiant2::~Etudiant2()
{
	delete[] mat;
}

void Etudiant2::Affic()
{
	Personne::Affic();
	float* notes = GetNotes();
	uint nb = GetNb();
	cout<<endl<<"Notes :"<<endl;

	
	for(uint i = 0; i < nb; i++)
	{
		cout<<'|'<<mat[i].GetNom()<<" : "<<notes[i]<<'|';
	}
	cout<<endl;
	
	
}

float Etudiant2::Moyenne()
{
	uint nb = GetNb();
	float* notes = GetNotes();
	float sum = 0;
	int div = 0;
	for(uint i = 0; i < nb; i++)
	{
		sum += notes[i]*mat[i].GetCoef();
		div += mat[i].GetCoef();
	}

	return sum/div;
}

Etudiant2& Etudiant2::operator=(Etudiant2& E)
{
	uint nb = E.GetNb();
	if(this != &E)
	{
		Etudiant1::operator=(E);
		delete[] mat;
		mat = new Matiere[nb];
		for(uint i = 0; i < nb; i++)
		{
			mat[i] = E.mat[i];
		}

	}
	return *this;
}