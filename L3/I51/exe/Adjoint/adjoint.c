#include "graphe.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
	graphe* testAdjoint = lireGraphe("TestAdjoint.txt");
	graphe* adjoi = adjoint(testAdjoint);
	dessiner("TestAdjoint", testAdjoint);
	dessiner("Adjoint", adjoi);
	afficheAdj(testAdjoint);
	freeGraphe(testAdjoint);
	freeGraphe(adjoi);
	return 0;
}
