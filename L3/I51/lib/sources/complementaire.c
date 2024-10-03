#include "complementaire.h"
#include <stdio.h>


graphe* complementaire(graphe* g)
{
	graphe* comple = initGraphe(g->nbs);
	liste tmp;
	int flag[g->nbs];
	for(int i = 0; i < g->nbs; i++)
	{
		for(int j = 0; j < g->nbs; j++)	flag[j] = 1;

		tmp = g->adj[i];
		while(tmp != NULL)
		{
			flag[tmp->num] = 0;
			tmp = tmp->svt;
		}
		for(int k = i+1; k < g->nbs; k++)
		{
			if(flag[k] == 1)
			{
				ajoutArrete(comple, i, k, 0);
			}
		}
	}

	
	return comple;
}
