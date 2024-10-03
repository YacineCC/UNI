#include <stdio.h>

int main() {

	int n;

	scanf("%d", &n);
	int nb = 0;
	int k = n;
	do{
		k = k / 10;
		nb++;
	}while(k >= 1);

	printf("%d est composé de %d chiffres.\n", n, nb);

	return 0;

}
