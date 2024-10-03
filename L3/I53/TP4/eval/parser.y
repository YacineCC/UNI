%{
  #include <stdio.h>
  #include <ctype.h>
  
  extern int yylex();
  void yyerror(char *msg);
  
 %}

%token <nb> NB
%token EOL
%token <nb> NB
%token <id> ID
%token <nb> EXP

%right 
%left '+' '-'

%start PROG

%type <nb> EXP

%union{
  int nb;
  char id[32];
 }

 
 


%%

PROG : PROG EXP EOL {
  printf("= %d\n> ", $2 );

  % empty;
 }
;
EXP : NB         { $$ = $1; } 
| EXP '+' EXP    { $$ = $1 + $3;}
| 
;
%%

int main( void ) {
  printf("> ");
  yyparse() ;
}

void yyerror(char *msg) {
  printf("\n%s\n", msg);
}
