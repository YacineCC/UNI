#ifndef INOUT_H
#define INOUT_H

#include "graphe_base.h"
#include <stdio.h>
#include <stdlib.h>
FILE* ouvrir(char*);    //Ouvre un fichier dans le répertoire courant où dans I51/entrees/ sinon. 
void minilire(char*);   //Affiche sur le terminal l'odre d'un graphe et ses arrêtes depuis un fichier texte.
graphe* lireGraphe(char*);  //Retourne un graphe depuis un fichier texte.
void ecrireGraphe(char*, graphe*); //Produit un fichier texte dans I51/sorties/ depuis un graphe.
void dessiner(char*, graphe*);  //Produit un png dans I51/sorties/ depuis un graphe à l'aide de la commande dot.
void afficheAdj(graphe*);   //Affiche sur le terminal la liste d'adjacence des sommets du graphe.

#endif
