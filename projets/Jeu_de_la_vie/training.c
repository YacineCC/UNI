#include <stdio.h>
#include <stdlib.h>
#include <SDL2/SDL.h>

void SDL_ExitWithError(const char *message);

int main(int argc, char **argv)
{
    SDL_Window *window = NULL;
    SDL_Renderer *renderer = NULL;
    
    //Lancement SDL
    if(SDL_Init(SDL_INIT_VIDEO) != 0)
    {
        SDL_ExitWithError("Initialisation SDL");
    }
    
    //Création fenêtre
    window = SDL_CreateWindow("Première fenêtre SDL 2",SDL_WINDOWPOS_CENTERED, 
                              SDL_WINDOWPOS_CENTERED,800, 600, 0);
    
    if(window == NULL)
    {
        SDL_ExitWithError("Creation fenetre echouee");
    }
    
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_SOFTWARE);

    if(renderer == NULL)
    {
        SDL_ExitWithError("Creation rendu echouee");
    }

    if(SDL_SetRenderDrawColor(renderer, 255, 255, 255, SDL_ALPHA_OPAQUE) != 0)
    {
        SDL_ExitWithError("Impossible de changer la couleur pour le rendu");
    }

    if(SDL_RenderDrawPoint(renderer, 100, 450) != 0)
    {
        SDL_ExitWithError("Impossible de dessiner un poin");
    }
    for(int k = 0; k < 800; k += 100){
        if(SDL_RenderDrawLine(renderer, k, 0, k, 800 ) != 0)
        {
           SDL_ExitWithError("Impossible de dessiner une ligne");
        }
    }
    for(int k = 0; k < 600; k += 100){
        if(SDL_RenderDrawLine(renderer, 0, k, 800, k ) != 0)
        {
           SDL_ExitWithError("Impossible de dessiner une ligne");
        }
    }

    SDL_Rect rectangle;
    rectangle.x = 300;
    rectangle.y = 300;
    rectangle.w = 200;
    rectangle.h = 200;
    if(SDL_SetRenderDrawColor(renderer, 255, 15, 15, SDL_ALPHA_OPAQUE) != 0)
    {
        SDL_ExitWithError("Impossible de changer la couleur pour le rendu");
    }


    if(SDL_RenderFillRect(renderer, &rectangle) != 0)
    {
        SDL_ExitWithError("Impossible de dessiner un rectangle");
    }

    SDL_RenderPresent(renderer);

    if(SDL_RenderClear(renderer) != 0)
    {
        SDL_ExitWithError("Effacement rendu echouee");
    }
    


/* Création fenêtre + rendu
    if(SDL_CreateWindowAndRenderer(800, 600, 0, &window, &renderer) != 0)
        SDL_ExitWithError("Impossible de creer la fenetre et le rendu");
*/


    
    SDL_Delay(3000);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();



    return EXIT_SUCCESS;

}

void SDL_ExitWithError(const char *message)
{
    SDL_Log("Erreur : %s > %s\n", message, SDL_GetError());
    SDL_Quit();
    exit(EXIT_FAILURE);
}
