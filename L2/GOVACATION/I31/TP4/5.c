/* Le tri selection consiste a trouver le minimum du tableau et le positionner ala premiere case. UNe fois cette operation realisee, elle est repetee pour le reste du tableau en positionnant le nouveau minimum a la deuxieme case et ainsi de suite */

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

void tri_selection(int t[], unsigned n) {
	if(n > 1) { // On ne trie qu'a partir de 2 elements
		int i,j,c;

		for(i = 0; i < n-1; i++) { // Parcours du tableau de 0 a n
			for(j = i+1; j<n; j++) { // Parcours du tableau de i+1 a n
				if(t[i] > t[j]) {
					c = t[i];
				}
				t[i] = t[j]; // Affectation du minimum a t[i]
				t[j] = c;
				
			} // Apres cette iteration, t[i] contient obligatoirement le minimum
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
	tri_selection(t, N);
	printf("\nTableau trie: ");
	affiche(t, N);
	return 0;
}
