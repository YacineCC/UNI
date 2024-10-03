#include "coloration.h"
#include <stdio.h>

void colorier(int s, int fc[], int k, int* cpt, graphe* g)
{
	if(s == g->nbs)
	{
		*cpt = *cpt +1;
		return;
	}
	int dispo[k];
	int i;
	for(i = 0; i < k; i++)
	{
		dispo[i] = 1;
	}

	liste tmp = g->adj[s];
	while(tmp != NULL)
	{
		if(tmp->num < s)dispo[fc[tmp->num]] = 0;
		tmp = tmp->svt;
	}
	
	
	for(i = 0; i < k; i++)
	{
		if(dispo[i])
		{
			fc[s] = i;
			colorier(s+1, fc, k, cpt, g);
		}
	}
}

int coloration(int k, graphe* g)
{
	int fc[g->nbs];
	//int* fc = (int*)malloc(g->nbs * 
	for(int i = 0; i < g->nbs; i++) fc[i] = 0;
	int cpt = 0;

	colorier(0, fc, k, &cpt, g);
	return cpt;
}
