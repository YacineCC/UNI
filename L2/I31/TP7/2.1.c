#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
  unsigned short numero;
  char* voie;
  unsigned int code;
  char* ville;
  
} Adresse;


typedef struct {
    char* nom;
    char* prenom;
    unsigned short age;
    Adresse* adresse;
} Personne;

Adresse* lireAdresse(){
    Adresse* a = (Adresse*)malloc(sizeof(Adresse));
    a->voie = (char*) malloc(255*sizeof(char));
    a->ville = (char*) malloc(255*sizeof(char));
    
    printf("Saisir une adresse (numero rue code ville): ");
    
    scanf("%hd %s %d %s", &(a->numero), a->voie, &(a->code), a->ville);
    
    return a;
}

Personne* lirePersonne(void) {
    Personne* p = (Personne*)malloc(sizeof(Personne));
    p->nom = (char*) malloc(255*sizeof(char));
    p->prenom = (char*) malloc(255*sizeof(char));
    
    printf("Saisir une personne (nom prenom age): ");
    
    scanf("%s %s %hd", p->nom, p->prenom, &(p->age));
    
    p->adresse = lireAdresse();
    
    return p;
}
void ecrireAdresse(Adresse* a) {
    if (a != NULL)
      printf("%hd %s %d %s", a->numero, a->voie, a->code, a->ville);
    else
      printf("Pas d'adresse connue.");
}

void ecrirePersonne(Personne* p) {
    if (p != NULL){
        printf("%s, %s - %hd\n", p->nom, p->prenom, p->age);
        ecrireAdresse(p->adresse);
    } else {
        printf("Personne inconnue.");
    }
}
int memeAdresse(Personne* a, Personne* b) {
    if ((a == NULL) || (b == NULL))
      return 0;

    if ((a->adresse == NULL) || (b->adresse == NULL))
      return 0;

    if (a->adresse->numero != b->adresse->numero)
      return 0;

    if (a->adresse->code != b->adresse->code)
      return 0;

    if (strcmp(a->adresse->voie, b->adresse->voie) != 0)
      return 0;

    if (strcmp(a->adresse->ville, b->adresse->ville) != 0)
      return 0;

    return 1;
}
/*int main()
{
    Personne* p1 = lirePersonne();
    ecrirePersonne(p1);
    printf("\n");

    Personne* p2 = lirePersonne();
    ecrirePersonne(p2);
    printf("\n");

    if (memeAdresse(p1, p2))
      printf("Meme adresse.\n");
    else
      printf("Adresse differente.\n");

    return 0;
}*/
typedef struct Voisin Voisin;

struct Voisin{

	Personne* pers;
	Voisin* precedent;
	Voisin* suivant;
};

typedef Voisin* liste;

typedef struct {
	Voisin* first;
	Voisin* last;
} Rue;

Rue* population(void) {

	Rue* r = (Rue*) malloc(sizeof(Rue));

	r -> first = NULL;
	r -> last = NULL;
	Personne* test = lirePersonne();
	r -> first -> pers = test;
	r -> last -> pers = test;
	r -> last -> suivant = NULL;
	char flag = 'Y';

	while(flag == 'Y') {
		Voisin* v = (Voisin*)malloc(sizeof(Voisin));
		
		v -> pers = lirePersonne();
		r -> first -> precedent = v;
		r -> first -> pers = v;
		r -> first -> precedent = NULL;




		printf("Continuer ? (Y/N)\n");
		getchar();
		scanf("%c", &flag);
	}

}
int main() {
	Rue* r = NULL;
	r = population();
	return 0;
}
