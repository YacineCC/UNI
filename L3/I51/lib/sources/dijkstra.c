#include "dijkstra.h"
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int choisir(int* esti, int* visit, graphe* g)
{
	int score = INT_MAX, s, res;
	for(s = 0; s < g->nbs; s++)
	{
		if(!visit[s] && score > esti[s])
		{
			score = esti[s];
			res = s;
		}
	}
	return res;

}

void miseajour(int s, int* esti, int* r, int* visit, graphe* g)
{
	int t;
	liste tmp = g->adj[s];
	while(tmp != NULL)
	{
		t = tmp->num;
		if(!visit[t] && esti[t] > esti[s] + tmp->poids)
		{
			esti[t] = esti[s] + tmp->poids;
			r[t] = s;
		}
		tmp = tmp->svt;
	}
	visit[s] = 1;
	
}



void dijkstra(int a, int b, graphe* g)
{
	int* esti = calloc(g->nbs,sizeof(int));
	int* r = calloc(g->nbs,sizeof(int));
	int* visit = calloc(g->nbs,sizeof(int));

	int s;
	for(s = 0; s < g->nbs; s++)
	{
		esti[s] = INT_MAX;
		r[s] = INT_MAX;
		visit[s] = 0;
	}
	esti[a] = 0;
	
	int cpt = 0;
	while(cpt < g->nbs)
	{
		s = choisir(esti, visit, g);
		miseajour(s, esti, r, visit, g);
		cpt++;
	}
	
	r[a] = -1;
	do{printf("%d. ", b); b = r[b];} while(b>=0);
	

	free(esti);
	free(r);
	free(visit);

}
