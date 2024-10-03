#include <stdio.h>

int main() {

	int n;
	scanf("%d", &n);
	int somcarre = 0;
	if(n > 0) {

		for(int i = 1; i <= n; i++) {

			somcarre += i*i;

		}
	
	printf("La somme des carrés de 1 à %d est = %d\n", n, somcarre);
	}
	else {
		printf("Invalide <= 0");
	}
}
