#include "complexe.h"
#include <iostream>
using namespace std;

int main()
{
	/*
	Complexe A;
	Complexe B(1.5,7.2);
	Complexe C(B);
	Complexe D(1.5,9.2);

	cout<<B.getIm()<<endl;
	cout<<C.getIm()<<endl;
	B.Print();
	A.Print();
	*/
	Complexe x(1,2);
	Complexe y(3,4);
	Complexe z(y);
	x.Print();
	y.Print();
	z.Print();
	(x.Sum(y)).Print();
	cout << x.Identical(y)<<endl;


	return 0;
}
