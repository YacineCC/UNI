#include <stdio.h>

int main() {

	int n;
	printf("Entrer un nombre : \n");
	scanf("%d",&n);

	int i = 1;

	while(i*i <= n) {

		i++;
	}

	printf("Le plus petit carré supérieur à %d est %d\n", n, i*i);

	return 0;
}
