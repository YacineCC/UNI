#include <stdio.h>

void main(void)
{
	float x1,y1,x2,y2;
	printf("Entrer les coordonées (x,y) du vecteur V1 : ");
	scanf("%f %f", &x1,&y1);
	printf("Entrer les coordonées (x,y) du vecteur V1 : ");
	scanf("%f %f", &x2,&y2);

	float scal = (x1*x2) + (y1*y2);

	printf("produit scalaire de V1(%f,%f) et V2(%f,%f) : %f\n",x1,y1,x2,y2,scal);
	



}
