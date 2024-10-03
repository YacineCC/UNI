#include "complexe.h"
#include <iostream>
using namespace std;

Complexe::Complexe()
{
	//static unsigned int nbident = 0; 
	reel = 0;
	imm = 0;
	//ident = nbident;
	//cout<<"Constructeur par défaut n°"<<nbident<<" appelé"<<endl;
	//nbident+=1;
}

Complexe::Complexe(float a, float b)
{
	reel = a;
	imm = b;
	//ident = nbident;
	//cout<<"Constructeur par paramètre n°"<<nbident<<" appelé"<<endl;
	//nbident+=1;
}


Complexe::Complexe(const Complexe& A)
{
	reel = A.reel;
	imm = A.imm;
	//ident = nbident;
	//cout<<"Constructeur par copie n°"<<nbident<<" appelé"<<endl;
	//nbident+=1;
}

Complexe::~Complexe()
{
	//cerr<<"Complexe n°"<<ident<<" détruit"<<endl;
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
	//cout<<"n°"<<ident<<": ";
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

Complexe& Complexe::operator=(const Complexe& C)
{
	reel = C.reel;
	imm = C.imm;
	return *this;
}

Complexe Complexe::operator*(const Complexe& C)
{
	Complexe R;
	R.reel = reel*C.reel - C.imm*imm;
	R.imm = reel*C.imm + imm*C.reel;
	return R;

}

Complexe Complexe::operator*(const float& f)
{
	Complexe R;
	R.reel = reel * f;
	R.imm = imm * f;
	return R;
}

Complexe operator*(const float& f, const Complexe& C)
{
	Complexe R;
	R.reel = C.reel * f;
	R.imm = C.imm * f;
	return R;
	//return C*f;
}

ostream& operator<<(ostream &o, const Complexe& C)
{

	if(C.imm >= 0)
		o<<C.reel<<"+"<<C.imm<<".i"<<endl;
	else
	{
		o<<C.reel<<C.imm<<".i"<<endl;
	}
	return o;
}
