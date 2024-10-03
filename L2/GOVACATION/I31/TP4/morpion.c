#include <stdio.h>

void affiche(char plateau[][3]) {
	int i = 0; int j = 0;

	while(i < 3) {
		j = 0;
		printf("[ ");
		while(j < 3) {
			printf("%c ",plateau[i][j]);
			j++;
		}
		printf("]");
		i++;
		printf("\n");
	}
}
		
char case_valide(int ligne, int colonne, char plateau[][3]) {
	if((0 <= ligne && ligne < 3) && (0 <= colonne && colonne < 3) && (plateau[ligne][colonne] == ' '))
	     return 1;
	else return 0;
}

char case_libre(char plateau[][3]) {

	for(int i = 0; i < 3; i++) {
		for(int j = 0; j < 3; j++) {
			if(plateau[i][j] == ' ') return 1;
		}
	}
	return 0;
}
char aligne(char symbole, char plateau[][3]) {

	return	 ((plateau[0][0] == symbole) && (plateau[0][1] == symbole) && (plateau[0][2] == symbole)) 
	      || ((plateau[1][0] == symbole) && (plateau[1][1] == symbole) && (plateau[1][2] == symbole)) 
	      || ((plateau[2][0] == symbole) && (plateau[2][1] == symbole) && (plateau[2][2] == symbole)) 
	      || ((plateau[0][0] == symbole) && (plateau[1][0] == symbole) && (plateau[2][0] == symbole)) 
	      || ((plateau[0][1] == symbole) && (plateau[1][1] == symbole) && (plateau[2][1] == symbole)) 
	      || ((plateau[0][2] == symbole) && (plateau[1][2] == symbole) && (plateau[2][2] == symbole)) 
	      || ((plateau[0][0] == symbole) && (plateau[1][1] == symbole) && (plateau[2][2] == symbole)) 
	      || ((plateau[0][2] == symbole) && (plateau[1][1] == symbole) && (plateau[2][0] == symbole)); 
}
int main() {
	printf("\nJeu Du Morpion\n\n");	
	char plateau[3][3] = {{' ',' ',' '},{' ',' ',' '},{' ',' ',' '}};
	unsigned int ligne,colonne;
	unsigned char joueur_1_actif = 1;
	unsigned char joueur_2_actif = 0;
	char partie_en_cours = 1;
	affiche(plateau);

	while(partie_en_cours && case_libre(plateau)) {
		if(joueur_1_actif) {
			printf("\nJoueur 1 : (symbole ligne colonne) \n");
			scanf("%d %d",&ligne,&colonne);

			if(case_valide(ligne,colonne,plateau)){
					plateau[ligne][colonne] = 'X';
					affiche(plateau);	
					if(aligne('X',plateau)){
						printf("\nJoueur 1 Gangne\n");
						partie_en_cours = 0;

				} else {
					joueur_1_actif = 0;
					joueur_2_actif = 1;
				}
			}else {
				printf("Case invalide, joueur 1 rejoue !!\n");
			}

		}
		if(joueur_2_actif && case_libre(plateau)) {
			printf("\nJoueur 2 : (symbole ligne colonne) \n");
			scanf("%d %d",&ligne,&colonne);

			if(case_valide(ligne,colonne,plateau)){
					plateau[ligne][colonne] = 'O';
					affiche(plateau);	
					if(aligne('O',plateau)){
						printf("\nJoueur 2 Gangne\n");
						partie_en_cours = 0;

				} else {
					joueur_1_actif = 1;
					joueur_2_actif = 0;
				}
			}else {
				printf("Case invalide, joueur 2 rejoue !!\n");
			}

		}


	}
	if(!case_libre(plateau))
		printf("\n Pas de gagnants plus de place sur le plateau \n");
	printf("\nEND GAME...\n");	
	return 0;
}
