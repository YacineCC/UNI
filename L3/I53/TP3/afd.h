#ifndef AFD_H
#define AFD_H

#define AFD_ASCII_SHIFT 97
#define AFD_NB_SYMB 26

struct AFD{
  int Q, q0;
  int *F;
  char * sigma;
  int **delta;
};


typedef struct AFD * AFD;

AFD afd_init(int Q, int q0, int * F, char * sigma);
void afd_ajouter_transition(AFD A, int q1, char s, int q2);
void afd_print(AFD A);
void afd_free(AFD A);

AFD afd_finit(char *file);
int afd_simuler(AFD A, char *s);

#endif
