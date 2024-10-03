/* Test flex */

/* ______________________________________________________________________________ */
/* Partie déclarations de fonctions, variables globales et includes C */
%{
	
	#include <stdio.h>
	#include <math.h>
%}

/* ______________________________________________________________________________ */





/* ______________________________________________________________________________ */
/* Expressions régulières */
%option noyywrap
nombre [1-9]+[0-9]*
chaine [a-zA-Z]+



/* ______________________________________________________________________________ */











/* ______________________________________________________________________________ */
/* Descriptions (pairs de (Expression, Règles)) Règles : code C */

/* Exemple nombre : patern, printf : action */
%%
{nombre} { printf("%d\n", atoi(yytext));}
{chaine} printf("%s\n", yytext);
. 


%%

/* ______________________________________________________________________________ */




/*Main en C */

int main(int argc, char** argv)
{
	yyin = fopen(argv[1], "r");
	yylex();
}
