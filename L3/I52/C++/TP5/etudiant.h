#ifndef ETUDIANT_H
#define ETUDIANT_H
#include "personne.h"
#include <string>
#include <stdio.h>
using namespace std;


class Etudiant{
	private:
		string cursus;
	public:
		Etudiant();
		Etudiant(const Etudiant&);
		~Etudiant();
		Etudiant& operator=(const Etudiant&);

		Etudiant(string, string,uint, string);
};


#endif
