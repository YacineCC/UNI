#include <stdio.h>
#include <math.h>

int main() {

	float a,b,c;

	printf("Saisir les coefficients a, b, c du trinôme : ");

	scanf("%f %f %f", &a, &b, &c);
	printf("L'équation : %fx² + %fx + %f\n", a, b, c);

	float delta = (b*b) - (4*a*c);
	printf("Delta = %f\n", delta);
	if(delta < 0) {
		printf("Pas de solutions réeles.\n");
	}
	else if(delta > 0) {

		float x1,x2;

		x1 = (-b-sqrt(delta))/(2*a);
		x2 = (-b+sqrt(delta))/(2*a);

		printf("Les solutions de l'équation sont x1 = %f x2 = %f \n", x1, x2);
	}
	else {
		float x0;

		x0 = -b/(2*a);

		printf("L'unique solution de l'équation est x0 = %f \n", x0);
	}

	return 0;
}
