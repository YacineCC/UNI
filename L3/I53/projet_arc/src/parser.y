%{
  #include <stdio.h>
  #include <ctype.h>
  #include <string.h>
  
  #include "asa.h"
  #include "semantic.h"
  #include "codegen.h"
  
  extern int yylex();
  static void print_file_error(char * s, char *errmsg);

  table_symb TABLE_SYMBOLES = NULL;
  struct asa * ARBRE_ABSTRAIT = NULL;

  void yyerror(const char * s);

  char srcname[64];
  char exename[64] = "a.out";
  FILE * exefile;
%}

%union{
  int nb;
  struct asa* tree;
  char id[32];
 };

%type <tree> PROGRAMME_ALGO ROOT CORPS_FCT
%type <tree> LISTES_DECLAS DECLA_VARS DECLA_VAR DECLA_FCT
%type <tree>  LISTE_INST  LISTE_INT LISTE_PARAM
%type <tree>  INST  INIT_INT INIT_TAB EXP STATIC_TAB
%type <tree> INST_SI INST_TQ INST_RETOURNER OP_BIN INDICE AFFECTATION NOMBRE IDENTIFICATEUR



%define parse.error verbose
%locations

%token <nb> NB
%token PROGRAMME DEBUT FIN 
%token AFFECT "<-"
%token VAR 
%token ALGO TQ FTQ SI FSI RETOURNER ALORS FAIRE
%token <id> ID

%right AFFECT
%left '+' '-'
%left '*' '/' '%'

%start ROOT

%%

ROOT: LISTES_DECLAS 
PROGRAMME_ALGO {$$ = creer_noeud_ROOT($1, $2);ARBRE_ABSTRAIT = $$;}
;


PROGRAMME_ALGO :
PROGRAMME '(' ')' SEP
DECLA_VAR SEP 
CORPS_FCT {$$ = creer_noeud_DECLA_FCT(creer_feuille_ID("PROGRAMME"), NULL, $7);}
;
/*{ $$ = $5; ARBRE_ABSTRAIT = $5; }*/

LISTES_DECLAS:
/*DECLA_FCT {$$ = creer_noeud_LISTES_DECLAS($1,NULL);}*/
LISTES_DECLAS DECLA_FCT {$$ = creer_noeud_LISTES_DECLAS($1,$2);}
|LISTES_DECLAS DECLA_VARS {$$ = creer_noeud_LISTES_DECLAS($1, $2);}
|%empty {$$ = NULL;}
;

DECLA_FCT: ALGO ID '('LISTE_PARAM')' SEP
DECLA_VARS SEP
CORPS_FCT  {$$ = creer_noeud_DECLA_FCT(creer_feuille_ID($2), $4, $9);}
;

LISTE_PARAM: ID {$$ = creer_noeud_LISTE_PARAM(creer_feuille_ID($1), NULL);}
| LISTE_PARAM ',' ID {$$ = creer_noeud_LISTE_PARAM(creer_feuille_ID($3),$1);}
;

DECLA_VARS : DECLA_VAR {$$ = creer_noeud_DECLA_VARS($1, NULL);}
| DECLA_VARS ',' DECLA_VAR {$$ = creer_noeud_DECLA_VARS($1, $3);}
;
DECLA_VAR : VAR INIT_INT {$$ = creer_noeud_DECLA_VAR($2);}
| VAR INIT_TAB  {$$ = creer_noeud_DECLA_VAR($2);}
|%empty {$$ = NULL;}

;

INIT_INT: ID {$$ = creer_noeud_INIT_INT(NULL, creer_feuille_ID($1));}
|ID AFFECT EXP {$$ = creer_noeud_INIT_INT($3, creer_feuille_ID($1));}  /*{$$ = creer_noeudAFFECTATION(creer_feuille_ID($1), $3);}*/
;

INIT_TAB: '@'ID {$$ = creer_noeud_INIT_TAB(creer_feuille_ID($2), NULL, NULL);}
| ID '['NB']' AFFECT STATIC_TAB {$$ = creer_noeud_INIT_TAB(creer_feuille_ID($1), creer_feuille_NB($3), $6);}
;

STATIC_TAB : '['LISTE_INT']' {$$ = creer_noeud_STATIC_TAB($2);}
;

LISTE_INT: NB {$$ = creer_noeud_LISTE_INT(NULL,creer_feuille_NB($1));}
|LISTE_INT ',' NB {$$ = creer_noeud_LISTE_INT(creer_feuille_NB($3), $1);}/*yylval.nb*/
;

CORPS_FCT:
DEBUT SEP
LISTE_INST SEP
FIN SEP {$$ = creer_noeud_CORPS_FCT($3);}
;

LISTE_INST : INST {$$ = creer_noeud_LISTE_INST(NULL, $1);}  
| LISTE_INST SEP INST   {$$ = creer_noeud_LISTE_INST($1, $3);} 
;

INST: EXP {$$ = creer_noeud_INST($1);}
| INST_SI {$$ = creer_noeud_INST($1);}
| INST_TQ {$$ = creer_noeud_INST($1);}
| INST_RETOURNER {$$ = creer_noeud_INST($1);}
;

INST_SI: SI EXP ALORS LISTE_INST FSI {$$ = creer_noeud_SI($2, $4);};

INST_TQ: TQ EXP FAIRE LISTE_INST FTQ {$$ = creer_noeud_TQ($2, $4);};

INST_RETOURNER: RETOURNER EXP {$$ = creer_noeud_RETOURNER($2);};


EXP: OP_BIN {$$ = creer_noeud_EXP($1);}
| INDICE {$$ = creer_noeud_EXP($1);}
| NOMBRE {$$ = creer_noeud_EXP($1);}
| IDENTIFICATEUR {$$ = creer_noeud_EXP($1);}
/*| TAB {creer_noeud_EXP($1);}*/
;

OP_BIN: EXP '+' EXP            {$$= creer_noeud_OP (creer_feuille_NB('+'), $1, $3);}
| EXP '-' EXP            {$$= creer_noeud_OP (creer_feuille_NB('-'), $1, $3);}
| EXP '*' EXP            {$$= creer_noeud_OP (creer_feuille_NB('*'), $1, $3);}
| EXP '/' EXP            {$$= creer_noeud_OP (creer_feuille_NB('/'), $1, $3);}
| EXP '%' EXP            {$$= creer_noeud_OP (creer_feuille_NB('%'), $1, $3);}
| ID AFFECT AFFECTATION {$$ = creer_noeud_OP(creer_feuille_ID("<-"), creer_feuille_ID($1), ($3));}
;

INDICE: ID '['EXP']' {$$ = NULL;} /*creer_noeud_INDICE($3*/

AFFECTATION : ID AFFECT EXP {$$ = creer_noeud_AFFECTATION(creer_feuille_ID($1), $3);}
;


NOMBRE : NB {$$ = creer_feuille_NB($1);}
;

IDENTIFICATEUR : ID {$$ = creer_feuille_ID($1);}
;



SEP: '\n' | SEP '\n';


%%
/*
ALGO : ID (LIST_ID) : SEP LI;


LIST_ID:
ID	{$$ = creer_noeud_DECLA_VAR($1, NULL, NULL);}
|ID ',' LIST_ID {$$ = creer_noeud_DECLA_VAR($1, NULL, $3);}
|AFFECTATION
|AFFECTATION ',' LIST_ID
;

EXP : NB                 {$$ = creer_feuille_NB($1);}
| ID '['EXP']'           
| EXP '+' EXP            {$$= creer_noeud_OP ('+', $1, $3);}
| EXP '-' EXP            {$$= creer_noeud_OP ('-', $1, $3);}
| EXP '*' EXP            {$$= creer_noeud_OP ('*', $1, $3);}
| EXP '/' EXP            {$$= creer_noeud_OP ('/', $1, $3);}
| EXP '%' EXP            {$$= creer_noeud_OP ('%', $1, $3);}
| '('EXP')'              {$$= $2;}
| ID                     {$$= creer_feuille_ID($1);}
| AFFECTATION

;


DECLA_VAR:
VAR LIST_ID SEP {$$ = $2; print_asa($$);}
| %empty
;


;

*/



int main( int argc, char * argv[] ) {
  extern FILE *yyin;
  
  if (argc > 1){
    strcpy(srcname, argv[1]);
    if ( (yyin = fopen(srcname,"r"))==NULL ){
      char errmsg[256];
      sprintf(errmsg,"fichier \x1b[1m\x1b[33m' %s '\x1b[0m introuvable",srcname);
      print_file_error(argv[0],errmsg);
      exit(1);
    }
  }  else {
    print_file_error(argv[0],"aucun fichier en entree");
    exit(1);
  }
  if (argc == 3){
    strcpy(exename, argv[2]);
  }
 
  
  exefile = fopen(exename,"w");
  TABLE_SYMBOLES = ts_init_table("GLOBAL");
  
  yyparse();
  print_asa(ARBRE_ABSTRAIT);
  semantic(ARBRE_ABSTRAIT);
  print_context(TABLE_SYMBOLES, 1);
  //load 128 store 2
  //fprintf()
  codegen(ARBRE_ABSTRAIT);
  //STOP
  fclose(yyin);
}



static void print_file_error(char * prog, char *errmsg){
  fprintf(stderr,
	  "\x1b[1m%s:\x1b[0m \x1b[31m\x1b[1merreur fatale:\x1b[0m %s\nechec de la compilation\n",
	  prog, errmsg);
}

void yyerror(const char * s)
{
  fprintf(stderr, "\x1b[1m%s:%d:%d:\x1b[0m %s\n", srcname, yylloc.first_line, yylloc.first_column, s);
  exit(0);
}


