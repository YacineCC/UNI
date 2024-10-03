#include <stdio.h>

int pgcd(int a, int b) {
	int tmp;
	while(b != 0) {
		
		tmp = b;
		b = a % b;
		a = tmp;
	}
	return a;
}

/* ppcm(a,b) = (a*b) / pgcd(a,b) */

int ppcm(int a, int b) {

	return ((a*b) / pgcd(a,b));
}


int main() {
	
	int a,b;
	printf("Saisir deux nombre pour avoir le ppcm : ");
	scanf("%d %d", &a, &b);	
	printf("%d\n",ppcm(a,b));
	return 0;
}
