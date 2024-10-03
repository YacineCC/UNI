%{
  #include "parser.h"
%}
  
%option nounput
%option noinput

NOMBRE [0-9][1-9]*
OPERATEURS [-+*/%]
%%

{OPERATEURS} { return yytext[0]; }
{NOMBRE}  { yylval.nb = atoi(yytext); return NB; }
\n        { return EOL;}
[ \t]     { /* ignorer les blancs */ }
.         { fprintf(stderr, "caractere inconnu %c\n", yytext[0]); }

%%
