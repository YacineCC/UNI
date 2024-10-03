%{
  
  #include <stdio.h>
  #include <ctype.h>
  #include <stdlib.h>
	#include <string.h>
  
  int yylval;
  int yylex();
  int yyerror(char *msg);
	int myexp(int x, int y);
  
  
%}


%token NB PLUS MOINS MUL DIV FIN POW PO PF
%left PLUS MOINS
%left MUL DIV
%right POW


%start PROG

%%

PROG : EXP FIN { printf("%d\n", $1 ); return 1;}
EXP  : NB { $$ = $1 ;} 
| EXP PLUS EXP { $$ = $1 + $3 ;}
| EXP MOINS EXP { $$ = $1 - $3 ;}
| EXP MUL EXP { $$ = $1 * $3 ;}
| EXP DIV EXP { $$ = $1 / $3 ;}
| EXP POW EXP { $$ = myexp($1, $3) ;}
| PO EXP PF { $$ = $2 ;}
;
%%

int main( int argc, char** argv ) {
  yyparse() ;
  return 0;
}

int yylex( ){
  int car;
	do{car = getchar();}
while(car == ' ' || car == '\t');
	
			

	
  if ( car == EOF ) return 0 ;
  if ( isdigit(car) ) {
	char buffer[16];
	buffer[0] = '\0';
	int i = 0;
	while(i < 16 && isdigit(car))
	{
		buffer[i++] = car;
		buffer[i] = '\0';
		car = getchar();
	}
	ungetc(car, stdin);
    yylval = atoi(buffer);
    return NB;
  }

  switch ( car ) {
  case '+' : return PLUS; break;
	case '-' : return MOINS; break;
	case '*' : { car = getchar();
				if (car == '*') return POW;
					
				else 
				{
					ungetc(car, stdin);
					return MUL;
				}
				break;
				}
	case '(' : return PO; break;
	case ')' : return PF; break;
	case '/' : return DIV; break;
  case '\n': return FIN; break;
  }
  return -1;
}
	int myexp(int x, int y)
	{
		int res = 1;
		for(int i = 0; i < y; i++)
		{
			res = res * x;
		}
		return res;
	}
	
 
int yyerror(char *msg) {
  printf("\n%s\n", msg);
  return 1;
}
