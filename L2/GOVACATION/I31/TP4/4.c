#include <stdio.h>
#define N 5

void affiche(int t[], unsigned n) {

	printf("[");
	if(n > 0){
		printf("%d ",t[0]);
		for(int i = 1; i < n; i++) {
			printf(", %d", t[i]);
		}
	}
	printf("]");
}

void inverse(int t[], unsigned n) {

	if(n > 1) { // On inverse qu'a partir de 2 elements

		int tmp;

		for(int i = 0; i < n/2; i++) {
			tmp = t[i];
			t[i] = t[n-i-1];
			t[n-i-1] = tmp;
		}
	}
}

int main() {
	int t[N];
	
	for(int i = 0; i < N; i++) {
		printf("Element %d/%d: ", i+1, N);
		scanf("%d", &t[i]);
	}
	printf("\nTableau original: ");
	affiche(t, N);
	inverse(t, N);
	printf("\nTableau inverse: ");
	affiche(t, N);
}
