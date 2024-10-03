#include <SDL2/SDL.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    // Les dimensions de la fenetre (zone d'affichage en pixels

    unsigned int frame_width = 800; // Largeur
    unsigned int frame_height = 800; // Hauteur


    // Le nombre de colonnes (columns) et de lignes (rows)
    unsigned int columns;
    unsigned int rows;

    // La largeur d'une colonne et la hauteur d'une ligne en pixel
    // ces tailles son fonction des dimensions de la fenetre et du
    // nombre de colonnes et de lignes
    unsigned int column_width;
    unsigned int row_height;

    // Saisie du nombre de colonnes et de lignes
    printf("Nombre de colonnes : ");
    scanf("%d", &columns);

    printf("Nombre de lignes : ");
    scanf("%d", &rows);

    // Calcul des largeurs de colonnes et hauteurs de lignes en pixel
    column_width = frame_width / columns;
    row_height = frame_height / rows;

    printf("Taille de la grille : %d x %d \n", columns, rows);
    printf("Taille d'une cellule (largeur x hauteur) : %dpx x %dpx\n", column_width, row_height);

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
    fenetre = SDL_CreateWindow("Une fenetre SDL", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, frame_width, frame_height, 0);

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

    
    // Dessin d'une grille au bonnes dimensions

    // Choix de la couleur utilisee pour le tracage
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, SDL_ALPHA_OPAQUE); // Couleur blanche (RGB 255, 255, 255) SDL_APLHA_OPAQUE est une constante à 255 pour l'opacité
    
    // Lignes verticales
    for(unsigned int col = 0; col < columns; col++)
    {
        SDL_RenderDrawLine(renderer, col * column_width, 0, col * column_width, frame_height);
    }

    // Lignes horizontales
    for(unsigned int row = 0; row < rows; row++)
    {
        SDL_RenderDrawLine(renderer, 0, row * row_height, frame_width, row * row_height);
    }

    // Demande au renderer d'appliquer les changements
    SDL_RenderPresent(renderer);





    SDL_Delay(3000); // Pause de 3 secondes avant de terminer la fenetre
    
    // Destruction du renderer et de la fenetre
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(fenetre);
    SDL_Quit(); // On quite la SDL
    return 0;    
}
