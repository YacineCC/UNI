%{
  #include "parser.h"
%}
  
%option nounput
%option noinput

NOMBRE [0-9]+
IDENT [a-z]+


%%

[+]       { return yytext[0]; }
{NOMBRE}  { yylval.nb = atoi(yytext); return NB; }
{IDENT} {strcpy(yylval.id, yytext); return ID;}
\n        { return EOL;}
[ \t]     { /* ignorer les blancs */ }
.         { fprintf(stderr, "caractere inconnu %c\n", yytext[0]); }

%%
