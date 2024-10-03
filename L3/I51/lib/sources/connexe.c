#include "connexe.h"
#include "pile.h"
void PPR(graphe* g, int s, int* v, liste* passage)
{
   
    if(v[s] == 1) return;
    empiler(passage, s, 0);
    
    v[s] = 1;   //Le sommet est visité.
    liste aux = g->adj[s];  //On prend le sommet s.
    while(aux != NULL)  //Parcours des voisins de s.
    {
        if(v[aux->num] == 0)    //Si le sommet n'a pas encore été visité.
        {
            
            PPR(g, aux->num, v, passage);
            
        }
        aux = aux->svt;

    }

}

int compConnexe(graphe* g)
{
    int* visite =(int*)calloc(g->nbs, sizeof(int));
    int p = 0;
    for(int s = 0; s < g->nbs; s++)
    {
        if(visite[s] == 0)
        {
            PPR(g, s, visite, NULL);  //1 PPR = 1 composante connexe.
            p++;
        }
    }
    free(visite);
    return p;
}

int estConnexe(graphe* g)
{
    return(compConnexe(g) == 1);
}


int degre(graphe* g, int s)
{
    int deg = 0;

    enrliste* aux = g->adj[s];
    while(aux != NULL)
    {
        aux = aux->svt;
        deg++;
    }
    return deg;
}
