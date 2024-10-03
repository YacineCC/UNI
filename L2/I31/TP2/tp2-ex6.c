#include <stdio.h>

void main(void){
	
	int n = 0;
	int som = 0;
	int cpt = 0;
	
	while(n >= 0){
		printf("Entrer un nombre (<0 pour terminer) :\n");
		scanf("%d",&n);
		if (n >= 0){
		som += n;
		cpt++;
		}
	}

	printf("La moyenne est de %d\n", som/cpt);

			
}
