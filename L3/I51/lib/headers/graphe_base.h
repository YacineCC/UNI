#ifndef GRAPHE_BASE_H
#define GRAPHE_BASE_H

typedef unsigned char uchar;

//Structure de liste chainée.
typedef struct enrliste enrliste;
struct enrliste
{
    int num;    //Nom du sommet.
    enrliste* svt;  //enr : enregistrement. Pointeur sur le prochain élement de la liste.
	float poids;
};
typedef enrliste* liste;    //Pointeur sur la tete de la liste.

typedef struct 
{
    int nbs;    //Ordre du graphe.
    uchar** mat;    //Matrice d'adjacence.
    liste* adj; //Liste d'adjacence.
}graphe;




graphe* initGraphe(int);    //Allocation d'un graphe, pas d'initialisation.
void ajoutArrete(graphe*, int, int, float);    //Ajoute une arrête entre deux sommets du graphe.
void enleveArrete(graphe* g, int x, int y);
int nbArretes(graphe* g);
void randGraphe(graphe**, float);  //Rend aléatoire l'adjacence des sommets d'un graphe.
void freeGraphe(graphe*);   //Libère l'allocation du graphe pour ne pas avoir de fuites mémoires.

#endif
