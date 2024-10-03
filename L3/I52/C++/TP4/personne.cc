#include "personne.h"

Personne::Personne()
{
    nom = "";
    prenom = "";
    age = 0;
}

Personne::Personne(string n, string pre, uint a)
{
    nom = n;
    prenom = pre;
    age = a;
}

void Personne::Affic()
{
    cout<<"|Nom : "<<nom<<"| Prénom : "<<prenom<<"| âge : "<<age<<'|';
}

void Personne::Viellir()
{
    age += 1;
}
