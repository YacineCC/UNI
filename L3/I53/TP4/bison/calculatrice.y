%{
  
  #include <stdio.h>
  #include <ctype.h>
  #include <stdlib.h>
  #include <string.h>
  int yylval;
  int yylex();
  int yyerror(char *msg);
  int myexp(int x, int n);
  
  
%}


%token NB PLUS FIN MOINS MULT DIV POW PO PF
%left PLUS MOINS
%left MULT DIV
%right POW


%start PROG


%%

PROG : EXP FIN { printf("%d\n", $1 ); return 1;}
EXP  : NB { $$ = $1 ;} 
| EXP PLUS EXP { $$ = $1 + $3 ;}
| EXP MOINS EXP {$$ = $1 - $3;}
| EXP MULT EXP {$$ = $1 * $3;}
| EXP DIV EXP {$$ = $1 / $3;}
| EXP POW EXP {$$ = myexp($1,$3);}
| PO POW PF {$$ = $2;}

;
%%

int main( void ) {
  yyparse() ;
  return 0;
}

int yylex( ){
  int car;
  
  do{car = getchar();

  }while(car == ' ' || car == '\t');

  if ( car == EOF ) return 0 ;
  if ( isdigit(car) ) {
    char nb[16];
    nb[0] = '\0';
    char buff[2];
    buff[1] = '\0';
    while(isdigit(car))
    {
      buff[0] = car;
      strcat(nb, buff);
      
      car = getchar();
    }
    ungetc(car, stdin);
    yylval = atoi(nb);
    
    return NB;
  }
  switch ( car ) {
  case '+' : return PLUS;
  case '\n': return FIN;
  case '*' :
    car = getchar();
    if(car == '*') return POW;
    else
    {
      ungetc(car,stdin);
      return MULT;
    }

    return MULT;
  case '/' : return DIV;
  case '-' : return MOINS;
  case '(' : return PO;
  case ')' : return PF;

 
  }
  return -1;
}

int myexp(int x, int n)
{
  int res = 1;
  for(int i = 0; i < n; i++)
  {
    res = res * x;
  }
  return res;
}

int yyerror(char *msg) {
  printf("\n%s\n", msg);
  return 1;
}
