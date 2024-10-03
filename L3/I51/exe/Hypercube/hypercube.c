#include "hypercube.h"
#include "inout.h"

int main(int argc, char** argv)
{
	
	graphe* hyper = hypercube(atoi(argv[1]));
	afficheAdj(hyper);
	dessiner("hypercube", hyper);
	
	

	return 0;
}
