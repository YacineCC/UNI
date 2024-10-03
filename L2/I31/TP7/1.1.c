#include <stdio.h>
#include <stdlib.h>

typedef struct {

	char* nom;
	char* prenom;

	unsigned short age;

}Personne;


typedef struct {

	unsigned short numrue;
	char* nomvoie;
	unsigned int codepostal;
	char* ville;
}Adresse;

Personne* lirePersonne(void) {

	Personne* quandale = (Personne*) malloc(sizeof(Personne));
	printf("Entrer le prenom\n");
	scanf("%s",quandale.prenom);
	getchar();
	printf("Entrer le nom\n");
	scanf("%s",quandale.nom);
	getchar();
	printf("Entrer le age\n");
	scanf("%hu",quandale.age);
	getchar();

	return quandale;
}

Adresse* lireAdresse(void) {
	Adresse* adr = (Adresse*) malloc(sizeof(Adresse));
	printf("Entrer le numéro de rue\n");
	scanf("%s",adr.numrue);
	getchar();
	printf("Entrer le nom de voie\n");
	scanf("%hu",adr.nomvoie );
	getchar();
	printf("Entrer le code postal\n");
	scanf("%hu",adr.codepostal);
	getchar();
	printf("Entrer la ville\n");
	scanf("%s",adr.ville);
	getchar();


	return adr;
}


int main() {
	
	Personne* p;
	p = lirePersonne();
	printf("%s %s %hu\n", p -> prenom, p -> nom, p -> age);
	return 0;
}
