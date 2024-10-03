#include <stdio.h>
#define N 5

void affiche(int t[], unsigned n) {

	printf("[");
	if(n > 0){
		printf("%d",t[0]);
		for(int i = 1; i < n; i++) {
			printf(", %d", t[i]);
		}
	}
	

	printf("]");
}

int main() {
	int t[N];

	for(int i = 0; i < N; i++){
		printf("Element %d/%d: ", i+1, N);
		scanf("%d", &t[i]);
	}
	printf("\nTableau saisit: ");
	affiche(t,N);
	printf("\n");
	return 0;
}
