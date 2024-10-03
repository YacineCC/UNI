#ifndef PROFESSEUR_H
#define PROFESSEUR_H
#include "personne.h"


class Professeur : public Personne
{
    private:
        string statut;
        uint heures;
    public:
        Professeur(string,string, string, uint);
        void Affic();
        void Travailler(uint);

};

#endif
