#include <stdio.h>

int factorielle(int n) {

	int fact = 1;
	if(n > 0) {

		int i = 0;
		while(i < n) {

			fact *= (n-i);

			i++;
		}
	}

	return fact;
}

int main() {

	int a;
	printf("Saisir un entier pour en avoir sa factorielle : ");
	scanf("%d", &a);
	printf("%d\n", factorielle(a));

	return 0;
}
