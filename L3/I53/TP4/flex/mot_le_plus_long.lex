%{
  /*Prologue*/
  #include <stdio.h>
  #include <string.h>
  
  extern FILE* yyin;
  int ligne=1; int col=1; int lignemax=1; int colmax=1;
  long long somme = 0;
  int longmax=0;
  char motlepluslong[256];

%}
%option nounput noinput
/*Définitions*/

LETTRE   [a-zA-Z]
MOT      {LETTRE}+
NOMBRE   [0-9]+  
%%  

{MOT} { if (yyleng > longmax){
    longmax = yyleng;
    strcpy(motlepluslong, yytext);
    lignemax = ligne;
    colmax = col;
    col += yyleng;
  }
}
{NOMBRE} {somme+=atoll(yytext);}
\n {ligne++; col=1;}      //ignore les espaces
.  {col++;}     //ignore tous les autres caracteres
%%
int main(int argc, char** argv) {
  yyin = fopen(argv[1], "r");
  yylex();
  printf("Mot le plus long: '%s', de longueur: %d ligne : %d colonne : %d\n", motlepluslong, longmax, lignemax, colmax);
  printf("Somme des entiers : %lld\n", somme);
  
  return 0;
}
