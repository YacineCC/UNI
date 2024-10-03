#include "graphe.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
	graphe* hyper = hypercube(3);
	
	graphe* comp = complementaire(hyper);
	dessiner("complementaire_hypercube_3", comp);
	return 0;
}
