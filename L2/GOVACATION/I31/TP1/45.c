#include <stdio.h>

int main() {

	int n;
	printf("Test de parité affiche 0 si pair 1 sinon.\nSaisir un entier.\n");
	scanf("%d",&n);
	
	printf("%d\n",n%2);
	return 0;
}
