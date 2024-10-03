#include "disjoint.h"
#include <time.h>


int main(int argc, char** argv)
{
	

	
	int sample = atoi(argv[2]);

	srand(time(NULL));
	int n = atoi(argv[1]);
	ed* table = calloc(n, sizeof(ed));
	ed ri, rj;
	int i,j, moy = 0;
	
	
	
	for(int k = 0; k < sample; k++) 
	{	
		for(i = 0; i < n; i++)
		table[i] = singleton(i);
		int p = n, m = 0;
		
		while(p > 1) //Tant que le graphe n'est pas connexe
		{
			
			i = rand()%n;
			j = rand()%n;
			m++;	//Augmentation du nombre d'arrêtes
			ri = representant(table[i]);
			rj = representant(table[j]);
			
			if(ri != rj)
			{
				reunion(ri,rj);
				p = p-1;
			}
			
			
		}
		
		moy += m;
		
	}
	moy = moy/sample;
	printf("%d %d\n", n, moy);
	
	return 0;
}
