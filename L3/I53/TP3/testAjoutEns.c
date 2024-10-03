#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include "afd.h"
#include "afn.h"



int main()
{
    srand(time(NULL));
    


    int ** listEtats = init_listEtats();
    
    for(int j = 0; j < 5; j++)
        ajoute_etat(&listEtats, random_set(5));
    listeEtats_print(listEtats);

    ajoute_etat(&listEtats, random_set(5));
    int testajout[] = {1, 2 , 3, 4, 5, 7, -1};
    
    ajoute_etat(&listEtats, testajout);
    
    int testcherche[] = {1,2,3, -1};
    ajoute_etat(&listEtats, testcherche);
    
    listeEtats_print(listEtats);
    
    
    printf("%d\n",cherche_etat(listEtats, testcherche));
    

    int testfaux[] = {0,0,0, -1};
    printf("%d\n",cherche_etat(listEtats, testfaux));
    
    //free_listEtats(listEtats);
    return 0;
}