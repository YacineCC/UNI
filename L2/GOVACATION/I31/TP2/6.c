#include <stdio.h>

int main() {

	float n;
	int cpt = 0;
	float som = 0;
	do{
		printf("Entrer un nombre(<0 pour terminer):\n");
		scanf("%f",&n);
		if(n >= 0){

			som += n;

			cpt++;
		}
	}while(n >= 0);

	printf("La moyenne est de %f\n",som/cpt);

	return 0;
}


