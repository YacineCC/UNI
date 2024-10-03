#ifndef COMPLEXE_H
#define COMPLEXE_H
#include <iostream>

class Complexe
{
	private:
		float reel;
		float imm;
		unsigned int ident;
	public:
		Complexe();
		Complexe(float, float);
		Complexe(const Complexe&);
		~Complexe();
		float getRe(); //partie reelle du complexe
		float getIm(); //partie imaginaire du complexe
		void Print(); //affichage sur stdout des valeurs du complexe
		Complexe Sum(const Complexe&); // ajout d'un complexe au complexe courant
		bool Identical(const Complexe&); //comparaison d'un complexe et du complexe courant
};





#endif
