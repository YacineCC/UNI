%{
  #include <stdio.h>
  #include <ctype.h>
  
  extern int yylex();
  void yyerror(char *msg);
  
 %}

%token <nb> NB
%token EOL


%left '+' '-'
%left '*' '/' '%'

%start PROG

%type <nb> EXP

%union{
  int nb;
 }

%%

PROG : EXP EOL PROG{
  printf("= %d\n", $1 );
  printf("> ");
 }
;
EXP : NB      { $$ = $1; } 
| EXP '+' EXP    { $$ = $1 + $3;}
| EXP '-' EXP    { $$ = $1 - $3;}
| EXP '*' EXP    { $$ = $1 * $3;}
| EXP '/' EXP    { $$ = $1 / $3;}
| EXP '%' EXP    { $$ = $1 % $3;}
;
%%

int main( void ) {
  printf("> ");
  yyparse() ;
}

void yyerror(char *msg) {
  printf("\n%s\n", msg);
}
