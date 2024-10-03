%{
  #include <string.h>
  #include "parser.h"

  extern void yyerror(char *);

  char errmsg[256]="";
  const char charerr[] = "\x1b[1m\x1b[31m[erreur lexicale]\x1b[0m caractère \x1b[41m%c\x1b[0m inattendu";
  
  /* MACRO défini 
   * Action executee avant chaque action semantique (meme vide)  
   * et rempli la variable Bison `yylloc` avec la position du token
   */
#define YY_USER_ACTION                                             \
  yylloc.first_line = yylloc.last_line;                            \
  yylloc.first_column = yylloc.last_column;                        \
  if (yylloc.last_line == yylineno)                                \
    yylloc.last_column += yyleng;                                  \
  else {                                                           \
    yylloc.last_line = yylineno;                                   \
    yylloc.last_column = 1;					   \
  }



%}
  
%option nounput
%option noinput
%option yylineno

CHIFFRE  [0-9]
NOMBRE   [1-9][0-9]*
IDENT [a-zA-Z]+
%%

{NOMBRE}        {  yylval.nb = atoi(yytext); return NB; }
{CHIFFRE}        {  yylval.nb = atoi(yytext); return NB; }
"PROGRAMME" {return PROGRAMME;}
"DEBUT" {return DEBUT;}
"FIN" {return FIN;}
"VAR" {return VAR;}
{IDENT} {strcpy(yylval.id, yytext); return ID;}
"<-" {return AFFECT;}

[-*+/=%\n(),]      {return *yytext;}
[ \t]           { /* ignorer les blancs */ }

.         {           
	    sprintf(errmsg,charerr, yytext[0]);
            yyerror(errmsg);
            return 1;
          }

%%
 
