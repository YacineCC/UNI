#include <stdio.h>

void main(void)
{
	const float PI = 3.141592653589793;
	float r;

	printf("Saisir un rayon : ");

	scanf("%f",&r);

	printf("\nLe périmètre du cercle de rayon %f : %f\n",r,2*PI*r);

	printf("L'aire du cercle de rayon %f : %f\n",r,PI*(r*r));
}
