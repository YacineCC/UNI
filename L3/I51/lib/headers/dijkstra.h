#ifndef DIJKSTRA_H
#define DIJKSTRA_H
#include "graphe_base.h"


int choisir(int* e, int* v, graphe* g);
void miseajour(int s, int* e, int* r, int* v, graphe* g);
void dijkstra(int a, int b, graphe* g);

#endif
