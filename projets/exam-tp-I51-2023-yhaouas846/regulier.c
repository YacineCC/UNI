#include <stdio.h>
#include <stdlib.h>

typedef unsigned char uchar;

typedef struct {
	int **mat;
	int nbs;
	int *clr;
} graphe;

graphe init_graphe(int n)
{
	//graphe *G = malloc(sizeof(graphe));;
	graphe G;
	G.nbs = n;
	G.mat = calloc(n,sizeof(int**));
	G.clr = calloc(n,sizeof(int*));
	
	int i;
	for(i = 0; i < n; i++)
	{
		G.mat[i] = calloc(n, sizeof(int *));
	}



	return G;
}

void free_graphe(graphe G)
{
	int i;
	for(i = 0; i < G.nbs; i++)
	{
		free(G.mat[i]);
	}
	free(G.mat);

}


void dessiner(char* nom, graphe G)
{
	if(nom == NULL)
	{
		nom = "Sans_nom";
	}

	FILE* dst;
	char buffer[64];
	sprintf(buffer, "%s.dot", nom);
	dst = fopen(buffer, "w");

	if(dst == NULL)
	{
		perror(buffer);
		exit(1);
	}

	fprintf(dst, "graph %s {\n", nom);
	int i, j;
	for(i = 0; i < G.nbs; i++)
	{
		int flag = 0;
		for(j = i+1;  j < G.nbs; j++)
		{
			flag |= G.mat[i][j];
			if(G.mat[i][j] > 0)
			{
				fprintf(dst, "	%d--%d;\n", i, j);
			}
		}
		if(flag == 0)
		{
			fprintf(dst, "	%d;\n", i);
		}
	}

	fprintf(dst, "}\n");

	fclose(dst);
	char cmd[128];
	sprintf(cmd, "neato -Tpng %s.dot -o %s.png",nom, nom);
	system(cmd);
	
	
}



int degre(int s, graphe G)
{
	int i, j;
	int deg = 0;
	for(i = 0; i < G.nbs; i++)
	{
		for(j = 0; j < G.nbs; j++)
		{
			if(G.mat[i][j])
			{
				deg++;
			}
		}
	}
	return deg;
}


int test (graphe G)
{
	int i;
	int flag = -1;
	int deg = 0;
	int test;
	for(i = 0; i < G.nbs; i++)
	{
		test = degre(i, G);
		if(degre(i, G) > deg)
		{
			deg = test;
			flag++;
		}
	}
	if(flag > 0)
	{
		return 0;
	}
	else
	{
		return deg;
	}
}

graphe regulier(int n)
{
	graphe G = init_graphe(n);
	int i;
	for(i = 0; i < G.nbs; i++)
	{
		G.mat[i][(i+n+1)%n] = 1;
		G.mat[i][(i+n-1)%n] = 1;
		G.mat[i][(i +n+ i/2)%n] = 1;

	}
	return G;
}

int disponible(int *tab, int n)
{
	int *mex = calloc(n, sizeof(int));
	int i;
	for(i = 0; i < n; i++)
	{
		mex[tab[i]] = 1;
	}

	for(i = 0; i < n; i++)
	{
		if(mex[i] > 0)
		{
			return i;
		}
	}
	return -1;
}

int glouton(graphe G)
{
	int i;
	for(i = 0; i < G.nbs; i++)
	{
		G.clr[i] = G.nbs;
	}

	int j, set_indice;
	int *X;
	for(i = 0; i < G.nbs; i++)
	{
		X = calloc(i+1,sizeof(int));
		set_indice = 0;
		for(j = 0; j < G.nbs; j++)
		{
			X[set_indice] = G.clr[j];
			set_indice += 1;
		}
		G.clr[i] = disponible(X, i+1);
		free(X);
	}

	int max = G.clr[0];
	
	for(i = 0; i < G.nbs; i++)
	{
		if(G.clr[i] > max)
		{
			max = G.clr[i];
		}
	}
	return max;
}


int main(int argc, char **argv)
{
	int n = atoi(argv[1]);

	graphe G = regulier(n);
	
	dessiner("regulier",G);
	glouton(G);
	dessiner("Coloration", G);
	free_graphe(G);

	return 0;
}
