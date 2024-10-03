#include "complexe.h"
#include <iostream>
using namespace std;
Complexe::Complexe()
{
	static unsigned int nbident = 0; 
	reel = 0;
	imm = 0;
	ident = nbident;
	nbident+=1;
}

Complexe::Complexe(float a, float b)
{
	static unsigned int nbident = 0; 
	reel = a;
	imm = b;
	ident = nbident;
	nbident+=1;
}


Complexe::Complexe(const Complexe& A)
{
	static unsigned int nbident = 0; 
	reel = A.reel;
	imm = A.imm;
	ident = nbident;
	nbident+=1;
}

Complexe::~Complexe()
{
	cerr<<"Complexe n°"<<ident<<" détruit"<<endl;
}

float Complexe::getRe()
{
	return reel;
}
float Complexe::getIm()
{
	return imm;
}

void Complexe::Print()
{
	cout<<"n°"<<ident<<": ";
	if(imm >= 0)
		cout<<reel<<"+"<<imm<<".i"<<endl;
	else
	{
		cout<<reel<<imm<<".i"<<endl;
	}
}

Complexe Complexe::Sum(const Complexe& z)
{
	return Complexe(reel+z.reel, imm + z.imm);
}

bool Complexe::Identical(const Complexe& z)
{
	if(reel == z.reel && imm == z.imm)
		return true;
	else
		return false;


}

