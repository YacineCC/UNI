#include <stdlib.h>
#include "graphe.h"
#include <time.h>

int main()
{
    srand(time(NULL));
    // float tmp[5][2] = {{1, 2}, {0, 1}, {2, 1}, {0, 0}, {2, 0}};
    point *nuagePenta = (point *) malloc(sizeof(point) * 5);
    nuagePenta[0].x = 1;
    nuagePenta[0].y = 2;

    nuagePenta[1].x = 0;
    nuagePenta[1].y = 1;

    nuagePenta[2].x = 2;
    nuagePenta[2].y = 1;

    nuagePenta[3].x = 0;
    nuagePenta[3].y = 0;

    nuagePenta[4].x = 2;
    nuagePenta[4].y = 0;
    

    graphe* acmPenta = Kruskal(nuagePenta, 5);
    dessiner("testAcmPentagrame", acmPenta);

    point* nuage = randNuage(10);
    graphe* acm = Kruskal(nuage, 10);
    dessiner("testAcm", acm);

    int* visite = calloc(10, sizeof(int));
    int test = 0;
    liste passage = creerElement(test);
    
    PPR(acm, test, visite, &passage);
    while(passage != NULL)
    {
        printf("%d ",passage->num);
        passage = passage->svt;
    }
    return 0;
}
