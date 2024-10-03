#include <graphe.h>
#include <time.h>


int main()
{
    srand(time(NULL));
    graphe* g = initGraphe(10);
    while(estConnexe(g) != 1)
    {
        randGraphe(&g, 0.05);
    }
    dessiner("testConnexe", g);
    freeGraphe(g);
    return 0;
}