#include "serie.h"




Serie::Serie()
{
    titreSerie = "";
    comedie = false;
    genre = "";
    nbSaison = 0;
    enPublic = false;
}

Serie::Serie(string titre, bool estcomedie, string genr, int nbs, bool estpublic)
{
    titreSerie = titre;
    comedie = estcomedie;
    genre = genr;
    nbSaison = nbs;
    enPublic = estpublic;
}

Serie::Serie(const Serie& S)
{
    titreSerie = S.titreSerie;
    comedie = S.comedie;
    genre = S.genre;
    nbSaison = S.nbSaison;
    enPublic = S.enPublic;
}


string Serie::Get_titreSerie() const
{
    return titreSerie;
}

int Serie::Get_nbSaison() const
{
    return nbSaison;
}

bool Serie::shortcom()
{
    if(comedie == true && enPublic == false)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool Serie::sitcom()
{
    if(comedie == true && enPublic == true)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void Serie::affiche()
{
    cout<<"|Titre Serie : "<<titreSerie<<" |comedie : "<<comedie<<" |genre : "<<genre<<" |nb saisons : "<<nbSaison<<" |en public : "<<enPublic<<endl;

}