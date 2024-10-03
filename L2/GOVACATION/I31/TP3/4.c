#include <stdio.h>

int puissance(int x, int n) {

	int i = 0;

	int puiss = 1;

	while(i < n) {

		puiss *= x;

		i++;
	}
	return puiss;
}

int main() {

	int x,n;
	printf("Saisir deux entiers x n pour avoir x powered n : ");
	scanf("%d %d", &x, &n);
	printf("%d\n", puissance(x,n));
	return 0;
}
