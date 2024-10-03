#ifndef PERSONNE_H
#define PERSONNE_H
#include <iostream>
#include <string>
using std::string;
using std::cout;
using std::endl;
typedef unsigned int uint;
class Personne
{
    private:
        string nom;
        string prenom;
        uint age;
    public:
    	Personne();
        Personne(string, string, uint);
        void Affic();
        void Viellir();
};

#endif
