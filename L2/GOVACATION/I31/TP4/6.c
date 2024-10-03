/* Le tri bulle parcourt le tableau en comparant 2 cases successives. Lorsqu'il trouve qu elles ne sont pas dans l ordre souhaite, il permute ces 2 cases. A la fin d un parcourt complet on aura le deplacement du minimum au debut du tableau. En repetant cet operation N fois, le tableau resultant est trie. */

#include <stdio.h>
#define N 5

void affiche(int t[], unsigned n) {

	printf("[");
	if(n > 0) {
		printf("%d", t[0]);

		for(int i = 1; i < n; i++) {
			printf(", %d", t[i]);
		}
	}
	printf("]\n");
}

void tri_bulle(int t[], unsigned n) {
	if(n > 1) { // On ne trie qu'a partir de 2 elements
		int i,j,c;

		for(i = 1; i <= n; i++) { // Parcours du tableau de 1 a n
			for(j = 0; j<n-1; j++) { // Parcours du tableau de 0 a n
				if(t[j] > t[j+1]) {
					c = t[j];
				
					t[j] = t[j+1]; 
					t[j+1] = c;
				}
			}
		
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
	tri_bulle(t, N);
	printf("\nTableau trie: ");
	affiche(t, N);
	return 0;
}
