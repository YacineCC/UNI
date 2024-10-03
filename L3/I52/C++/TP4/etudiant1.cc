#include "etudiant1.h"


Etudiant1::Etudiant1() : Personne()
{
	nb = 0;
	notes = NULL;
}
Etudiant1::Etudiant1(string n, string p, uint a, uint nbnotes) : Personne(n, p, a)
{
	nb = nbnotes;
	notes = new float[nb];
	for(uint i = 0; i < nb; i++)
	{
		notes[i] =0;
	}
	
}


Etudiant1::Etudiant1(const Etudiant1& E) : Personne(E) 
{
	nb = E.nb;
	
	notes = new float[nb];
	
	for(uint i = 0; i < nb; i++)
	{
		notes[i] = E.notes[i];
	}
}


Etudiant1::~Etudiant1()
{
	delete[] notes;
}

void Etudiant1::AjouterNotes(float* n)
{
	
	
	for(uint i = 0; i < nb; i++)
	{
		notes[i] = n[i];
	}

}

void Etudiant1::Affic()
{
	Personne::Affic();
	cout<<" Notes : ["<<notes[0];
	for(uint i = 1; i < nb; i++)
	{
		cout<<", "<<notes[i];
	}
	cout<<"]|"<<endl;
}

float Etudiant1::Moyenne()
{
	float sum = 0;
	for(uint i = 0; i < nb; i++)
	{
		sum += notes[i];
	}
	return sum/nb;
}

Etudiant1& Etudiant1::operator=(const Etudiant1& e)
{
	if(this != &e)
	{
		Personne::operator=(e);
		delete[] notes;
		nb = e.nb;
		notes = new float[nb];
		
		for(uint i = 0; i < nb; i++)
		{
			notes[i] = e.notes[i];
		}
	}
	return *this;
}

float* Etudiant1::GetNotes()
{
	return notes;
}

uint Etudiant1::GetNb()
{	return nb;
}