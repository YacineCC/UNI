#include "graphe_base.h"
#include "pile.h"
graphe* initGraphe(int n)
{
    graphe* g = (graphe*)malloc(sizeof(graphe));    //Aloue la structure du graphe.
    g->nbs = n; //Ordre du graphe.
    g->mat = (uchar**)calloc(n,sizeof(uchar*)); //Aloue les n lignes de la matrice d'adjacence.
    g->adj = (liste*)calloc(n,sizeof(enrliste*));   //Alloue les n élements de la liste d'adjacence.

    for(int i = 0; i < n; i++)
    {
        //g->mat[i] = (uchar*)calloc(n,sizeof(uchar));    //Aloue les n colonnes de la matrice d'adjacence.  
        g->adj[i] = NULL;   //!Bien mettre à NULL, les élements de la liste d'adjacence n'existent pas encore.
    }
    return g;

}

void ajoutArrete(graphe* g, int x, int y, float p)
{
    empiler(&(g->adj[x]), y, p);   //Ajout du sommet y dans la liste d'adjacence de x.
    empiler(&(g->adj[y]), x, p);   //Ajout du sommet x dans la liste d'adjacence de y.
}

void enleveArrete(graphe* g, int x, int y)
{
	liste tmp = g->adj[x];
	while(tmp->svt->num != y) tmp = tmp->svt;
	liste auxX = tmp->svt;
	tmp->svt = tmp->svt->svt;

	tmp = g->adj[y];
	while(tmp->svt->num != x) tmp = tmp->svt;
	liste auxY = tmp->svt;
	tmp->svt = tmp->svt->svt;
	free(auxX);
	free(auxY);

}

int nbArretes(graphe* g)
{
	int i;
	liste tmp;
	int nb = 0;
	for(i = 0; i < g->nbs; i++)
	{
		tmp = g->adj[i];
		while(tmp != NULL)
		{
			if(tmp->num > i)nb += 1;
			tmp = tmp->svt;
		}
	}
	return nb;
}

void randGraphe(graphe** g, float p)
{   int n = (*g)->nbs;
    freeGraphe(*g);
    *g = initGraphe(n);
    int seuil = RAND_MAX * p;
    for(int i = 0; i < (*g)->nbs; i++)
    {
        for(int j = i+1; j < (*g)->nbs; j++)    //(j = i+1)Pour ne pas répéter la liaison et fausée la probabilité.
        {
            if(rand() < seuil)  //Si la probabilité est atteinte.
            {
                //(*g)->mat[i][j] = (*g-)>mat[j][i] = 1;
                ajoutArrete(*g, i, j, rand()%20);
            }
        }
    }
}


void freeGraphe(graphe* g)
{
    liste aux;
    for(int i = 0; i < g->nbs; i++)
    {
        free(g->mat[i]);    //Libère chaque lignes de la matrice.
        while(g->adj[i] != NULL)    //Tant qu'il y a des voisins au sommet i.
        {
            aux = g->adj[i];
            g->adj[i] = g->adj[i]->svt;
            free(aux);  //On libère chaque voisins à l'aide d'une variable auxiliaire.
        }
    }
    free(g->mat);   //Libère la matrice.
    free(g->adj);   //Libère la liste de sommet.
    free(g);    //Libère la structure//!A ne pas oublier pour être libre des fuites mémoire.
}
