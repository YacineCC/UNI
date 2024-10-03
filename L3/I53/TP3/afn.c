#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include "afn.h"
#include "stdlib.h"

void listeEtats_print(int ** L)
{
  if(taille_listeEtats(L) == 0)
    printf("{}\n");
  else
  {
  printf("{");
  set_print(L[0]);
  for(int i = 1; L[i] != NULL; i++)
  {
    printf(", ");
    set_print(L[i]);
  }
  printf("}\n");
  }
}

void tri(int** r)
{
  int tmp;
  for(int i = 0; (*r)[i+1] != -1; i++)
  {
    for(int j = 0; (*r)[j+i+1] != -1; j++)
    {
      if((*r)[j]>(*r)[j+1])
      {
        tmp = (*r)[j];
        (*r)[j] = (*r)[j+1];
        (*r)[j+1] = tmp;
        
      }
    }
  }
}

int * random_set(int n)
{
  int * r = (int*)malloc((n+1)*sizeof(int));
  int test, flag;
  int i = 0;
  r[n] = -1;
  while(i < n)
  {
    flag = 1;
    test = rand()%10;
    for(int j = 0; j < i; j++)
    {
      if(test == r[j])
        flag = 0;
    }
    if(flag)
    {
      r[i] = test;
      i++;
    }
    
    
  }
  tri(&r);
  
  return r;
}


/*
 * FUNCTION: afn_init
 * ------------------
 * initialise et retourne un AFN dont les états sont numérotés de 0 à `Q`
 * ajoute le symbole '&' en début d'alphabet si celui-ci n'y est pas déjà
 * 
 * param: 
 *        Q  - plus grand état de l'automate
 *        nbInitaux - nombre d'états initiaux
 *        listInitiaux - tableau de `nbInitiaux` entiers représentant les états initiaux
 *        nbFinals - nombre d'états finals
 *        listFinals - tableau de `nbFinals` entiers représentant les états finals
 *        Sigma - alphabet de l'automate
 * 
 * return:
 *        un AFN dont la tableau de transition est allouée mais vide
 */
AFN  afn_init(int Q,  int * I, int * F, char *sigma){
  AFN A; 
  if ( (A=malloc(sizeof(struct AFN))) == NULL){
    printf("malloc error A");
    exit(1);
  }
  A->Q = Q;

  int nbInitiaux=1;
  for (int i=0; I[i]!=-1;i++) nbInitiaux++;
  if ( (A->I = malloc(sizeof(int)*(nbInitiaux))) == NULL){
    printf("malloc error A->I");
    exit(1);
  }
  for (int i=0; i<nbInitiaux; i++) A->I[i] = I[i];
  
  int nbFinals=1;
  for (int i=0; F[i]!=-1;i++) nbFinals++;
  if ( (A->F = malloc(sizeof(int)*(nbFinals))) == NULL){
    printf("malloc error A->F");
    exit(1);
  }
  for (int i=0; i<nbFinals; i++) A->F[i] = F[i];
  
  
  if ( (A->sigma = malloc( sizeof(char)*(strlen(sigma)+1))) == NULL){
    printf("malloc error A->sigma");
    exit(1);
  }
  strcpy(A->sigma,sigma);
  
  if ((A->delta = malloc( sizeof(int***)*(Q+1)))==NULL){
    printf("malloc error A->delta");
    exit(1);
  }
  for (int q=0; q<A->Q+1; q++){
    if( (A->delta[q] = malloc( sizeof(int **)*AFN_NB_SYMB))==NULL){
      printf("malloc error A->delta[%d]", q);
      exit(1);
    }
    for (int s=0; s<AFN_NB_SYMB; s++)	A->delta[q][s]=NULL;
  }
  return A;
}

/*
 * FUNCTION: afn_ajouter_transition
 * --------------------------------
 * ajoute la transition  `q1` -- `s` --> `q2` à l'automate `A` où l'ensemble des transitions
 * partant de l'état `q1` et étiquetées par le symbole `s` delta[q][s] est un tableau 
 * d'entiers trié dans l'ordre croissant et se terminant par -1, NULL si vide
 * 
 * param: 
 *        A  - un AFN
 *        q1 - état de départ de la transition    
 *        s  - étiquette de la transition
 *        q2 - état d'arrivée de la transition    
 */
void afn_ajouter_transition(AFN A, int q1, char s, int q2){
  int symb = (s=='&' ? 0 : s-AFN_ASCII_SHIFT);
  if (A->delta[q1][symb]==NULL){
    A->delta[q1][symb]=malloc(sizeof(int)*2);
    A->delta[q1][symb][0]=q2;
    A->delta[q1][symb][1]=-1;
  } else {
    int i=0;
    while (A->delta[q1][symb][i]!=-1) i++;  
    
    if ( (A->delta[q1][symb]=reallocarray(A->delta[q1][symb], i+2, sizeof(int)))==NULL){
      printf("impossible de réallouer la mémoire du bloc (%d,%c)",q1,s);
    }; 
    
    A->delta[q1][symb][i+1] = A->delta[q1][symb][i]; i--; 
    while ( i>=0 ){
      if (A->delta[q1][symb][i] == q2 ) break; 
      if (A->delta[q1][symb][i] < q2){
	A->delta[q1][symb][i+1] = q2;
	break;
      }
      if (A->delta[q1][symb][i] > q2){
	    A->delta[q1][symb][i+1] = A->delta[q1][symb][i];
	    i--; 
      } 
    }
    if (i == -1) A->delta[q1][symb][0] = q2;
  }
}

/*
 * FUNCTION: afn_print
 * -------------------
 * affiche l'AFN `A`
 * 
 * param: 
 *        A  - un AFN
 */
void afn_print(AFN A){
  printf("Q = {0,..,%d}\n", A->Q);
  printf("I = {");
  for (int i=0; A->I[i]!=-1; i++) printf("%d,",A->I[i]);
  printf("\b}\n");

  printf("F = {");
  for (int i=0; A->F[i]!=-1; i++) printf("%d,",A->F[i]);
  printf("\b}\n");
  printf("Sigma = %s\n",A->sigma);

  int * sigma = calloc(sizeof(int),AFN_NB_SYMB);
  int nb_symb=strlen(A->sigma)+1;

  sigma[0]=1;
  for (unsigned i=0; i < strlen(A->sigma); i++){
    sigma[(int)A->sigma[i]-AFN_ASCII_SHIFT] = 1;
  }
  
  int state_size = (int)(ceil(log10( (double)A->Q)));
  int padding = (state_size>=5)? (state_size-5)/2+1: 1;
  int first_column_size = state_size>=5 ? state_size+2 : 7;
  int max_cell_size = 0;

  for (int q=0; q<A->Q; q++){
    for (int s=0; s<AFN_NB_SYMB; s++){
      if (A->delta[q][s]!=NULL){
	int cell_size = 0;
	
	while (A->delta[q][s][cell_size]!=-1) cell_size++;
	max_cell_size = (max_cell_size < cell_size ? cell_size : max_cell_size);
      }
    }
  }
  
  int total_cell_size;
  if (max_cell_size == 1){
    total_cell_size=max_cell_size*(state_size+1)+2;
  } else {
    total_cell_size=max_cell_size*(state_size+1)+1;
  }
  int line_length = first_column_size+1+(total_cell_size+1)*nb_symb;
  char * line = malloc(sizeof(char)*(line_length+2));
  for (int i=0; i<=line_length; i++) line[i]='-';
  line[line_length+1]='\0';
  printf("%s\n",line);
  printf("|%*sdelta |", padding, "");
  for (int i=0; i<AFN_NB_SYMB; i++){
    if (sigma[i]==1)
      printf("%*c |", total_cell_size-1, (i==0)?'&':(char)i+AFN_ASCII_SHIFT);
  }
  printf("\n");
  printf("%s\n",line);

  char *buffer = malloc(sizeof(char)*(total_cell_size+1));
  char state_char[MAX_INT_SIZE];
  for (int q=0; q<A->Q+1; q++){
    printf("|%*d |", padding+5, q);
    for (int i=0; i<AFN_NB_SYMB; i++){
      if (sigma[i]==0) continue;
      int s = i;
      if (A->delta[q][s] != NULL){
	int j=0;
	buffer[0]='{';
	buffer[1]='\0';
	while (A->delta[q][s][j]!=-1) {
	  sprintf(state_char,"%d,", A->delta[q][s][j++]);
	  strcat(buffer, state_char);
	}
	printf("%*s\b}|", total_cell_size ,buffer );
      } else {
	printf("%*s|",total_cell_size,"");
      }
    }
    printf("\n");
    printf("%s\n",line);
  }
  free(sigma);
  free(buffer);
  free(line);
}

/*
 * FUNCTION: afn_free
 * -------------------
 * libère la mémoire de l'AFN `A` initialisé par la fonction afn_init 
 * 
 * param: 
 *        A  - un AFN
 */
void afn_free(AFN A){
  free(A->I);
  free(A->F);
  free(A->sigma);
  for (int q=0; q<A->Q+1; q++){
    for (int s=0; s<AFN_NB_SYMB; s++){
      if (A->delta[q][s]!=NULL)
	free(A->delta[q][s]);
    }
    free(A->delta[q]);
  }
  free(A->delta);
  free(A);  
}


/*
 * FUNCTION: afn_finit
 * ------------------
 * initialise et renvoie un AFN à partir du fichier `file` écrit au format:
 * 
 *  'nombre_etat
 *  'nombre_etats_initiaux
 *  'etat_initial_1 etat_initial_2 ... etat_initial_n
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
 *         un AFN complet
 */
AFN afn_finit(char *file){
  FILE * fd;
  if ( (fd = fopen(file,"r"))==NULL ){
    printf("impossible d'ouvrir le fichier %s\n",file);
    exit(1);
  }

  int Q;
  if ( fscanf(fd,"%d",&Q)!=1 ){
    printf("Problème de formatage du fichier ligne 1\n");
    exit(1);
  }

  int nbInitiaux, *listInitiaux;
  if ( fscanf(fd,"%d",&nbInitiaux)!=1 ){
    printf("Problème formatage du fichier ligne 4\n");
    exit(1);
  }
  if ( (listInitiaux=malloc(sizeof(int)*(nbInitiaux+1)))==NULL ){
    printf("Echec allocation mémoire etas finals\n");
    exit(1);
  }
  for (int i=0; i<nbInitiaux; i++) fscanf(fd,"%d", &listInitiaux[i]);
  listInitiaux[nbInitiaux]=-1;
  
  int nbFinals,* listFinals;
  if ( fscanf(fd,"%d",&nbFinals)!=1 ){
    printf("Problème formatage du fichier ligne 4\n");
    exit(1);
  }
  if ( (listFinals=malloc(sizeof(int)*(nbFinals+1)))==NULL ){
    printf("Echec allocation mémoire etas finals\n");
    exit(1);
  }
  for (int i=0; i<nbFinals; i++) fscanf(fd,"%d", &listFinals[i]);
  listFinals[nbFinals]=-1;
  
  char *Sigma;
  if ( fscanf(fd,"%ms",&Sigma)!=1 ){
    printf("Problème de lecture de l'alphabet\n");
    exit(1);
  }

  
  AFN A = afn_init(Q, listInitiaux, listFinals, Sigma);

  int q1,q2;
  char s;

  while ( fscanf(fd,"%d %c %d",&q1,&s,&q2)==3 ){
    afn_ajouter_transition(A, q1, s, q2);
  }
  free(listInitiaux);
  free(listFinals);
  free(Sigma);
  fclose(fd);
  return A;
}

/*
 * FUNCTION: afn_epsilon_fermeture
 * -------------------------------
 * renvoie l'epsilon fermeture de l'ensemble `R` par rapport a l'automate `A`
 * 
 * param :
 *         A - un automate
 *         R - un ensemble sous forme de tableau terminant par -1, NULL si vide
 * return:
 *         l'epsilon fermeture de R sous forme de tableau, {-1} si vide
 */

stack init_stack(int data)
{
  stack s =(stack)malloc(sizeof(pile));
  s->nxt = NULL;
  s->data = data;
  return s;
}

void stack_print(stack s)
{
  printf("[");
  if(s != NULL)
  {
    printf("%d", s->data);
    stack p = s->nxt;
    while(p != NULL)
    {
      printf(", %d",p->data);
      p = p->nxt;
    }
    
  }
  printf("]\n");
  
  
  
}

void push(stack* s, int data)
{
  stack tmp =(stack)malloc(sizeof(pile));
  tmp->data = data;
  tmp->nxt = (*s);
  (*s) = tmp; 
}

int pop(stack* s)
{
  if((*s) == NULL)
  {
    perror("Pile vide");
    exit(1);
  }
  stack res = (*s);
  (*s) = (*s)->nxt;
  int r = res->data;
  res->nxt = NULL;
  free(res);
  res = NULL;
  return r;


}


int * afn_epsilon_fermeture(AFN A, int * R){
  
  int* epsfer =(int*)calloc((A->Q + 2),(sizeof(int)));
  stack s = init_stack(R[0]);
  epsfer[R[0]] = 1;

  for(int i = 1; R[i] != -1; i++)
  {
    push(&s, R[i]);
    epsfer[R[i]] = 1;
    
  } 
  
  int tmp;
  int* qprime;
  int j;
  while(s != NULL)
  {
    
    tmp = pop(&s);
    
   
    qprime = A->delta[tmp]['&'-38];
   

    j = 0;
    while((qprime != NULL) && (qprime[j] != -1))
    {
      
      
      if(epsfer[qprime[j]] == 0)
      {
        push(&s, qprime[j]);
        epsfer[qprime[j]] = 1;
      }
      
      
    
      j++;
    }
    
  }
  epsfer[A->Q+1] = -1;
  int* res =(int*)malloc(sizeof(int)*(A->Q+2));
  int k = 0;
  for(int i = 0; epsfer[i] != -1; i++)
  {
    if(epsfer[i] == 1)
    {
      res[k] = i;
      k++;
    }
  }
  res[k] = -1;
  res = reallocarray(res,k+1, sizeof(int));
  
  free(epsfer);
  return res;
 
}

/*
 * FUNCTION: ajouter_etat
 * ----------------------
 * ajouter un etat (sous forme d'ensemble) a la liste d'etat `listEtats`
 *
 * param:
 *         listEtats - un tableau de tableau
 *         i         - l'indice ou ajouter le nouvel état
 *         etat      - l'etat sous forme de tableau se terminant par -1
 */

int ** init_listEtats()
{
  int **L =(int**)malloc(sizeof(int *));
  L[0] = NULL;
  return L;
}

int taille_listeEtats(int ** listeEtats)
{
  int size = 0;
  for(size = 0; listeEtats[size] != NULL; size++);
  return size;
}




void ajoute_etat(int *** listeEtats, int  *etat){

  int size = taille_listeEtats(*listeEtats); // Donne la taille de la liste sans le NULL de fin
  
  
  (*listeEtats) = reallocarray(*listeEtats, size+2, sizeof(int*));  //Réalloue la liste + le nouvel état et l'état de fin NULL
  
  int * tmp = (*listeEtats)[size];
  (*listeEtats)[size] = etat;
  (*listeEtats)[size+1] = tmp;

  
}

void free_listEtats(int ** L)
{
  int i = 0;
  for(i = 0; L[i] != NULL; i++)
  {
    free(L[i]);
  }
  free(L[i]);
  free(L);
}

/*
 * FUNCTION: cherche_etat
 * ----------------------
 * cherche l'etat `etat`  dans la liste d'état `listEtats` et renvoie son indice, -1 si absent
 *
 * param:
 *         listEtats - un tableau de tableau se terminant par -1
 *         listSize  - nombre d'element de listEtats
 *         etat      - l'etat sous forme de tableau se terminant par -1
 */
int cherche_etat(int** listEtats, int  *etat){
  int i = 0;
  int j;
  while(listEtats[i] != NULL)
  {
    j = 0;
    while(listEtats[i][j] != -1 && listEtats[i][j] != -1 && listEtats[i][j] == etat[j])
      j += 1;
    if(etat[j] == -1 && listEtats[i][j] == -1)
      return i;
    i += 1;
  }
  return -1;
}

/*
 * FUNCTION: set_print
 * ----------------------
 * affiche l'ensemble `R`
 *
 * param:
 *        R - un ensemble sous forme de tableau terminant par -1, NULL si vide
 */
void set_print(int *R){
  if (R==NULL){
    printf("{}");
  }
  printf("{");
  int i;
  for (i=0; R[i]!= -1; i++) printf("%d,",R[i]);
  if (i==0) printf("}");
  else  printf("\b}");
}

/*
 * FUNCTION: set_union
 * ----------------------
 * renvoie l'union des ensembles `R1` et `R2`
 *
 * param:
 *        R1 - un ensemble sous forme de tableau terminant par -1, NULL si vide
 *        R2 - un ensemble sous forme de tableau terminant par -1, NULL si vide
 *
 * return:
 *        l'union des  ensembles sous forme de tableau terminant par -1, NULL si vide
 */

int * set_union(int *R1, int *R2){
  int sizeR1 = 0;
  while(R1[sizeR1] != -1) sizeR1++;
  
  
  int sizeR2 = 0;
  while(R2[sizeR2] != -1) sizeR2++;
    
  int sizeUnion = sizeR1 + sizeR2;

  int* Union =(int*)calloc(sizeUnion+1,sizeof(int));

  
 


  int i = 0; int j = 0; int k = 0; int z = 0;
  
  while((i < sizeR1) && (j < sizeR2))
  {
    
    if(R1[i] < R2[j])
    {
      Union[k] = R1[i];
      i += 1;
      k += 1;
    }
    else if(R2[j] < R1[i])
    {
      Union[k] = R2[j]; 
      j += 1;
      k += 1;
    }
    else
    {
      Union[k] = R1[i];
      i += 1;
      j += 1;
      k += 1;
      z++;
    }
    
  
  }

  while(i < sizeR1)
  {

    Union[k] = R1[i];
    i++;
    k++;
  }
  while(j < sizeR2)
  {
    
    Union[k] = R2[j];
    j++;
    k++;
  }
  

  int test = 1;
  while(Union[test] !=0 && test < sizeUnion)
    test++;
  if(test != sizeUnion)
    Union[test] = -1;
  else
    Union[sizeUnion-z] = -1;

  

  
  
  return Union;
}
/*
 * FUNCTION: set_intersection
 * ----------------------
 * renvoie l'intersection des ensembles `R1` et `R2`
 *
 * param:
 *        R1 - un ensemble sous forme de tableau terminant par -1, NULL si vide
 *        R2 - un ensemble sous forme de tableau terminant par -1, NULL si vide
 *
 * return:
 *        l'intersection des  ensembles sous forme de tableau terminant par -1, NULL si vide
 */

int * set_intersection(int *R1, int *R2){
  int sizeR1 = 0;
  while(R1[sizeR1] != -1) sizeR1++;
  
  
  int sizeR2 = 0;
  while(R2[sizeR2] != -1) sizeR2++;
    
  int sizeInter = sizeR1 + sizeR2;

  int* Inter =(int*)calloc(sizeInter,sizeof(int));

  
 


  int i = 0; int j = 0; int k = 0;
  
  while((i < sizeR1) && (j < sizeR2))
  {
    
    if(R1[i] < R2[j])
    {
      
      i += 1;
      
    }
    else if(R2[j] < R1[i])
    {
    
      j += 1;
      
    }
    else
    {
      Inter[k] = R1[i];
      i += 1;
      j += 1;
      k += 1;
    }
    
  
  }

  Inter[k] = -1;
  

  
  
  return Inter;

}


/*
 * FUNCTION: afn_determinisation
 * -------------------------------
 * renvoie un AFD equivalent à l'AFN en entrée
 * 
 * param :
 *         A - un AFN
 * return:
 *         un AFD equivalent
 */

AFD afn_determinisation(AFN A){

  char* sigma = A->sigma;
  int * q0 = afn_epsilon_fermeture(A, A->I);
  int ** Qb = init_listEtats();
  ajoute_etat(&Qb, q0);
  int * Fb = A->F;
  


  int* R =(int*)malloc(sizeof(int));

  for(int i = 0; Qb[i] != NULL; i++)
  {
    R[0] = -1;
    for(int j = 0; Qb[i][j] != -1 ; j++)
    {
      for(int k = 'a'; k <= 'z'; k++)
      {
        if(A->delta[Qb[i][j]][k-96] != NULL)
        {
          R = set_union(R, A->delta[Qb[i][j]][k-96]);
          //for(int k = 0; )
          //  afd_ajouter_transition(A, i, i-96, j);
          

        }
      }
      
    }
    R = afn_epsilon_fermeture(A,R);
    //for(int test = 0; R[i] != -1 && A->delta[Qb[i][j]][i-96])
    if(cherche_etat(Qb, R) == -1)
    {
      ajoute_etat(&Qb, R);
      
    }
    
  }

  /*
  int** indice = init_listEtats();
  
  ajoute_etat(&indice, afn_epsilon_fermeture(A,A->I));
  listeEtats_print(indice);
  int* R =(int*)malloc(sizeof(int));
  R[0] = -1;
  for(int i = 0; indice[i] != NULL; i++)
  {
    for(int j = 0; indice[i][j] != -1 ; j++)
    {
      if(A->delta[indice[i][j]]['a'-96] != NULL)
      {
        R = set_union(R,A->delta[indice[i][j]]['a'-96]);
        
      }
      R = afn_epsilon_fermeture(A,R);

    }
   
    set_print(R);
  }
  */
  ajoute_etat(&Qb, NULL);
  listeEtats_print(Qb);
  AFD Deter = afd_init(Qb, 0, Fb, sigma);
  return Deter;
  
}

AFN afn_char(char c, char* sigma)
{
  int Q = 1;
  int I[2] = {0, -1};
  int F[2] = {1, -1};
  AFN C = afn_init(Q, I, F, sigma);
  afn_ajouter_transition(C, 0, c, 1);
  return C;
}

int set_size(int * set)
{
  int i = 0;
  while(set[i] != -1) i++;
  
  return i;
}

int* set_shift(int* set, int decal)
{
  int setTaille =  set_size(set); 
  int* res = calloc(setTaille + 1, sizeof(int));
  res[setTaille] = -1;
  for(int i = 0; set[i] != -1; i++)
  {
    res[i] = set[i]+decal;
  }
  return res;
}

void transition_copy(AFN A, AFN B, int decal)
{
  int * p;
  int c;
  for(int q = 0; q <= B->Q; q++)
  {
    for(int k = 0; k < B->sigma[k] != '\0'; k++)
    {
      c = B->sigma[k];
      
      if((p = B->delta[q][c-AFN_ASCII_SHIFT]) == NULL)
        continue;
      
      for(int j = 0; p[j] != -1; j++)
      {
        afn_ajouter_transition(A, q+decal, c, p[j]+decal);
      }
      
      
    }
  }
}

AFN afn_concat(AFN A, AFN B)
{
  int Q = A->Q + B->Q + 1;
  int I[2] = {0, -1};
  int* F = set_shift(B->F,A->Q+1);

  AFN C = afn_init(Q, I, F, A->sigma);
  for(int  i = 0; A->F[i] != -1; i++)
  {
    afn_ajouter_transition(C, A->F[i], '&', A->Q+1);
  }
 
  transition_copy(C, A, 0);
  transition_copy(C, B, A->Q+1);
  
  free(F);
  return C;
}

AFN afn_kleene(AFN A)
{
  int Q = A->Q + 1;
  int I[2] = {0, -1};
  int* F = set_union(I, set_shift(A->F, 1));
  AFN C = afn_init(Q, I, F, A->sigma);
  for(int  i = 1; F[i] != -1; i++)
  {
    afn_ajouter_transition(C, F[i], '&', 0);
  }
  transition_copy(C, A, 1);
  
  for(int i = 1; i < Q-2; i += 2)
  {
    afn_ajouter_transition(C, i, '&', i+1);
  }
  afn_ajouter_transition(C, 0, '&', 1);
  afn_ajouter_transition(C, 1, '&', 2);
  afn_ajouter_transition(C, 1, '&', A->Q);
  return C;
}

AFN afn_union(AFN A, AFN B)
{
  int Q = A->Q + B->Q+2;
  int I[2] = {0, -1};
  int F_size = set_size(A->F) + set_size(B->F);
  int* F = calloc(F_size+1,sizeof(int));
  F[F_size] = -1;

  F = set_union(set_shift(A->F, 1), set_shift(B->F, A->Q+2));

  AFN C = afn_init(Q, I, F, A->sigma);

  afn_ajouter_transition(C, 0, '&', 1);
  afn_ajouter_transition(C, 0, '&', A->Q+2);
  
  transition_copy(C, A, 1);
  transition_copy(C, B, A->Q+2);
  free(F);
  return C;
}