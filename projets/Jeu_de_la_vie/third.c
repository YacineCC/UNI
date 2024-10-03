#include <SDL2/SDL.h>
#include <stdio.h>
#include <stdlib.h>

char **creation_matrice(unsigned int taille)
{
    char **matrice =  (char**)malloc(taille * sizeof(char*));

    for(int i = 0; i < taille; i++)
    {
        matrice[i] = (char*)malloc(taille * sizeof(char));
        
    }

    return matrice;
}

char **initialise_matrice(char **matrice, int taille)
{
    for(int i = 0; i < taille; i++)
    {
        for(int j = 0; j < taille; j++)
        {
            matrice[i][j] = '0';
        }
    }
    return matrice;
}
void affiche_matrice(char **tab, unsigned int taille)
{
    for(int i = 0; i < taille; i++)
    {
        for(int j = 0; j < taille; j++)
        {
            printf("%c", tab[i][j]);
        }
        printf("\n");
    }
}
void destruction_matrice(char **matrice, int taille)
{
    for(int i = 0; i < taille; i++)
    {
        free(matrice[i]);
        matrice[i] = NULL;
    }
    free(matrice);
    matrice = NULL;
}

char **choix_matrice(char **matrice, int taille)
{
    int x, y;
    int i = 1;
    printf("Choisir les coordonnees [x][y] des cases à initialisé vivantes (choisir (x,y) = (-1,-1) pour arreter la saisie.\n");
    do
    {
        printf("Case n°%d : ", i);
        getchar();
        scanf("(%d,%d)", &x, &y);

        if ((x < taille && x >= 0) && ((y < taille && y >= 0)))
        {
            if (matrice[x][y] == '1')
                printf("Case deja prise choisir une autre\n");

            else
            {
                printf("Case valide\n");
                matrice[x][y] = '1';
                i++;
                //affiche_matrice(matrice, taille); si on fait sans SDL
            }
        }
        else
        {
            
            if (x != -1 || y != -1)
                printf("Case invalide, recommencez\n");
        }
    } while (x != -1 || y != -1);

    return matrice;
}


char **copie_matrice(char **matrice1, char **matrice2, int taille)
{
    for(int i = 0; i < taille; i++)
    {
        for(int j = 0; j < taille; j++)
        {
            matrice2[i][j] = matrice1[i][j];
        }
    }
    return matrice2;
}

char **test_matrice(char **matrice1, int taille)
{
    char **matrice2;
    matrice2 = creation_matrice(taille);
    initialise_matrice(matrice2, taille);
    copie_matrice(matrice1, matrice2, taille);
    initialise_matrice(matrice1, taille);
    char count = 0;
    for(int i = 1; i < taille-1; i++)
    {
        for(int j = 1; j < taille-1; j++)
        {
            count = 0;
            if (matrice2[i-1][j-1] == '1')
                count += 1;
            if (matrice2[i][j-1] == '1')
                count += 1;
            if (matrice2[i+1][j-1] == '1')
                count += 1;
            if (matrice2[i-1][j] == '1')
                count += 1;
            if (matrice2[i+1][j] == '1')
                count += 1;
            if (matrice2[i+1][j+1] == '1')
                count += 1;
            if (matrice2[i][j+1] == '1')
                count += 1;
            if (matrice2[i-1][j+1] == '1')
                count += 1;
            if (matrice2[i][j] == '0')
            {
                if (count == 3)
                    matrice1[i][j] = '1';
            }
            else if (matrice2[i][j] == '1')
            {
                if (count != 2 && count != 3)
                    matrice1[i][j] = '0';
                else
                    matrice1[i][j] = '1';
            }
        }
    }
    destruction_matrice(matrice2, taille);
    return matrice1;
}



int main(int argc, char **argv)
{
    // Les dimensions de la fenetre (zone d'affichage en pixels)

    unsigned int taille_fenetre = 700; // Fenetre caree de taille 800x800 pixels

    
    // Le nombre de cellules presente dans la matrice
    unsigned int taille_matrice;
    printf("Taille de la matrice caree : ");
    scanf("%d", &taille_matrice);

    char **matrice;
    matrice = creation_matrice(taille_matrice);
    initialise_matrice(matrice, taille_matrice);
    choix_matrice(matrice, taille_matrice);

    unsigned int nb_tours;
    printf("Nombre de tours à afficher :");
    scanf("%d", &nb_tours);

    // Dimension d'une cellule
    unsigned int taille_cellule;

    // La taille d'une cellule en pixel
    // cette taille est fonction de  la dimension de la fenetre et du
    // Saisie de la taille de la matrice 
    taille_cellule = taille_fenetre / taille_matrice;
    

    printf("Taille de la matrice : %d x %d \n", taille_matrice, taille_matrice);
    printf("Taille d'une cellule (largeur x hauteur) : %dpx x %dpx\n", taille_cellule, taille_cellule);

    printf("\nLancement de l'interface graphique\n");

    SDL_Window* fenetre;
    SDL_Renderer* renderer; // Déclaration du renderer
    
    // Initialisation du SDL
    if(SDL_VideoInit(NULL) != 0)
    {
        printf("Erreur d'initialisation du SDL : %s", SDL_GetError());
        SDL_Quit(); // On quite le SDL
        return EXIT_FAILURE; // On stop le programme
    }
       
    // Création de la fenêtre, la fonction doit renvoie NULL si la fenêtre ne s'est pas bien crée
    fenetre = SDL_CreateWindow("Une fenetre SDL", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, taille_fenetre, taille_fenetre, 0);

    if(fenetre == NULL)
    {
        printf("Erreur lors de la creation d'une fenetre : %s", SDL_GetError());
        SDL_DestroyWindow(fenetre); // On detruit la fenetre
        SDL_Quit();
        return EXIT_FAILURE;
    }
    
    // Création du renderer, le renderer est l'objet qui permet
    // de dessier dans la fenêtre. La fonction renvoie NULL si le
    // renderer ne s'est pas bien crée

    renderer = SDL_CreateRenderer(fenetre, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);

    if(renderer == NULL)
    {
        printf("Erreur lors de la creation d'un renderer : %s", SDL_GetError());
        SDL_DestroyRenderer(renderer); // On detruit le renderer
        SDL_DestroyWindow(fenetre);
        SDL_Quit();
        return EXIT_FAILURE;
    }

    

    
    SDL_Rect cellule;

    for(int k = 0; k < nb_tours; k++)
    {
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        for(int i = 0; i < taille_matrice; i++)
        {
            for(int j = 0; j < taille_matrice; j++)
            {
                if(matrice[i][j] == '1')
                {

                    cellule.x = j * taille_cellule;
                    cellule.y = i * taille_cellule;
                    cellule.w = taille_fenetre / taille_matrice;
                    cellule.h = taille_fenetre / taille_matrice;

                    SDL_RenderFillRect(renderer, &cellule);


                }
            }
        }
        SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255);
        for(unsigned int col = 0; col < taille_matrice; col++)
        {
            SDL_RenderDrawLine(renderer, col * taille_cellule, 0, col * taille_cellule, taille_fenetre-1);
            SDL_RenderDrawLine(renderer, 0, col * taille_cellule, taille_fenetre-1,col*taille_cellule);
        }
        SDL_RenderPresent(renderer);
        SDL_Delay(100);


              
              
        test_matrice(matrice,taille_matrice);
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);
    }   

    SDL_Delay(7000); // Pause de 3 secondes avant de terminer la fenetre
    
    // Destruction du renderer et de la fenetre
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(fenetre);
    SDL_Quit(); // On quite la SDL
    destruction_matrice(matrice, taille_matrice);
    return 0;    
}
