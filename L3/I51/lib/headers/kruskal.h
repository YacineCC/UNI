
#ifndef KRUSKAL_H
#define KRUSKAL_H
#include "graphe_base.h"
//Structure de point sous forme de coordonnées
typedef struct
{
    float x;
    float y;
}point;

//Structure d'arc avec deux sommet s1-->s2 et le poids
typedef struct
{
    int s1;
    int s2;
    double poids;
}arc;


double distance_euclidienne(point a, point b);
int comp_arr(const void *x, const void *y);
graphe* Kruskal(point* nuage, int n);
point* randNuage(int n);
#endif