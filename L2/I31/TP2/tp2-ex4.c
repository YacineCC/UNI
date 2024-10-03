#include <stdio.h>

void main(void){
	int i = 0;
	int a;
	scanf("%d",&a);
	int b = a;
	do{
	       a = a / 10;
	       i ++;
	} while(a>0);

	printf("L'entier %d est composé de %d chiffres.\n",b,i);

}
