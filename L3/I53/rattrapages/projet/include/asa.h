#ifndef ASA_H
#define ASA_H

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define  MAX_SIZE_FIELD_NAME  12
#define  MAX_SIZE_FIELD_VAL   32
#define  TXT_RED    "\x1b[31m"
#define  TXT_GREEN  "\x1b[32m"
#define  TXT_BLUE   "\x1b[34m"
#define  TXT_BOLD   "\x1b[1m"
#define  TXT_NULL   "\x1b[0m"

#define TYPE_ENTIER  'e'
#define TYPE_TABLEAU 't'
#define TYPE_PTR     'p'
#define TYPE_FCT     'f'

typedef enum {typeNB, type_ID, typeOP, type_INSTS, type_AFFECTATION, type_DECLAS_VARS, type_DECLA_VARS, type_FCT, type_DECLAS_FCT, type_PARAM_FCT, type_ROOT, type_SI, type_TQ, type_RETOURNER, type_ECRIRE, type_LIRE, type_NON} typeNoeud;

typedef struct {
  int val;
} feuilleNb;

typedef struct 
{
  char nom[32];
} feuille_ID;

typedef struct {
  int ope;
  struct asa * noeud[2];
} noeudOp;

typedef struct 
{
  struct asa* instruction;
  struct asa* instruction_svt;
} noeud_INSTS;

typedef struct 
{
  char id[32];
  struct asa* exp;
} noeud_AFFECTATION;

typedef struct 
{
  struct asa* decla_var;
  struct asa* decla_var_svt;
} noeud_DECLAS_VARS;

typedef struct 
{
  char id[32];
  struct asa* exp;
  struct asa* var_svt;
} noeud_DECLA_VARS;

typedef struct 
{
  char id[32];
  struct asa* param;
  struct asa* decla_var;
  struct asa* liste_insts;
} noeud_FCT;

typedef struct 
{
  struct asa* fct;
  struct asa* fct_svt;
} noeud_DECLAS_FCT;

typedef struct 
{
  struct asa* declas_vars;
  struct asa* declas_fcts;
  struct asa* main;
} noeud_ROOT;

typedef struct 
{
  struct asa* condition;
  struct asa* liste_insts_si;
  struct asa* liste_insts_sinon;

} noeud_SI;

typedef struct 
{
  struct asa* condition;
  struct asa* liste_insts;
} noeud_TQ;

typedef struct 
{
  struct asa* exp;
} noeud_RETOURNER;

typedef struct 
{
  char id[32];
  struct asa* param_svt;
} noeud_PARAM_FCT;

typedef struct 
{
  struct asa* exp;
} noeud_ECRIRE;

typedef struct 
{
  struct asa* exp;
} noeud_LIRE;

typedef struct 
{
  struct asa* exp;
} noeud_NON;




typedef struct asa{
  typeNoeud type;
  int memadr;
  int codelen;
  union {
    feuilleNb nb;
    feuille_ID id;
    noeudOp op;
    noeud_INSTS insts;
    noeud_AFFECTATION affectation;
    noeud_DECLAS_VARS declas_vars;
    noeud_DECLA_VARS decla_vars;
    noeud_FCT fct;
    noeud_DECLAS_FCT declas_fct;
    noeud_PARAM_FCT param_fct;
    noeud_ROOT root;
    noeud_SI si;
    noeud_TQ tq;
    noeud_RETOURNER retourner;
    noeud_ECRIRE ecrire;
    noeud_LIRE lire;
    noeud_NON non;
  };
} asa;



asa * creer_feuilleNB( int value );
asa* creer_feuille_ID(char* nom);
asa * creer_noeudOP( int ope, asa * p1, asa * p2 );
asa* creer_noeud_INSTS(asa* p1, asa* p2);
asa* creer_noeud_AFFECTATION(char* p1, asa* p2);
asa* creer_noeud_DECLAS_VARS(asa* p1, asa* p2);
asa* creer_noeud_DECLA_VARS(char* p1, asa* p2, asa* p3);
asa* creer_noeud_FCT(char* p1, asa* p2, asa* p3, asa* p4);
asa* creer_noeud_PARAM_FCT(char* p1, asa* p2);
asa* creer_noeud_ROOT(asa* p1, asa* p2, asa* p3);
asa* creer_noeud_DECLAS_FCT(asa* p1, asa* p2);
asa* creer_noeud_SI(asa* p1, asa* p2, asa* p3);
asa* creer_noeud_TQ(asa* p1, asa* p2);
asa* creer_noeud_RETOURNER(asa* p1);
asa* creer_noeud_ECRIRE(asa* p1);
asa* creer_noeud_LIRE(void);
asa* creer_noeud_NON(asa* p1);

void free_asa(asa *p);

void print_asa(asa * p);
void print_typeOP(asa *p);
void print_ID(asa* p);
void print_typeNB(asa *p);
void print_INSTS(asa* p);
void print_AFFECTATION(asa* p);
void print_DECLAS_VARS(asa* p);
void print_DECLA_VARS(asa* p);
void print_FCT(asa* p);
void print_DECLAS_FCT(asa* p1);
void print_PARAM_FCT(asa* p);
void print_ROOT(asa* p);
void print_SI(asa* p);
void print_TQ(asa* p);
void print_RETOURNER(asa* p);
void print_ECRIRE(asa* p);
void print_LIRE(asa* p);
void print_NON(asa* p);


void error_asa(const char * s);

#endif
