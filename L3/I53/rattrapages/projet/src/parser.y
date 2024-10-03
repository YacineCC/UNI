%{
  #include <stdio.h>
  #include <ctype.h>
  #include <string.h>
  
  
  #include "asa.h"
  #include "semantic.h"
  #include "codegen.h"
  extern int yylex_destroy();
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

%define parse.error verbose
%locations
 
%type <tree> PROGRAMME_ALGO EXP INST INSTS DECLAS_VARS DECLA_VARS FCT PARAM_FCT ROOT DECLAS_FCT INST_SI INST_TQ INST_RETOURNER INST_ECRIRE INST_LIRE 
%token <nb> NB
%token <id> ID
%token AFFECT VAR PROGRAMME DEBUT FIN ALGO SI TQ RETOURNER ALORS FSI FAIRE FTQ ECRIRE LIRE SINON

%right AFFECT
%left OU
%left ET
%left '=' DIFF
%left '<' '>' SUPEGAL INFEGAL 
%left '+' '-'
%left '*' '/' '%'
%right NON

%start ROOT

%%

ROOT: DECLAS_VARS DECLAS_FCT
PROGRAMME_ALGO {$$ = creer_noeud_ROOT($1,$2, $3);ARBRE_ABSTRAIT = $$;}
;



DECLAS_FCT : FCT SEP DECLAS_FCT {$$ = creer_noeud_DECLAS_FCT($1, $3);}
|%empty {$$ = NULL;}

FCT : ALGO ID '('PARAM_FCT')' SEP DECLAS_VARS DEBUT SEP INSTS FIN  {$$ = creer_noeud_FCT($2,$4,$7,$10);}

PARAM_FCT : ID {$$ = creer_noeud_PARAM_FCT($1, NULL);}
|ID ',' PARAM_FCT {$$ = creer_noeud_PARAM_FCT($1, $3);}
|%empty {$$ = NULL;}
; 

PROGRAMME_ALGO :
PROGRAMME'('')' SEP
DECLAS_VARS 
DEBUT SEP
INSTS 
FIN {$$ = creer_noeud_FCT("PROGRAMME", NULL, $5, $8);}
;


DECLAS_VARS : VAR DECLA_VARS SEP DECLAS_VARS {$$ = creer_noeud_DECLAS_VARS($2,$4);}
| %empty {$$ = NULL;} 
;

DECLA_VARS: ID {$$ = creer_noeud_DECLA_VARS($1, NULL, NULL);}
| ID ',' DECLA_VARS {$$ = creer_noeud_DECLA_VARS($1, NULL,$3);}
| ID AFFECT EXP {$$ = creer_noeud_DECLA_VARS($1, $3, NULL);}
| ID AFFECT EXP ',' DECLA_VARS {$$ = creer_noeud_DECLA_VARS($1, $3, $5);}




INSTS: INST SEP INSTS {$$ = creer_noeud_INSTS($1, $3);}
|%empty {$$ = NULL;}
;


INST : EXP
|INST_SI
|INST_TQ
|INST_RETOURNER
|INST_ECRIRE
;

INST_SI : SI EXP ALORS SEP INSTS FSI{$$ = creer_noeud_SI($2, $5, NULL);}
|SI EXP ALORS SEP INSTS SINON SEP INSTS FSI {$$ = creer_noeud_SI($2, $5, $8);}
;
INST_TQ : TQ EXP FAIRE SEP INSTS FTQ {$$ = creer_noeud_TQ($2, $5);};
INST_RETOURNER : RETOURNER EXP  {$$ = creer_noeud_RETOURNER($2);};

INST_ECRIRE: ECRIRE '('EXP')' {$$ = creer_noeud_ECRIRE($3);};
INST_LIRE: LIRE '('')' {$$ = creer_noeud_LIRE();};


;
EXP : NB                 {$$ = creer_feuilleNB($1);}
| EXP '+' EXP            {$$ = creer_noeudOP('+', $1, $3);}
| EXP '-' EXP            {$$ = creer_noeudOP('-', $1, $3);}
| EXP '*' EXP            {$$ = creer_noeudOP('*', $1, $3);}
| EXP '/' EXP            {$$ = creer_noeudOP('/', $1, $3);}
| EXP '%' EXP            {$$ = creer_noeudOP('%', $1, $3);}
| EXP '<' EXP            {$$ = creer_noeudOP('<', $1, $3);}
| EXP '>' EXP            {$$ = creer_noeudOP('>', $1, $3);}
| EXP '=' EXP            {$$ = creer_noeudOP('=', $1, $3);}
| EXP SUPEGAL EXP        {$$ = creer_noeudOP('s', $1, $3);}
| EXP INFEGAL EXP        {$$ = creer_noeudOP('i', $1, $3);}
| EXP DIFF EXP           {$$ = creer_noeudOP('d', $1, $3);}
| EXP ET EXP             {$$ = creer_noeudOP('e', $1, $3);}
| EXP OU EXP             {$$ = creer_noeudOP('o', $1, $3);}
| NON EXP                {$$ = creer_noeud_NON($2);}
| '('EXP')'              {$$ = $2;}
| ID                     {$$ = creer_feuille_ID($1);}
|INST_LIRE
|ID AFFECT EXP           {$$ = creer_noeud_AFFECTATION($1,$3);}
;

SEP : '\n' | SEP '\n' 

;

%%

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
  
  semantic(ARBRE_ABSTRAIT);
  print_asa(ARBRE_ABSTRAIT);

  ts_print(TABLE_SYMBOLES);
  codegen(ARBRE_ABSTRAIT);


  fclose(yyin);
  fclose(exefile);
  free_asa(ARBRE_ABSTRAIT);
  ts_free_table(TABLE_SYMBOLES);
  yylex_destroy();
  
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
