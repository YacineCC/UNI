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
                affiche_matrice(matrice, taille);
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



int main(void)
{
    
    unsigned int taille;
    char **matrice; 
    printf("Choisir la taille de la matrice caree : ");
    scanf("%u", &taille);
    
    matrice = creation_matrice(taille);
    initialise_matrice(matrice, taille);

    choix_matrice(matrice, taille);
    affiche_matrice(matrice,taille);
    printf("\n--------------------------\n");

    
    

    for(int i = 0; i < 5; i++)
    { 
        test_matrice(matrice, taille);
        affiche_matrice(matrice,taille);
        printf("\n--------------------------\n");
        
    }
    destruction_matrice(matrice, taille);
    return 0;
}

