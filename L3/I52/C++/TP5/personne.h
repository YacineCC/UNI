#ifndef PERSONNE_H
#define PERSONNE_H

#include <string>
#include <fstream>
//using std::string;
using namespace std;

typedef unsigned int uint;
class Personne{
	private:
		string nom;
		string prenom;
		uint age;
	public:
		//Forme cannonique de coplien
		Personne();
		Personne(const Personne&);
		~Personne();
		Personne& operator=(const Personne&);

		
		Personne(string, string, uint);
		friend ostream& operator<<(ostream&, const Personne&);
	
};

#endif
