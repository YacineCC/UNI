#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include "afd.h"

/*
 * FUNCTION: afd_init
 * ------------------
 * initialise et retourne un AFD dont les états sont numérotés de 0 à `Q`
 * 
 * param: 
 *        Q  - plus grandétat de l'automate
 *        q0 - état inital    
 *        nbFinals - nombre d'états finals
 *        listFinals - tableau de `nbFinals` entiers représentant les états finals
 *        Sigma - alphabet de l'automate
 * 
 * return:
 *        un AFD dont la tableau de transition est allouée mais vide
 */
AFD afd_init(int Q, int q0, int *F, char * sigma){
  AFD A; 
  if ( (A=malloc(sizeof(struct AFD))) == NULL){
    printf("malloc error A");
    exit(1);
  }
  A->Q = Q;
  A->q0 = q0;

  int  nbFinals=1;
  for (int i=0; F[i]!=-1; i++) nbFinals++; 
  if ( (A->F = malloc(sizeof(int)*nbFinals)) == NULL){
    printf("malloc error A->F");
    exit(1);
  }
  for (int i=0; i<nbFinals; i++) A->F[i] = F[i];
   
  if ( (A->sigma = malloc( sizeof(char)*(strlen(sigma)+1))) == NULL){
    printf("malloc error A->sigma");
    exit(1);
  }
  strcpy(A->sigma,sigma);

  if ((A->delta = malloc( sizeof(int**)*(Q+1)))==NULL){
    printf("malloc error A->delta");
    exit(1);
  }

  for (int q=0; q<A->Q+1; q++){
    if( (A->delta[q] = malloc( sizeof(int *)*(AFD_NB_SYMB)))==NULL){
      printf("malloc error A->delta[%d]", q);
      exit(1);
    }
    for (int s=0; s<AFD_NB_SYMB; s++){
      A->delta[q][s]=-1;
    }
  }
  return A;
}


/*
 * FUNCTION: afd_ajouter_transition
 * --------------------------------
 * ajoute la transition  `q1` -- `s` --> `q2` à l'automate `A`
 * 
 * param: 
 *        A  - un AFD
 *        q1 - état de départ de la transition    
 *        s  - étiquette de la transition
 *        q2 - état d'arrivée de la transition    
 */
void afd_ajouter_transition(AFD A, int q1, char s, int q2){
  A->delta[q1][s-AFD_ASCII_SHIFT] = q2;
}


/*
 * FUNCTION: afd_print
 * -------------------
 * affiche l'AFD `A`
 * 
 * param: 
 *        A  - un AFD
 */
void afd_print(AFD A){
  printf("Q = {0,..,%d}\n", A->Q);
  printf("q0 = %d\n", A->q0);
  printf("F = {");
  for (int i=0; A->F[i]!=-1; i++) printf("%d,",A->F[i]);
  printf("\b}\n");

  int * sigma = calloc(sizeof(int),AFD_NB_SYMB);
  int nb_symb=strlen(A->sigma);

  for (unsigned i=0; i < strlen(A->sigma); i++){
    sigma[(int)A->sigma[i]-AFD_ASCII_SHIFT] = 1;
  }
  
  int cellsize = (int)(ceil(log10( (double)A->Q)))+1;
  int first_column_size = cellsize>=5 ? cellsize+2 : 7;
  int padding = (cellsize>=5)? (cellsize-5)/2+1: 1;
  int line_length = first_column_size+1+(cellsize+2)*(nb_symb);
  char * line = malloc(sizeof(char)*(line_length+2));

   
  for (int i=0; i<=line_length; i++) line[i]='-';
  line[line_length+1]='\0';

  printf("%s\n",line);
  printf("|%*sdelta |", padding, "");
  for (int i=0; i<AFD_NB_SYMB; i++) {
    if (sigma[i])
      printf("%*c |", cellsize, (char)i+AFD_ASCII_SHIFT);
  }
  printf("\n%s\n",line);
  
  for (int q=0; q<A->Q+1; q++){
    printf("|%*d |", padding+5, q);
    for (int i=0; i<AFD_NB_SYMB; i++){
      int s = i;
      if (sigma[i]){
      if (A->delta[q][s] !=-1){
	printf("%*d |", cellsize, A->delta[q][s]);
      }
      else
	printf("%*s |", cellsize, "");
      }
    }
    printf("\n");
    printf("%s\n",line);
  }
  free(sigma);
  free(line);
}

/*
 * FUNCTION: afd_free
 * -------------------
 * libère la mémoire de l'AFD `A` initialisé par la fonction afd_init 
 * 
 * param: 
 *        A  - un AFD
 */
void afd_free(AFD A){
  free(A->F);
  free(A->sigma);
  for (int q=0; q<A->Q+1; q++) free(A->delta[q]);
  free(A->delta);
  free(A);  
}


/*
 * FUNCTION: afd_finit
 * ------------------
 * initialise et renvoie un AFD à partir du fichier `file` écrit au format:
 * 
 *  'nombre_etat
 *  'etat_initial
 *  'nombre_etats_finals
 *  'etat_final_1 etat_final_2 ... etat_final_n
 *  'alphabet
 *  'etat_i1 symbole_k1 etat_j1
 *  'etat_i2 symbole_k2 etat_j2
 *  '...
 *  'etat_in symbole_kn etat_jn 
 * 
 * param :
 *         file - un nom de fichier
 * return:
 *         un AFD complet
 */
AFD afd_finit(char *file){
  FILE * fd;
  if ( (fd = fopen(file,"r"))==NULL ){
    printf("impossible d'ouvrir le fichier %s\n",file);
    exit(1);
  }

  int Q,q0,nbFinals;
  if ( fscanf(fd,"%d %d %d",&Q,&q0,&nbFinals)!=3 ){
    printf("Problème de formatage du fichier ligne 1 à 3\n");
    exit(1);
  }
	
  int * listFinals;
  if ( (listFinals=malloc(sizeof(int)*(nbFinals+1)))==NULL ){
    printf("Echec allocation mémoire etas finals\n");
    exit(1);
  }
  for (int i=0; i<nbFinals; i++) fscanf(fd,"%d", &listFinals[i]);
  listFinals[nbFinals]=-1;

  char *sigma;
  if ( fscanf(fd,"%ms",&sigma)!=1 ){
    printf("Problème de lecture de l'alphabet\n");
    exit(1);
  }

  AFD A = afd_init(Q, q0, listFinals, sigma);

  int q1,q2;
  char s;

  while ( fscanf(fd,"%d %c %d",&q1,&s,&q2)==3 ){
    afd_ajouter_transition(A, q1, s, q2);
  }
  free(listFinals);
  free(sigma);
  fclose(fd);
  return A;
}

/*
 * FUNCTION: afd_simuler
 * ---------------------
 * renvoie 1 si la chaine `s` est acceptée par l'AFD `A`, 0 sinon
 *
 * param:
 *        A - un AFD
 *        s - la chaine de caractères à analyser
 */
int afd_simuler(AFD A, char *s){

  int i = 0;
  int q = A->q0;
  while(s[i] != '\0')
  {
    q = A->delta[q][s[i]-97];
    i++;
  }
  i = 0;
  while(A->F[i] != -1)
  {
    if(q == A-> F[i])
      return 1;
    i++;
  }
  return 0;
}
