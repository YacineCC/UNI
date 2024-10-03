#include <graphe.h>
#include <time.h>


int main()
{
    srand(time(NULL));
    graphe* g = lireGraphe("maison.txt");
    
    printf("%d\n", estSemiEulerien(g));
    printf("%d\n", estEulerien(g));
    freeGraphe(g);

    while(estEulerien(g) != 1)
    {
        randGraphe(&g, 0.1);
        
    }
    dessiner("testEulerien",g);
    randGraphe(&g, 0.1);
    while(estSemiEulerien(g) != 1)
    {
        randGraphe(&g, 0.1);
        
    }
    dessiner("testSemiEulerien",g);
    freeGraphe(g);
}