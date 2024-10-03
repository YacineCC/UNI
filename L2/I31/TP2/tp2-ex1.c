#include <stdio.h>

void main(void){
	
	int a,b;

	char op;
	
	printf("Entrer une opération : \n");
	scanf("%d %c %d",&a,&op,&b);

	switch(op){

		case '+':
			printf("Le résultat de %d + %d est %d\n",a,b,a+b);
			break;
		case '-':
			printf("Le résultat de %d - %d est %d\n",a,b,a-b);
			break;
		case '*':
			printf("Le résultat de %d * %d est %d\n",a,b,a*b);
			break;

		case '/':
			printf("Le résultat de %d / %d est %d\n",a,b,a/b);
			break;
	
		case '%':
			printf("Le résultat de %d %% %d est %d\n",a,b,a%b);
			break;
		default:
			printf("Erreur syntaxe.\n");


	}
}
