#include "polynome.h"
#include <iostream>
using namespace std;

Polynome::Polynome()
{
	deg = -1;
	coeff = NULL;
}

Polynome::Polynome(const Polynome& P)
{
	deg = P.deg;
	coeff = new float[deg+1];
	for(int i = 0; i < deg+1; i++)
	{
		coeff[i] = P.coeff[i];
	}

}


Polynome::Polynome(int d, float* c)
{
	deg = d;
	coeff = new float[d+1];
	for(int i = 0; i<= d; i++)
	{
		coeff[i] = c[i];
	}
}


Polynome::~Polynome()
{
	delete[] coeff;
}

Polynome& Polynome::operator=(const Polynome& P)
{
	delete[] coeff;
	deg = P.deg;

	coeff = new float[deg+1];
	for(int i = 0; i < deg+1; i++)
	{
		coeff[i] = P.coeff[i];
	}
	return *this;
}

void Polynome::Affic()
{
	cout<<"[";
	for(int i = 0; i <= deg; i++)
	{
		if (i == 0) cout << coeff[0];
		else
		cout<<", "<<coeff[i];
	}
	cout<<"]"<<endl;
}
