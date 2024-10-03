#ifndef VECTEUR_COMPLEXE_H
#define VECTEUR_COMPLEXE_H
#include "complexe.h"
#include <iostream>
#include <fstream>

using namespace std;

class VecteurComplexe
{
	private:
		int taille; // nb d'éléments du vecteur
		Complexe* vec; // éléments du vecteur

	public:
		VecteurComplexe();
		~VecteurComplexe();
		VecteurComplexe(const VecteurComplexe&);
		VecteurComplexe& operator=(const VecteurComplexe&);

		VecteurComplexe(const Complexe*, unsigned short);
		VecteurComplexe(ifstream&);
		void AfficVec();
		friend ostream& operator<<(ostream&, const VecteurComplexe&);


};


#endif
