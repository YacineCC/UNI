#include "episode.h"

Episode::Episode() : Serie()
{
    titreEpisode = "";
    numEpisode = 0;
    numSaison = 0;
    duree = 0;
}

Episode::Episode(string tserie, bool estcomedie, string tgenre, int nbsaison, bool estpublic, string tepisode, int nepisode, int nsaison, float eduree) : Serie(tserie, estcomedie, tgenre,nbsaison, estpublic)
{
    titreEpisode = tepisode;
    numEpisode = nepisode;
    numSaison = nsaison;
    duree = eduree;
}

Episode::Episode(const Episode& E) : Serie(E)
{
    titreEpisode = E.titreEpisode;
    numEpisode = E.numEpisode;
    numSaison = E.numSaison;
    duree = E.duree;
}

bool Episode::shortcom()
{
    if((Serie::shortcom() == true) && (duree < 10))
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool Episode::sitcom()
{
    if((Serie::sitcom() == true) && (duree < 30))
    {
        return true;
    }
    else
    {
        return false;
    }
}


ostream& operator<<(ostream& o, const Episode& E)
{
    o<<"|Titre Serie : "<<E.Get_titreSerie()<<" |Num de saison : "<<E.Get_nbSaison()<<" |Num épisode : "<<E.numEpisode<<" |Titre épisode : "<<E.titreEpisode<<" |"<<endl;
    return o; 
}