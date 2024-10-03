#include <stdio.h>
#define N 5

int somme(int t[], unsigned n) {
	int som = 0;
	for(int i = 0; i < n; i++) {

		som += t[i];
	}
	return som;
}

int main() {

	int t[N];
	for(int i = 0; i < N; i++){
		printf("Element %d/%d : ", i+1, N);
		scanf("%d",&t[i]);
	}
	printf("La somme des elements saisis : %d",somme(t,N));
	printf("\n");
	return 0;
}


