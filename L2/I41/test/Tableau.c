#include <stdio.h>
#include "Tableau.h"

void print_tab(int *tab, int n)
{
    printf("[%d", tab[0]);
    for(int i = 1; i < n; i++)
    {
        printf(", %d",tab[i]);
    }
    printf("]\n");
}


