#include <stdio.h>

void croissant(int* a, int* b) {

	if(*a > *b) {
		int tmp = *a;
		*a = *b;
	       	*b = tmp;
	}
}

int main() {
	int a,b;
	printf("Saisir deux entiers a et b ce qui sortira sera croissant : ");
	scanf("%d %d", &a, &b);

	printf("a = %d b = %d \n", a, b);
	croissant(&a, &b);

	printf("a = %d b = %d \n", a, b);
	return 0;
}
