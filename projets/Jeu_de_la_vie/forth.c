#include <stdio.h>
#include <stdlib.h>
#include <SDL2/SDL.h>

// Definition de la structure Matrice caree  avec un tableau de tableau de caracteres et une taille

typedef struct
{
    char **data;
    unsigned int taille;

}Matrice;


// Creation de la matrice, allocation de memoire et test du pointeur puis allocation
// de chaque elements du tableau avec une boucle, on utilise ici un calloc pour 
// directement initialiser tous les elements a 0, on fait bien attention a la
// validitee des pointeurs.

Matrice *creation_matrice(unsigned int taille)
{
    Matrice *m = (Matrice *)malloc(sizeof(Matrice));
    
    char **d = (char **)malloc(taille*sizeof(char *));
    if(m== NULL || d == NULL)
        return NULL;

    for(unsigned int i = 0; i < taille; i++)
    {
        d[i] = (char *)calloc(taille,sizeof(char));
        if(d[i] == NULL)
            return NULL;
    }

    m -> taille = taille;
    m -> data = d;
    return m;
}

// On detruit la matrice en prenant garde a bien desallouer toutes les parties
// et a mettre tous les pointeurs a NULL
void destruction_matrice(Matrice * pm)
{
    if(pm == NULL || pm -> data == NULL)
        return;
    for(unsigned int i = 0; i < pm -> taille; i++)
    {
        free(pm -> data[i]);
        pm -> data[i] = NULL;
    }
    free(pm -> data);
    pm -> data = NULL;
    free(pm);
    pm = NULL;
}
// Fonction pour afficher la matrice sur le terminal pour effectuer les tests avant la SDL
void affiche_matrice(Matrice *pm)  // pm = pointeur sur matrice
{
    if(pm == NULL || pm -> data == NULL)
    {
        printf("[]\n");
        return;
    }
    for(unsigned int i = 0; i < pm -> taille; i++)
    {
        printf("[");
        for(unsigned int j = 0; j < pm -> taille; j++)
        {
            printf("%d", pm -> data[i][j]);
        }
        printf("]\n");
    }
}

// On initialise les les elements a 0, cette fonction sera utile
// dans la partie mise a jour de la matrice.
Matrice *initialise_matrice(Matrice *pm)
{
    if(pm == NULL || pm -> data == NULL)
        return NULL;

    for(unsigned int i = 0; i < pm -> taille; i++)
    {
        for(unsigned int j = 0; j < pm -> taille; j++)
        {
            pm -> data[i][j] = 0;
        }
    }
    
    return pm;
}

//Copie exactement tous les element du premier parametre dans le deuxieme
//cette fonction est necessaire car un simple matrice2 = matrice1
//n'est pas possible en langage C contrairement au Python, car cela
//va juste poiter au meme endroit, donc risque de perdre l'adresse
//de l'original et fuite memoire.
Matrice *copie_matrice(Matrice *pm, Matrice *pmc) // pmc = pointeur sur matrice copie
{
    if((pm == NULL  || pm -> data == NULL) || (pmc == NULL || pmc -> data == NULL))
        return NULL;
    for(unsigned int i = 0; i < pm -> taille; i++)
    {
        for(unsigned int j = 0; j < pm -> taille; j++)
        {
            pmc -> data[i][j] = pm -> data[i][j];
        }
    }

    return pmc;
}

//La fonction demande une saisie tant que la coordonnee speciale (-1,-1) n'est
//pas entree, le getchar est important pour pas que le buffer d'un ancien scanf
//interfere avec le traitement on verifie la validitee de la case et on change
//sa valeur a "1" donc vivante sur la matrice donee en parametre.
Matrice *choix_matrice(Matrice *pm)
{
    if(pm == NULL || pm -> data == NULL)
        return NULL;
    int x,y;
    int i = 1;
    
    getchar();
    printf("Choisir les coordonnees [x][y] des cases à initialiser vivantes. (Enter (x,y) = (-1,-1) pour arreter la saisie\n");
    
    do
    {
        printf("Case n°%d : ",i);
        scanf("(%d,%d)", &x, &y);
        getchar();

        if((x < pm -> taille && x >= 0) && ((y < pm -> taille && y >= 0)))
        {
            if(pm -> data[x][y] != 0)
                printf("Case deja prise, choisir une autre\n");

            else
            {
                printf("Case valide\n");
                pm -> data[x][y] = 1;
                i++;
                //affiche_matrice(pm);
            }
        }
        
        else
        {
            if(x != -1 || y != -1)
                printf("Case invalide, recommencez\n");
        }

    } while( x != -1 || y != -1);

    return pm;
}

//Le coeur du programme, on cree une matrice temporaire sur laquelle
//on passera l'algorithme, on initialise la matrice originale a 0
//puis pour chaque elements on regarde tous ses voisins dans un rayon
//de 1 et on ajoute 1 au compteur si il est vivant. Le nombre de voisins
//vivants et si la case elle meme est vivante ou non determineront son 
//futur selon les regles du jeu de la vie. On copie le resultat la 
//matrice originale vierge puis on detruit la matrice temporaire.
Matrice *update_matrice(Matrice *pm)
{
    if(pm == NULL || pm -> data == NULL)
        return NULL;
    Matrice *pmc = creation_matrice(pm -> taille);
    copie_matrice(pm,pmc);
    initialise_matrice(pm);
    
    unsigned int count = 0;
    for(unsigned int i = 1; i < pm -> taille -1; i++)   // On part de 1 et on s'arrete à pm -> taille -1
                                                        // pour ne pas depasser de la matrice et avoir un segmentation fault.
    {
        for(unsigned int j = 1; j < pm -> taille -1; j++)
        {
        
            count = 0;
            for(int x = -1; x <= 1; x++)
            {
                for(int y = -1; y <= 1; y++)
                {
                    if(pmc -> data[i+x][j+y] != 0)
                    {
                        count += 1;
                    }
                }
            }
            if(pmc -> data[i][j] != 0)
            {
                count -= 1;                             // ici on enleve 1 au compteur car si la case originale etait
                                                        // vivante elle serai rajoutee au compteur.
                if(count == 2 || count == 3)
                
                    pm -> data[i][j] = 1;
                
            }
            else
            { 
                if(count == 3)
                    pm -> data[i][j] = 1;
            

            }
        }
    }
    
    destruction_matrice(pmc);
    return pm;
}

// On initialise le SDL en s'assurant qu'il s'est bien cree
// on affiche le message d'erreur et quite le programme sinon.
// La fonction ne renvoi rien.
void initialisation_SDL()
{
    if(SDL_VideoInit(NULL) != 0)
    {
        printf("Erreur d'initialisation du SDL : %s", SDL_GetError());
        SDL_Quit(); //On quite la SDL
        exit(EXIT_FAILURE); //On sort du programme
    }
}

// Creation de la fenetre avec le meme procede.
// La fonction renvoi le renderer sous forme
// de pointeur d'un type special de la librairie SDL.
SDL_Window *creation_fenetre(unsigned int taille_fenetre)
{
    SDL_Window *fenetre = SDL_CreateWindow("Jeu de la vie", SDL_WINDOWPOS_CENTERED,SDL_WINDOWPOS_CENTERED,taille_fenetre, taille_fenetre, 0);
    
    if(fenetre == NULL)
    {
        printf("Erreur lors de la creation d'une fenetre : %s", SDL_GetError());
        SDL_DestroyWindow(fenetre); //Destruction de la fenetre
        SDL_Quit(); 
        exit(EXIT_FAILURE);
    }
    return fenetre;

}
// Creation du renderer avec le meme procede
// que la fenetre
SDL_Renderer *creation_renderer(SDL_Window *fenetre)
{
    SDL_Renderer *renderer = SDL_CreateRenderer(fenetre, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    
    if(renderer == NULL)
    {
        printf("Erreur lors de la creation d'un renderer : %s", SDL_GetError());
        SDL_DestroyRenderer(renderer); // Destruction du renderer.
        SDL_DestroyWindow(fenetre);
        SDL_Quit();
        exit(EXIT_FAILURE);

    }
    return renderer;
}

// La fonction d'affichage SDL principale, apres s'etre assure de la validite
// du pointeur, on parcours la matrice en affichant avec la SDL toutes les cases
// vivantes.
void update_rendu(SDL_Renderer *renderer, Matrice *pm, unsigned int taille_fenetre, unsigned int taille_cellule)
{
    if(renderer == NULL || pm == NULL || pm -> data == NULL)
        return;
    SDL_Rect cellule;

    SDL_SetRenderDrawColor(renderer, 255,255,255,255); // On met la couleur de dessin a blanc RGB(255,255,255)
                                                       // Le dernier parametre est pour l'opacite on laisse a 255.
    for(int i = 0; i < pm -> taille; i++)
    {
        for(int j = 0; j < pm -> taille; j++)
        {
            if(pm -> data[i][j] != 0)
            {
                cellule.x = j * taille_cellule;              // La coordonnee et la taille de la case sont
                cellule.y = i * taille_cellule;             // calculees en fonction de la taille de la cellule et du rapport
                cellule.w = taille_fenetre / pm -> taille; // taille fenetre / taile matrice.
                cellule.h = taille_fenetre / pm -> taille;

                SDL_RenderFillRect(renderer, &cellule); // Dessin de la case.
            }
        }
    }

    SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255);   // Choix de la couleur verte.
    //Tracage d'un cadrillage, on le fait apres les dessins des cases pour les lignes se superposent correctement.
    for(unsigned int ligne = 0; ligne < pm -> taille; ligne++)
    {
        SDL_RenderDrawLine(renderer, ligne * taille_cellule, 0, ligne * taille_cellule, taille_fenetre);
        SDL_RenderDrawLine(renderer, 0, ligne * taille_cellule, taille_fenetre, ligne * taille_cellule);
    }
    //Mise a jour du  rendu.
    SDL_RenderPresent(renderer);
    //Pause de 100 microsecondes.
    SDL_Delay(100);

    //Mise a jour de la matrice pour un nouveau tour
    update_matrice(pm);
    //On choisi la couleur de dessin noir pour effacer tout le rendu pour recommencer un tour une un canvas vierge.
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer);
}

int main(void)
{
    
    unsigned int taille_fenetre;
    printf("Saisir la taille de la fenetre caree : \n");
    scanf("%u", &taille_fenetre);

    unsigned int taille_matrice;
    printf("Saisir la taille de la matrice caree : \n");
    scanf("%u", &taille_matrice);

    unsigned int nb_tours;
    printf("Saisir le nombre de tours à afficher :\n");
    scanf("%u", &nb_tours);

    unsigned int taille_cellule = taille_fenetre / taille_matrice;

    Matrice *m = creation_matrice(taille_matrice);
    choix_matrice(m);

    printf("Taille de la matrice : %ux%u\n", taille_matrice, taille_matrice);
    printf("Taille d'une cellule (largeur x hauteur) : %upx x %upx\n", taille_cellule, taille_cellule);

    printf("Lancement de l'interface graphique\n");

    initialisation_SDL();
    SDL_Window *fenetre = creation_fenetre(taille_fenetre);
    SDL_Renderer *renderer = creation_renderer(fenetre);




        for(int i = 0; i < nb_tours; i++)
    {
        update_rendu(renderer, m, taille_fenetre, taille_cellule);

    }

    
    SDL_Delay(7000);

    
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(fenetre);
    SDL_Quit();
    destruction_matrice(m);
    return 0;
}
