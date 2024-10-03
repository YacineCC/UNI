#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void affiche_tab(uint *tab, uint n)
{
	printf("[%u",tab[0]);
	for(int i = 1; i < n; i++)
	{
		printf(", %u", tab[i]);
	}
	printf("]\n");

}
void echanger(uint *T, uint a, uint b)
{
	uint tmp = T[a];
	T[a] = T[b];
	T[b] = tmp;
}

uint *GenPerm(uint n)
{
	uint *R = (uint *)malloc(sizeof(uint)*n);

	for(int i = 0; i < n; i++)
	{
		R[i] = i+1;
	}
	uint tmp;
	for(int i = 0; i < n; i++)
	{
		//tmp = rand()%(n + 1 - i) + i;
		tmp = rand()%n;
		echanger(R,tmp,i);
	}
	return R;
	
}

uint idxMin(uint *T, uint a, uint b)
{
	uint min = T[a];
	uint idx = a;
	for(int i = a; i <= b; i++)
	{
		if(T[i] < min)
		{
			min = T[i];
			idx = i;
		}
	}
	return idx;
}

void TriSelection(uint *T, uint n)
{
	uint idx;
	for(int i = 0; i < n; i++)
	{
		idx = idxMin(T, i, n-1);
		echanger(T, i, idx);
	}
}


/*
void Propager(uint *T, uint a, uint b)
{

	
	int s = (a < b) ? +1 : -1;
	uint k = a;

	while((s*(b-k)) > 0)
	{
		
		if((s * (T[k] - T[k+s])) >= 0)
			{
				echanger(T,k,k+s);
				
			}
		
		k = k + s;
	}
}
*/

void PropagerGD(uint *T, uint a, uint b)
{
	uint k = a;
	while(k < b)
	{
		if(T[k] > T[k+1])
		{
			echanger(T,k,k+1);
		}
		k++;
	}
}

void PropagerDG(uint *T, uint a, uint b)
{
	uint k = b;
	while(k > a)
	{
		if(T[k] < T[k-1])
		{
			echanger(T,k,k-1);
		}
		k--;
	}
}
void TriBulles(uint *T, uint n)
{
	for(int i = 0; i < n; i++)
	{
		PropagerGD(T,0,n-i);
	}
}

void TriCocktail(uint *T, uint n)
{
	int g = 0;
	int d = n;
	while(g < d)
	{
		PropagerGD(T,g,d);
		d = d - 1;
		if(g < d)
		{
			PropagerDG(T,g,d);
			g = g+1;
		}

	}
}


int main(int argc, char** argv)
{
	uint n;
	scanf("%u", &n);
	srand(time(NULL));
	uint *test = GenPerm(n);
	affiche_tab(test,n);
	TriCocktail(test,n);
	affiche_tab(test,n);
	free(test);
	return 0;

}

