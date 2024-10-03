#ifndef AFN_H
#define AFN_H

#include "afd.h"

#define MAX_INT_SIZE 10

#define AFN_ASCII_SHIFT 96
#define AFN_NB_SYMB 27

struct AFN{
  int Q;
  int *I,*F;
  char *sigma;
  int ***delta;
};

typedef struct AFN * AFN;

typedef struct pile pile;

struct pile
{
  int data;
  pile* nxt;
};

typedef pile* stack;

stack init_stack();
void stack_print();
void push(stack*, int);
int pop(stack*);

AFN afn_init(int Q, int * listInitiaux,  int * listFinals, char * sigma);
void afn_ajouter_transition(AFN A, int q1, char s, int q2);
void afn_print(AFN A);
void afn_free(AFN A);

AFN afn_finit(char *file);

int * afn_epsilon_fermeture(AFN A, int * R);
AFD afn_determinisation(AFN A);

void ajoute_etat(int *** listEtats, int  *etat);
int cherche_etat(int** listEtats, int  *etat);

int * set_union(int *R1, int *R2);
int * set_intersection(int *R1, int *R2);
void set_print(int *R);
int * random_set(int);
void tri(int**);

int ** init_listEtats(); //retourne un tableau d'ensemble à un élement = à {{-1}}
void free_listEtats(int**);
void listeEtats_print(int **);
int taille_listeEtats(int **);
int set_size(int * set);
int* set_shift(int* set, int decal);
AFN afn_char(char c, char* sigma);
AFN afn_union(AFN A, AFN B);
void transition_copy(AFN A, AFN B, int decal); //Copie les transitions de B dans A avec un decalage
AFN afn_concat(AFN A, AFN B);
AFN afn_kleene(AFN A);

#endif
