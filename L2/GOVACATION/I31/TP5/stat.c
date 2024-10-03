#include <stdio.h>
#include <stdlib.h> // Pour malloc(), free()
#include <math.h> // Pour NAN
int* creation_serie(unsigned int n) {
	
	if(n > 0) {
		return (int*)malloc(n*sizeof(int));
	}
	return NULL;
}

void affiche_serie(int* s, unsigned int n) {
	printf("(");

	if((s != NULL) && (n > 0)) {
		printf("%d", s[0]);
		for(int i = 1; i < n; i++){
			printf(", %d", s[i]);
		}
	}
	printf(")");
}

void destruction_serie(int** ps) {
	if((ps != NULL) && (*ps != NULL)) {
		free(*ps);

		*ps = NULL;
	}
}

float moyenne(int* s, unsigned int n) {
	if ((s != NULL) && (n > 0)) {
		float m = 0;

		for(int i = 0; i < n; i ++) {
			m += s[i];
		}

		return m/n;
	}
	return NAN;
}

float variance(int* s, unsigned int n) {
	float m = moyenne(s, n);

	if(m != NAN) {
		float v = 0;

		for(int i = 0; i < n; i++) {
			v += (s[i] - m)*(s[i] - m);
		}
		return v / n;
	}
	return NAN;

}

int* tri_croissant(int* s, unsigned int n) {

	if((s == NULL) || (n < 1))
			return NULL;
	
	int* r = (int*)malloc(n*sizeof(int));
	for(int i = 0; i < n; i++) {
		r[i] = s[i];
	}

	// Tri selection
	int c;
	for(int i = 0; i < n-1; i++) {
		for(int j = i+1; j < n; j++) {
			if( r[i] > r[j]) {
				c = r[i];
				r[i] = r[j];
				r[j] = c;
			}
		}
	}
	return r;
}

float mediane(int* s, unsigned int n) {
	if((s != NULL ) && (n > 0)) {
		if(n % 2 == 0)
			return s[(n-1)/2];
		else
			return s[n/2];
	}
	return NAN;
}

int main() {
	unsigned int nb_valeurs = 5;
	int* serie = creation_serie(nb_valeurs);
	int* serie_triee = NULL;

	serie[0] = 1;
	serie[1] = 6;
	serie[2] = 2;
	serie[3] = 4;
	serie[4] = 8;
	
	printf("Serie: ");
	affiche_serie(serie, nb_valeurs);
	printf("\n\n");

	printf("Moyenne: %f\n", moyenne(serie, nb_valeurs));
	printf("Variance: %f\n", variance(serie, nb_valeurs));

	serie_triee = tri_croissant(serie, nb_valeurs);

	printf("\nSerie triee: ");
	affiche_serie(serie_triee, nb_valeurs);
	printf("\n");
	printf("Mediane: %f\n", mediane(serie_triee, nb_valeurs));

	destruction_serie(&serie);
	destruction_serie(&serie_triee);
}
