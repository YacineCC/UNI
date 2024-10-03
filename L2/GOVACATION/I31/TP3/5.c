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

int main() {

	unsigned int n,k;
	printf("Saisir deux entiers positifs k n pour avoir le nombre k parmi n : ");
	scanf("%u %u", &k, &n);
	printf("%u\n", arrangement(n,k));
	return 0;
}


