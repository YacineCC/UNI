#include <stdio.h>

typedef unsigned int uint;
typedef unsigned short ushort;

void AfficheTab(int *tab, int n);

void Echanger(int **liste, int i, int j)
{
    int aux = (*liste)[i];
    (*liste)[i] = (*liste)[j];
    (*liste)[j] = aux;
}

int IdxMin(int *liste, int g, int d)
{
    int idxmin = g;
    int min = liste[g];

    for(int i = g; i <= d; i++)
    {
        if(liste[i] < min)
        {
            min = liste[i];
            idxmin = i;
        }
    }
    return idxmin;
}


void TriSelection(int *liste, ushort n)
{
    int i = 0;
    int imin = 0;
    while(i < n)
    {
        imin = IdxMin(liste,i,n-1);
        Echanger(&liste,i,imin);
        i++;
    }
}

void AfficheTab(int *tab, int n)
{
    printf("[%d",tab[0]);
    for(int i = 1; i < n; i++)
    {
        printf(", %d",tab[i]);
    }
    printf("]\n");
}

int main()
{

    printf("Taille en octet d'un uint : %ld\n",sizeof(uint));
    
    int tab[5] = {3,2,1,5,4};
    
    AfficheTab(tab,5);
    TriSelection(tab,5);
    AfficheTab(tab,5);

    return 0;
}
