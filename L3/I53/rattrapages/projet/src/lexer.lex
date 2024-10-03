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


IDENTIFICATEUR [a-zA-Z_][a-zA-Z0-9_]*
CHIFFRE  [0-9]
NOMBRE   [0-9]+

%%

"<-"            {return AFFECT;}
"VAR"           {return VAR;}
"DEBUT"         {return DEBUT;}
"FIN"           {return FIN;}
"PROGRAMME"     {return PROGRAMME;}
"ALGO"          {return ALGO;}
"SI"            {return SI;}
"TQ"            {return TQ;}
"RETOURNER"     {return RETOURNER;}
"ALORS"         {return ALORS;}
"FSI"           {return FSI;}
"FAIRE"         {return FAIRE;}
"FTQ"           {return FTQ;}
"ECRIRE"        {return ECRIRE;}
"LIRE"          {return LIRE;}
">="            {return SUPEGAL;}
"<="            {return INFEGAL;}
"!="            {return DIFF;}
"ET"            {return ET;}
"OU"            {return OU;}
"NON"           {return NON;}
"SINON"         {return SINON;}


{NOMBRE}        {  yylval.nb = atoi(yytext); return NB; }
{IDENTIFICATEUR} {strcpy(yylval.id, yytext); return ID;}
[-*+/=%\n(),<>]      {return *yytext;}

[\t ]           { /* ignorer les blancs */ }
#[^\n]*             {/* commentaires */}

.         {           
	    sprintf(errmsg,charerr, yytext[0]);
            yyerror(errmsg);
            return 1;
          }

%%
 
