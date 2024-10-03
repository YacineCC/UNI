#include <iostream>
#include "complexe.h"
#include <cmath>
using namespace std;


void AfficherComplexe(const Complexe& C)
{
	cout<<"n°"<<C.ident<<": ";
	if(C.imm >= 0)
		cout<<C.reel<<"+"<<C.imm<<".i"<<endl;
	else
		cout<<C.reel<<C.imm<<".i"<<endl;
    
}

Complexe Somme(const Complexe& A, const Complexe& B)
{
    Complexe res;
    res.reel = A.reel + B.reel;
    res.imm = A.imm + B.imm;
    return res;
}

Complexe Produit(const Complexe& A, const Complexe& B)
{
    Complexe res;
    res.reel = A.reel*B.reel - A.imm*B.imm;
    res.imm = A.imm*B.reel + A.reel*B.imm;
    return res;
}
float Module(const Complexe& A)
{
    return sqrt(A.reel*A.reel + A.imm*A.imm);
}

Complexe Conjuge(const Complexe& A)
{
    Complexe res;
    res.reel = A.reel;
    res.imm = -A.imm;
    return res;
}
void Init(Complexe& A)
{
	static unsigned int nbident = 0;
	A.reel = 0;
	A.imm = 0;
	A.ident = nbident;
	nbident+= 1;
}

void CreerComplexe(Complexe** pc)
{
	*pc = new Complexe;
	Init(**pc);
}

void CreerComplexe(ptComplexe& pc)
{
	pc = new Complexe;
	Init(*pc);

}
Complexe* CreerComplexe()
{
	Complexe* pc = new Complexe;
	Init(*pc);
	return(pc);

 	
}

Complexe* CreerVecteurComplexe(int n)
{
	Complexe* res;
	res = new Complexe[n];
	for(int i; i < n; i++)
		Init(res[i]);
	return res;
}
