#include <stdio.h>
#include <stdlib.h> // Pour malloc(), free()
#include <math.h> // Pour NAN


typedef struct{

	int* valeurs;
	unsigned int taille;
}serie;


serie creation_serie(unsigned int n) {
	
	serie s;

	if(n > 0){
		s.valeurs = (int*)malloc(n*sizeof(int));
		s.taille = n;
	}else {
		s.valeurs = NULL;
		s.taille = 0;
	}

	return s;
}

void affiche_serie(serie s){
	printf("( ");

	if((s.valeurs != NULL) && (s.taille > 0)){
		printf("%d", s.valeurs[0]);
		for(int i = 1; i < s.taille; i++) {
			printf(", %d", s.valeurs[i]);
		}
	}
	printf(" )");
}

void destruction_serie(serie* ps) {
	if((ps != NULL) && (ps -> valeurs != NULL)){
		free(ps -> valeurs);
		ps -> valeurs = NULL;
		ps -> taille = 0;
	}
}

float moyenne(serie s) {
	if((s.valeurs != NULL) && (s.taille > 0)){
		float m = 0;

		for(int i = 0; i < s.taille; i++) {
			m += s.valeurs[i];
		}
		return m / s.taille;
	}
	return NAN;
}

float variance(serie s) {

	float m = moyenne(s);

	if(m != NAN){

		float v = 0;

		for(int i = 0; i < s.taille; i++){
			v += (s.valeurs[i] - m) *(s.valeurs[i] - m);
		}
		return v/s.taille;
	}

	return NAN;
}

serie tri_croissant(serie s) {

	serie r = creation_serie(s.taille);

	for(int i = 0; i < s.taille; i++){
		r.valeurs[i] = s.valeurs[i];
	}

	//Tri selection
	
	int c;

	for(int i = 0; i < s.taille  - 1;i++){
		for(int j = i+1; j < s.taille; j++){
			if(r.valeurs[i] > r.valeurs[j]) {
				c = r.valeurs[i];
				r.valeurs[i] = r.valeurs[j];
				r.valeurs[j] = c;
			}
		}
	}
	return r;
}


float mediane(serie s){

	if((s.valeurs != NULL) && (s.taille > 0)) {

		if(s.taille % 2 == 0)
			return s.valeurs[(s.taille-1) / 2];
		else
			return s.valeurs[s.taille / 2];
	}
	return NAN;
}


int main(){
	
	unsigned int nb_valeurs = 5;
	serie s = creation_serie(5);

	serie serie_triee;

	s.valeurs[0] = 1;
	s.valeurs[1] = 6;
	s.valeurs[2] = 2;
	s.valeurs[3] = 4;
	s.valeurs[4] = 8;


	printf("Serie: ");
	affiche_serie(s);
	printf("\n\n");
	
	printf("Moyenne : %f\n", moyenne(s));
	printf("Variance: %f\n", variance(s));

	serie_triee = tri_croissant(s);

	printf("\nSerie triee: ");
	affiche_serie(serie_triee);
	printf("\n");

	printf("Mediane: %f\n",mediane(serie_triee));
	
	destruction_serie(&s);
	destruction_serie(&serie_triee);
	return 0;


}
