#include <iostream>
#include "echangiste.h"
#include "complexe.h"
using namespace std;

Complexe Bidon(Complexe &Z)
{
	cout<<&Z<<endl;
	cout<<&(Z.reel)<<endl;
	cout<<&(Z.imm)<<endl;
	cout<<&(Z.ident)<<endl;
	
	Complexe A;
	Init(A);
	return A;
}

int main()
{
	/*
 	

    int a = 0, b = 1;
    cout << a <<" "<< b << endl;
    Permuter(a,b);
    cout << a <<" "<< b << endl;
    
    Complexe A;
    Complexe B;
    A.reel = 10;
    A.imm = 5;
    B.reel = -20;
    B.imm = -15;
    
    AfficherComplexe(A);
    AfficherComplexe(B);
    Permuter(A,B);
    AfficherComplexe(A);
    AfficherComplexe(B);
    
    cout<<"A: ";
    AfficherComplexe(A);

    cout<<"B: ";
    AfficherComplexe(B);

    cout<<"Somme A + B: ";
    AfficherComplexe(Somme(A,B));

    cout<<endl<<"Produit A * B: ";
    AfficherComplexe(Produit(A,B));

    cout<<endl<<"Module A: "<<Module(A)<<endl;

    cout<<"Conjuge de A: ";
    AfficherComplexe(Conjuge(A));

    AfficherComplexe(Produit(A,Conjuge(A)));
    cout<<Module(A)*Module(A)<<endl;

	*/

	Complexe A;
	Init(A);
	AfficherComplexe(A);
	Complexe B;
	Init(B);
	AfficherComplexe(B);
	Complexe C;
	Init(C);
	AfficherComplexe(C);

	static Complexe Z;
	Init(Z);
	cout<<&Z<<endl;
	cout<<&(Z.reel)<<endl;
	cout<<&(Z.imm)<<endl;
	cout<<&(Z.ident)<<endl;
	cout<<endl;

	Complexe& ref = Z;
	cout<<&ref<<endl;
	cout<<&(ref.reel)<<endl;
	cout<<&(ref.imm)<<endl;
	cout<<&(ref.ident)<<endl;
	cout<<endl;

	Complexe k = Bidon(Z);
	cout<<&k<<endl;

	Complexe* p1,p2;
	//CreerComplexe(&p1);
	//ptComplexe pt;
	//CreerComplexe(pt);
	//CreerComplexe(pt);
	p2 = CreerComplexe();

	//AfficherComplexe(*p1);
	AfficherComplexe(*p2);
	//AfficherComplexe(*pt);

}
