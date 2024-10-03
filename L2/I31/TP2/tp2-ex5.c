#include <stdio.h>

void main(void){
	int som = 0;
	int n;
	int i = 0;
	printf("Saisir un nombre strictement positif.\n");
	scanf("%d",&n);
	if (n<=0){
		printf("Erreur\n");
	}
	else{
		for(i;i<n;i++){
			som += i*i;
		}
	
	printf("Somme des carrés de 1 à %d : %d\n",n,som);
	}



}
