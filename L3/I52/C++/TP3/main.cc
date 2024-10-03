#include <iostream>
#include "complexe.h"
#include "polynome.h"
#include "vecteurcomplexe.h"
#include <fstream>
using namespace std;
int main()
{
	/*
	Complexe A;
	Complexe B(1,2);
	Complexe C(A);
	Polynome A1;
	A1.Affic();
	*/
	/*
	float tmp[3] = {1, 2, 3};
	Polynome B1(2,tmp);
	B1.Affic();
	Polynome C1 = B1;
	C1.Affic();
	*/
	ifstream test("data.txt");
	VecteurComplexe D1(test);
	VecteurComplexe H;
	Complexe A(1,2);
	VecteurComplexe B(&A, 1);

	Complexe J(5,6);
	Complexe K;
	J.Print();
	K.Print();
	K = J;
	K.Print();
	K = K*5;
	K.Print();
	K = -1*K;
	K.Print();
	K = J*K;
	K.Print();
	cout<<K<<"Surchage sur le flux"<<endl;
	cout<<A;




	return 0;
}
