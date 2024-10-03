#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct{

		int* valeurs;
		unsigned int taille;
}serie;

typedef struct{

		serie* classes;

		unsigned int nb_classes;
}ecole;

serie creation_serie(unsigned int n) {
		serie s;

		if(n > 0){
				s.valeurs = (int*)malloc(n*sizeof(int));
				s.taille = n;
		}else{
				s.valeurs = NULL;
				s.taille = 0;
		}
		return s;
}

void affiche_serie(serie s){

		printf("(");

		if((s.valeurs != NULL) && (s.taille > 0)){
				printf("%d", s.valeurs[0]);
				for(int i = 1; i < s.taille; i++){
						printf(", %d", s.valeurs[i]);
				}
		}

		printf(")");
}


void destruction_serie(serie* ps){
		if((ps != NULL) && (ps -> valeurs != NULL)) {
				free(ps -> valeurs);
				ps -> valeurs = NULL;
				ps -> taille = 0;
		}
}

float moyenne(serie s) {
		if((s.valeurs != NULL) && (s.taille > 0)) {
				float m = 0;

				for(int i = 0; i < s.taille; i++){
						m += s.valeurs[i];
				}
				return m / s.taille;
		}
		return NAN;
}

float variance(serie s){

		float m = moyenne(s);

		if(m != NAN){

				float v = 0;
				for(int i = 0; i < s.taille; i++){
						v += (s.valeurs[i] - m) * (s.valeurs[i] - m);
				}

				return v / s.taille;
		}
		return NAN;
}

serie tri_croissant(serie s) {
		serie r = creation_serie(s.taille);
		for(int i = 0; i < s.taille; i++){
				r.valeurs[i] = s.valeurs[i];
		}
		// Tri selection
		int c;

		for(int i = 0; i < s.taille - 1; i++){
				for(int j = i+1; j < s.taille; j++){
						if(r.valeurs[i] > r.valeurs[j]){
								c = r.valeurs[j];
						}
						r.valeurs[j] = r.valeurs[i];
						r.valeurs[i] = c;
				}
		}
		return r;
}

float mediane(serie s) {
		if((s.valeurs != NULL) && (s.taille > 0)){

				if(s.taille % 2)
						return (s.valeurs[(s.taille-1)/2]);
				else
						return(s.valeurs[s.taille/2]);
		}

		return NAN;
}


ecole creation_ecole(unsigned int m){
		ecole e;

		if(m > 0){
				e.classes = (serie*)malloc(m*sizeof(serie));
				e.nb_classes = m;
		} else{
				e.classes = NULL;
				e.nb_classes = 0;
		}
		return e;
}

void saisie_ecole(ecole e){
		int tmp;

		for(int i = 0; i <  e.nb_classes; i++) {
				printf("Nombre d'eleves de la classe %d: ", i+1);
				scanf("%d", &tmp);

				e.classes[i] = creation_serie(tmp);

				for(int j = 0; j < e.classes[i].taille; j++){
						printf("  Eleves %d/%d: ",j+1, e.classes[i].taille);
						scanf("%d", &(e.classes[i].valeurs[j]));
				}
		}
}

void affiche_ecole(ecole e) {
		for(int i = 0; i < e.nb_classes; i++) {
				printf("Classe %d: ", i);
				affiche_serie(e.classes[i]);
				printf("\n");
		}
}

void destruction_ecole(ecole* pe){

		if(pe != NULL) {
				for(int i = 0; i < pe -> nb_classes; i++) {
						destruction_serie(&(pe -> classes[i]));
				}

				free(pe -> classes);
				pe -> classes = NULL;

				pe -> nb_classes = 0;
		}

}


void main(void){

		unsigned int nb_classes;

		ecole e;

		printf("Nombre de classes dans l'ecole: ");
		scanf("%d", &nb_classes);

		e = creation_ecole(nb_classes);
		saisie_ecole(e);

		printf("\n\n");
		affiche_ecole(e);

		destruction_ecole(&e);
}
