#include "vecteurcomplexe.h"
#include "complexe.h"
#include <iostream>
#include <fstream>

//using namespace std;

VecteurComplexe::VecteurComplexe()
{
	taille = 0;
	vec = NULL;
}

VecteurComplexe::VecteurComplexe(const VecteurComplexe& V)
{
	taille = V.taille;
	vec = new Complexe[taille];
	for(int i = 0; i < taille; i++)
	{
		vec[i] = V.vec[i];
	}
}

VecteurComplexe::~VecteurComplexe()
{
	delete[] vec;
}

VecteurComplexe& VecteurComplexe::operator=(const VecteurComplexe& V)
{
	taille = V.taille;
	delete[] vec;

	for(int i = 0; i < taille; i++)
	{
		vec[i] = V.vec[i];
	}
	return *this;
}

VecteurComplexe::VecteurComplexe(const Complexe* v, unsigned short t)
{
	taille = t;
	vec = new Complexe[taille];

	for(int i = 0; i < taille; i++)
	{
		vec[i] = v[i];
	}
}



VecteurComplexe::VecteurComplexe(ifstream& f)
{
	f>>taille;
	//allocation
	vec = new Complexe[taille];
	//initialisation
	float a,b;
	for(int i = 0; i < taille; i++)
		{
			f>>a;
			f>>b;
			vec[i] = Complexe(a,b);
		}
}
/*
void VecteurComplexe::AfficVec()
{
	cout<<'[';
	for(int i = 0; i < taille; i++)
	{
		cout<<'('<<vec[i][0]<<", "<<vec[i][1]<<')';
	}
	cout<<']'<<endl;
}
*/


ostream& operator<<(ostream& o, const VecteurComplexe& V)
{
	for(int i = 0; i < V.taille; i++)
	{
		o<<V.vec[i]<<' ';
	}
	o<<endl;
	return o;
}
