#include "professeur.h"


Professeur::Professeur(string s, string n, string p, uint a) : Personne(n, p, a)
{
    statut = s;
    heures = 0;
}

void Professeur::Affic()
{
    Personne::Affic();
    cout<<"Statut : "<<statut<<"| Heures travaillées : "<<heures<<"|"<<endl;
}

void Professeur::Travailler(uint h)
{
    heures += h;
}

