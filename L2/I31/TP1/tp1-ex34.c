#include <stdio.h>

void main(void)
{
	char c;
	int i;
	float f;
	printf("Entrer 3 variables séparées par un espace, characère puis entier puis float.\n");
	scanf("%c %d %f", &c,&i,&f);
	printf("Le charactère : %c\nL'entier : %d\nLe flotant : %f\n",c,i,f);
}
