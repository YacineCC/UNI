#include <stdio.h>

int factorielle(int n) {

	if(n < 2) {
		return 1;
	}
	return n*factorielle(n-1);
}

int main() {
	printf("Saisir un entier :");
	int n;
	scanf("%d",&n);
	printf("Factorielle de %d = %d\n",n,factorielle(n));
	return 0;
}

