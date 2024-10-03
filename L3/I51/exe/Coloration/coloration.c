#include "coloration.h"
#include "hypercube.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
	int k = atoi(argv[1]);
	graphe* hyper = hypercube(3);
	int res = coloration(k, hyper);
	printf("Nb de %d coloration : %d\n", k, res);
	return 0;
}
