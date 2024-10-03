#include <stdio.h>

int main() {
	
	float x1,y1,x2,y2;

	printf("Saisir les coordonées du vecteur 1\n");
	scanf("%f %f",&x1,&y1);

	printf("Saisir les coordonées du vecteur 2\n");
	scanf("%f %f",&x2,&y2);
	
	printf("Le produit scalaire : %f \n",x1*x2 + y1*y2);

	return 0;	
	

}
