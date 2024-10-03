#include <stdio.h>

unsigned int factorielle(unsigned int n) {

	unsigned int fact = 1;
	if(n > 0) {

		unsigned int i = 0;
		while(i < n) {

			fact *= (n-i);

			i++;
		}
	}

	return fact;
}

unsigned int arrangement(unsigned int n, unsigned int k) {
	return (factorielle(n)/factorielle(n-k));
}

unsigned int combinaison(unsigned int n, unsigned int k) {
	return(arrangement(n,k)/factorielle(k));
}

int puissance(int x, int n) {

	int i = 0;

	int puiss = 1;

	while(i < n) {

		puiss *= x;

		i++;
	}
	return puiss;
}

void affichebinome() {

	unsigned int n;
	printf("Saisir un entier positif n pour afficher le polynome : ");
	scanf("%u", &n);
	printf("1X^%u", n);
	int i = 1;

	while(i <= n) {

		printf(" + %uX^%u", combinaison(n, i), (n-i));
		i++;
	}
}

unsigned int newton(unsigned int x,unsigned int y,unsigned int n) {

	unsigned int i = 0;
	unsigned int binom = 0;
	while(i <= n) {
		binom += (combinaison(n,i)*puissance(x,(n-i))*puissance(y,i));
		i++;
	}
	return binom;
}
int main() {
	unsigned x,y,n;
	printf("Saisir les entiers positifs x,y,n pour avoir (x+y)^n : ");
	scanf("%u %u %u", &x, &y, &n);
	printf("%u\n", newton(x,y,n));
	return 0;
}


