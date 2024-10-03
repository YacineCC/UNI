%{
  /*Prologue*/
  #include <stdio.h>
  #include <string.h>
  
  int longmax=0;
  char motlepluslong[256];
 	int numligne = 1;
	int numcolonne = 0;

 	int numlignemax = 1;
	int numcolonnemax = 0;
	int somme = 0;

%}
%option nounput noinput
/*Définitions*/

NOMBRE [1-9][0-9]*
LETTRE   [a-zA-Z]
MOT      {LETTRE}+
%%

{MOT} { if (yyleng > longmax){
    longmax = yyleng;
	numcolonnemax = numcolonne;
	numlignemax = numligne;
    strcpy(motlepluslong, yytext);
  }
}
{NOMBRE} { somme += atoi(yytext); }
\n     { numligne++; numcolonne = 0;}//ignore les espaces
.      { numcolonne++;} //ignore tous les autres caracteres
%%
int main(int argc, char** argv) {
  yyin = fopen(argv[1], "r");
  yylex();
  printf("Mot le plus long: '%s', de longueur: %d situé à la ligne : %d et la colonne : %d\n", motlepluslong, longmax, numlignemax, numcolonnemax);
	printf("Somme des entier : %d \n", somme);
  return 0;
}
