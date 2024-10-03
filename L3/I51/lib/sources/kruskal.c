#include "kruskal.h"
#include <math.h>
#include <stdlib.h>
#include "disjoint.h"
double distance_euclidienne(point a, point b)
{
    return sqrt((b.x-a.x)*(b.x-a.x) + (b.y-a.y)*(b.y-a.y));
}
int compar_arr(const void * x,const void * y)
{
    arc * a = (arc*)x;
    arc * b = (arc*)y;

    if(a->poids > b->poids)
    {
        return 1;
    }
    else
    {
        if(a->poids < b->poids)
        {
            return -1;
        }
        else
        {
            return 0;
        }
    }

}

graphe* Kruskal(point* nuage, int n)
{
    int nbarr = (n*(n-1))/2;
    arc* arcs =(arc*)malloc(nbarr*sizeof(arc));
    graphe* g = initGraphe(n);
    int m = 0;
    for(int i = 0; i < n; i++)
    {
        for(int j = i+1; j < n; j++)
        {
            
            arcs[m].s1 = i;
            arcs[m].s2 = j;
            arcs[m].poids = distance_euclidienne(nuage[i],nuage[j]);
            
            m++;  
        }

    }
    
    
    qsort(arcs, nbarr, sizeof(arc), compar_arr);
    
   

    ed* table = calloc(n, sizeof(ed));
	ed ri, rj;
    for(int i = 0; i < n; i++)
    {
		table[i] = singleton(i);
    }
    int p = n;
   
    for(int i = 0; i < nbarr; i++)
    {	
        ri = representant(table[arcs[i].s1]);
        rj = representant(table[arcs[i].s2]);
        
        if(ri != rj)
        {
            reunion(ri,rj);
            ajoutArrete(g, arcs[i].s1, arcs[i].s2, arcs[i].poids);
            p = p - 1;
        }
        
    }
    
    return g;
}

point* randNuage(int n)
{
    point* nuage = (point*)malloc(n*sizeof(point));
    for(int i = 0; i < n; i++)
    {
        nuage[i].x = random()%10;
        nuage[i].y = random()%10;
    }
    return nuage;
}
