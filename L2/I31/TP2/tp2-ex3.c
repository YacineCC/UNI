#include <stdio.h>

void main(void){
	
	int a;
	int i = 0;	
	printf("Entrer un nombre : \n");

	scanf("%d",&a);
	
	while (i*i <= a){
		i++;
	}

	printf("Le plus petit carre supérieur à %d est %d.\n",a,i*i);

}
