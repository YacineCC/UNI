#ifndef COMPLEXE_H
#define COMPLEXE_H
#include <iostream>
using namespace std;
class Complexe
{
	private:
		float reel;
		float imm;
		//unsigned int ident;
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
		Complexe& operator=(const Complexe&);
		Complexe operator*(const Complexe&);
		Complexe operator*(const float&);
		friend Complexe operator*(const float&,const Complexe&);
		friend ostream& operator<<(ostream& , const Complexe&);


};




#endif
