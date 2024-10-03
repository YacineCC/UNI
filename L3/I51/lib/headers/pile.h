#ifndef PILE_H
#define PILE_H
#include "graphe_base.h"
#include <stdio.h>
#include <stdlib.h>

enrliste* creerElement(int);    //Alloue un élement comme un sommet d'un graphe par exemple.
void empiler(liste*, int, float);  //Ajoute en tête de liste un élement, utile pour ajouter une arrête à une liste d'adjacence.
int depiler(liste*);    //Retourne la tête d'une liste et avance la tête d'un élement, utile pour supprimer une arrête à une liste d'adjacence.
int est_vide(liste*);   //Retour >= 1 si la liste est vide (NULL) 0 sinon.

#endif
