#include "hypercube.h"
#include <stdio.h>


int wt(int a)
{
	int x = a;
	int poids = 0;
	while(x > 0)
	{
		if(x & 1)
			poids++;
		x = x >> 1;
	}
	return poids;
}

graphe* hypercube(int n)
{
	graphe* hyper = initGraphe(1<<n);
	for(int i = 0; i < hyper->nbs; i++)
	{
		for(int j = i+1; j < hyper->nbs; j++)
		{
			if(wt(i^j) == 1)
				ajoutArrete(hyper,i, j, 0);
		}
	}
	return hyper;
}
