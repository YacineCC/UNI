#include "graphe.h"
#include <time.h>


int main()
{
	/*
	graphe* testTableau = initGraphe(7);
	ajoutArrete(testTableau, 0, 1, 10);
	ajoutArrete(testTableau, 0, 2, 5);
	ajoutArrete(testTableau, 1, 2, 12);
	ajoutArrete(testTableau, 1, 3, 3);
	ajoutArrete(testTableau, 2, 4, 18);
	ajoutArrete(testTableau, 3, 5, 4);
	ajoutArrete(testTableau, 3, 4, 1);
	ajoutArrete(testTableau, 4, 6, 2);
	ajoutArrete(testTableau, 5, 6, 1);
	dessiner("dijkstra", testTableau);
	dijkstra(0,6, testTableau); 

	freeGraphe(testTableau);
	*/
	srand(time(NULL));
	graphe* randomGraphe = initGraphe(10);
	randGraphe(&randomGraphe, 0.2);
	dessiner("RandomGrapheDijkstra", randomGraphe);
	dijkstra(0, 9, randomGraphe);
	freeGraphe(randomGraphe);

	return 0;
}
