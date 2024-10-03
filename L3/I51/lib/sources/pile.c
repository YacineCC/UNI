#include "pile.h"

enrliste* creerElement(int nom)
{
    enrliste* e = (enrliste*)malloc(sizeof(enrliste));
    e->num =  nom;
	e->poids = 0;
    e->svt = NULL;
    return e;
}

void empiler(liste* l, int nom, float p)
{
    if(l == NULL)
        exit(EXIT_FAILURE);
    if(*l == NULL)  //Si il n'y a pas de voisin, le premier voisin est nom.
	{
        *l = creerElement(nom);
		(*l)->poids = p;
	}	
    else
    {
    enrliste* e = creerElement(nom);
	e->poids = p;
    e->svt = *l;
    *l = e;
    }
}

int depiler(liste* l)
{
    enrliste* e = *l;
    *l = (*l)->svt;
    int res = e->num;
    free(e);
    return res;

}

int est_vide(liste* l)
{
    return !l;
}
