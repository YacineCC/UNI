#ifndef CONNEXE_H
#define CONNEXE_H
#include <stdio.h>
#include <stdlib.h>
#include "graphe_base.h"
void PPR(graphe*, int, int*, liste*);   //Parcours en profondeur récursif utilisant les listes d'adjacence.
int compConnexe(graphe*);   //Retourne le nombre de composantes connexe.
int estConnexe(graphe*);    //Retourne 1 si le graphe est connexe. Si il n'a qu'une composante connexe.
int degre(graphe*, int); //Le degre d'un sommet du graphe.

#endif