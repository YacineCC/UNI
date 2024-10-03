#include <stdio.h>
#include <math.h>

void main(void) {

	int a,b,c;

	printf("Saisir les trois entiers du polynôme : \n");

	scanf("%d %d %d", &a, &b, &c);

	int delta = (b*b) - (4*a*c);

	if(delta < 0) {
		printf("Pas de solutions dans R \n");
	}

	else {

		if(delta == 0){
			float sol;

			sol = -b/(2*a);

			printf("x0 = %f\n",sol);
		}

		else{
			float sol1,sol2,racinedelta;
				
			racinedelta = sqrt(delta);

			sol1 = (-b - racinedelta)/(2*a);

			sol2 = (-b + racinedelta)/(2*a);

			printf("x1 = %f x2 = %f\n",sol1, sol2);
		}
			

	}
}
