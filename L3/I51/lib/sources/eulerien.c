#include <eulerien.h>


int estEulerien(graphe* g)
{
    if(estConnexe(g) != 1) return 0;
    int degimpair = 0;
    for(int s = 0; s < g->nbs; s++) if(degre(g, s) % 2 != 0) degimpair++;
    if(degimpair == 0) return 1;
    else return 0;
}


int estSemiEulerien(graphe* g)
{
    if(estConnexe(g) != 1)
    {
        return 0;
    }
    int degimpair = 0;
    for(int s = 0; s < g->nbs; s++) if(degre(g, s) % 2 != 0) degimpair++;
    if(degimpair <= 2) return 1;
    else return 0;

}