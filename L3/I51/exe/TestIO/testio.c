#include "graphe.h"
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
//extern int verb;



int main(int argc, char* argv[])
{
	srand(time(NULL));
	srand(time(NULL));
//Gérer les options dans la commande.
	char* option = "n:p:o:";
	int opt, n=64;
	char* o = NULL;
	//char v[128]
	float p = 0.5;
	while((opt = getopt(argc, argv, option)) != -1)
	{
		switch(opt)
		{
			case 'n':
				n = atoi(optarg);
				break;
			case 'p':
				p = atof(optarg);
				break;
			case 'o':
				//verb++;
				//printf("%s",optarg);
				o = optarg;
				//sprintf(v,"%s",optarg);
				break;
			case '?':
				exit(EXIT_FAILURE);
		}
	}
	
	//Test de dessiner
	graphe* g = initGraphe(n);
	randGraphe(&g, p);
	dessiner(o, g);
	afficheAdj(g);
	freeGraphe(g);
	

	//Test de lecture et d'écriture d'un graphe depuis un fichier
	minilire("maison.txt");
	
	graphe* L = lireGraphe("maison.txt");
	dessiner("testLireMaison",L);
	ecrireGraphe("testEcrireMaison.txt", L);
	graphe* h = lireGraphe("testEcrireMaison.txt");
	dessiner("TestEcrireMaison",h);
	
	printf("nb arretes  maison : %d\n", nbArretes(L));
	enleveArrete(L, 0, 1);
	printf("nb arretes  maison : %d\n", nbArretes(L));
	dessiner("testLireMaisonMoins1",L);
	//afficheAdj(h);

	return 0;


}
