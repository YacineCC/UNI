#include "saison.h"

Saison::Saison()
{
    nbEpisodes = 0;
    liste = NULL;
}

Saison::Saison(int nb)
{
    nbEpisodes = nb;
    liste = new Episode[nb];
}

Saison::Saison(int nb, Episode* lep)
{
    nbEpisodes = nb;
    liste = new Episode[nbEpisodes];
    for(int i = 0; i < nbEpisodes; i++)
    {
        liste[i] = lep[i];
    }
}

Saison::Saison(const Saison& S)
{
    nbEpisodes = S.nbEpisodes;
    liste = new Episode[nbEpisodes];
    for(int i = 0; i < nbEpisodes; i++)
    {
        liste[i] = S.liste[i];
    }
}

Saison::~Saison()
{
    delete[] liste;
}

Saison& Saison::operator=(const Saison& S)
{
    if(this != &S)
    {
        nbEpisodes = S.nbEpisodes;
        delete[] liste;
        liste = new Episode[nbEpisodes];
        for(int i = 0; i < nbEpisodes; i++)
        {
            liste[i] = S.liste[i];
        }
    }
    return *this;
}

Saison Saison::operator+(const Episode& E) const
{
    Saison S(nbEpisodes+1);
    int i = 0;
    for(i = 0; i < nbEpisodes; i++)
    {
        S.liste[i] = liste[i];
    }
    S.liste[i] = E;
    return S;

}

Saison operator+(const Episode& E, Saison& S)
{
    int nb = S.get_nbEpisodes();
    Saison res(nb+1);
    int i = 0;
    for(i = 0; i< nb; i++)
    {
        res.liste[i] = S[i];
    }
    res.liste[i] = E;
    return res;
}

Saison Saison::sitcom()
{
    Saison S;
    for(int i = 0; i < nbEpisodes; i++)
    {
        if((liste[i].Episode::sitcom()) == true)
        {
            S = S+liste[i];
        }
    }
    return S;
}
