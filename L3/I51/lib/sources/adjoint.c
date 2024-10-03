#include "adjoint.h"
#include <stdio.h>
#include <stdlib.h>


graphe* adjoint(graphe* g)
{
	int nbarretes = nbArretes(g);
	graphe* adjoi = initGraphe(nbarretes);
	int** SommetsAdjoints = (int**)malloc(nbarretes*sizeof(int*));
	liste tmp;
	int i;
	int edgeIndex = 0;
	for(i = 0; i < g->nbs; i++)
	{
		tmp = g->adj[i];
		while(tmp != NULL)
		{
			if(i < tmp-> num)
			{
				int* sommet = (int*)malloc(2*sizeof(int));
				sommet[0] = i;
				sommet[1] = tmp->num;
				SommetsAdjoints[edgeIndex++] = sommet;
			
			}
			tmp = tmp->svt;
		}

	}

	for(i = 0  ; i < edgeIndex; i++)
	{
		for(int j = i; j < edgeIndex; j++)
		{
			if(SommetsAdjoints[i][0] == SommetsAdjoints[j][0]
			|| SommetsAdjoints[i][0] == SommetsAdjoints[j][1]
			|| SommetsAdjoints[i][1] == SommetsAdjoints[j][0]
			|| SommetsAdjoints[i][1] == SommetsAdjoints[j][1])
				ajoutArrete(adjoi, i, j, 0);
		}
	}
	for(int i = 0; i < nbarretes; i++)
		free(SommetsAdjoints[i]);
	free(SommetsAdjoints);

	return adjoi;
}

