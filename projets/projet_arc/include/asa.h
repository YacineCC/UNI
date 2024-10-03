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

typedef enum {type_ROOT, type_LISTES_DECLAS, type_DECLA_FCT, type_LISTE_PARAM, type_DECLA_VARS,
type_DECLA_VAR, type_INIT_INT, type_INIT_TAB, type_STATIC_TAB, type_LISTE_INT,type_CORPS_FCT, type_LISTE_INST, type_INST, type_SI,
type_TQ, type_RETOURNER, type_EXP, type_OP, type_AFFECTATION, type_ID, type_NB} type_Noeud;



typedef struct
{
  struct asa* listes_declas;
  struct asa* main;
} noeud_ROOT;

typedef struct 
{
  struct asa* declaration;
  struct asa* declaration_svt; 
} noeud_LISTES_DECLAS;


typedef struct
{
  struct asa* id;
  struct asa* liste_param;
  struct asa* corps_fct;
} noeud_DECLA_FCT;

typedef struct 
{
  struct asa* param;
  struct asa* param_svt;
} noeud_LISTE_PARAM;

typedef struct
{
  struct asa* decla_var;
  struct asa* decla_var_svt;
} noeud_DECLA_VARS;

typedef struct
{
  struct asa* var;
} noeud_DECLA_VAR;

typedef struct 
{
  struct asa* id;
  struct asa* exp;
} noeud_INIT_INT;

typedef struct 
{
  struct asa* id;
  struct asa* taille;
  struct asa* liste_int;
} noeud_INIT_TAB;

typedef struct 
{
  struct asa* liste_int;
} noeud_STATIC_TAB;

typedef struct 
{
  struct asa* nb;
  struct asa* nb_svt;
} noeud_LISTE_INT;

typedef struct 
{
  struct asa* liste_inst;
} noeud_CORPS_FCT;

typedef struct 
{
  struct asa* inst;
  struct asa* inst_svt;
} noeud_LISTE_INST;

typedef struct 
{
  struct asa* inst;
} noeud_INST;

typedef struct 
{
  struct asa* condition;
  struct asa* liste_inst;
} noeud_SI;

typedef struct 
{
  struct asa* condition;
  struct asa* liste_inst;
} noeud_TQ;

typedef struct 
{
  struct asa* exp;
} noeud_RETOURNER;

typedef struct
{
  struct asa* exp;
} noeud_EXP;

typedef struct {
  struct asa* ope;
  struct asa * noeud[2];
} noeud_OP;

typedef struct 
{
  struct asa* id;
  struct asa* exp;
} noeud_AFFECTATION;


typedef struct{
  char nom[32]; 
} feuille_ID;

typedef struct {
  int val;
} feuille_NB;

typedef struct asa{
  type_Noeud type;
  int memadr;
  int codelen;
  union {
    noeud_ROOT root;
    noeud_LISTES_DECLAS listes_declas;
    noeud_DECLA_FCT decla_fct;
    noeud_LISTE_PARAM liste_param;
    noeud_DECLA_VARS decla_vars;
    noeud_DECLA_VAR decla_var;
    noeud_INIT_INT init_int;
    noeud_INIT_TAB init_tab;
    noeud_STATIC_TAB static_tab;
    noeud_LISTE_INT liste_int;
    noeud_CORPS_FCT corps_fct;
    noeud_LISTE_INST liste_inst;
    noeud_INST inst;
    noeud_SI si;
    noeud_TQ tq;
    noeud_RETOURNER retourner;
    noeud_EXP exp;
    noeud_OP op;
    noeud_AFFECTATION affectation;
    feuille_ID id;
    feuille_NB nb;
  };
} asa;


asa* creer_noeud_ROOT(asa* liste_decla, asa* liste);
asa* creer_noeud_LISTES_DECLAS(asa* p1, asa* p2);
asa* creer_noeud_DECLA_FCT(asa* p1, asa* p2, asa* p3);
asa* creer_noeud_LISTE_PARAM(asa* p1, asa* p2);
asa* creer_noeud_DECLA_VARS(asa* p1, asa* p2);
asa* creer_noeud_DECLA_VAR(asa* p1);
asa* creer_noeud_INIT_INT(asa* p1, asa* p2);
asa* creer_noeud_INIT_TAB(asa* p1,asa* p2, asa* p3);
asa* creer_noeud_STATIC_TAB(asa* p1);
asa* creer_noeud_LISTE_INT(asa* p1, asa* p2);
asa* creer_noeud_CORPS_FCT(asa* p1);
asa* creer_noeud_LISTE_INST(asa* p1, asa* p2);
asa* creer_noeud_INST(asa* p1);
asa* creer_noeud_SI(asa* p1, asa* p2);
asa* creer_noeud_TQ(asa* p1, asa* p2);
asa* creer_noeud_RETOURNER(asa* p1);
asa* creer_noeud_EXP(asa* p1);
asa* creer_noeud_OP(asa* ope, asa* p1, asa* p2);
asa* creer_noeud_AFFECTATION(asa* p1, asa* p2);
asa* creer_feuille_ID(char* nom);
asa* creer_feuille_NB(int val);


void free_asa(asa* p);
void print_asa(asa* p);
void print_ROOT(asa* p);
void print_LISTES_DECLAS(asa* p);
void print_DECLA_FCT(asa* p);
void print_LISTE_PARAM(asa* p);
void print_DECLA_VARS(asa* p);
void print_DECLA_VAR(asa* p);
void print_INIT_INT(asa* p);
void print_INIT_TAB(asa* p);
void print_STATIC_TAB(asa* p);
void print_LISTE_INT(asa* p);
void print_CORPS_FCT(asa* p);
void print_LISTE_INST(asa* p);
void print_INST(asa* p);
void print_SI(asa* p);
void print_TQ(asa* p);
void print_RETOURNER(asa* p);
void print_EXP(asa* p);
void print_OP(asa* p);
void print_AFFECTATION(asa* p);
void print_ID(asa* p);
void print_NB(asa* p);


void error_asa(const char * s);

#endif
