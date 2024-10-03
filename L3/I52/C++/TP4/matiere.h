#ifndef MATIERE_H
#define MATIERE_H
#include <string>
#include <iostream>
using std::string;
using std::cout;
using std::endl;
class Matiere
{
	private:
		string nom;
		int coef;
	public:
		Matiere();
		Matiere(string, int);
		void Affic();
		string GetNom();
		int GetCoef();
};

#endif
