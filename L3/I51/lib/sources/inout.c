#include "inout.h"

FILE* ouvrir(char* nom)
{
    FILE* f;
    f = fopen(nom, "r");
    if(f != NULL) return f; //Si il trouve le fichier dans le répertoire courant.

    char buffer[128];   //Sinon il va le chercher dans le répertoire "entrees".
    sprintf(buffer, "%s/entrees/%s", getenv("TAG"), nom);
    f = fopen(buffer, "r");
    if(f != NULL) return f;
    perror(nom);    //Sinon erreur.
    exit(1);
}

graphe* lireGraphe(char* nom)
{
    FILE* src = ouvrir(nom);
    int nbs, x, y;
    while(0==fscanf(src, "nbs=%d", &nbs)) fgetc(src);
    graphe* g = initGraphe(nbs);
    while(!feof(src))
    {
        if(fscanf(src, "%d%d", &x, &y) >1)
            ajoutArrete(g, x, y, 0);
        else fgetc(src);
    } 
	fclose(src);
    return g;
}

void ecrireGraphe(char* nom, graphe* g)
{
  
    FILE* dst;
    dst = fopen(nom, "w");
    if(dst == NULL)
    {
        perror(nom);
        exit(1);
    }
    /*
    for(int i = 0; i < g->nbs; i++)
    {
        enrliste* tmp = g->adj[i];
        fprintf(dst, "Sommet %d : [", i);
        while(tmp != NULL)
        {
            fprintf(dst, "%d->",tmp->num);
            tmp = tmp->svt;
        }
        fprintf(dst,"]\n");
    }
    */
   fprintf(dst, "nbs=%d\n",g->nbs);
   for(int i = 0; i < g->nbs; i++)
   {
    enrliste* tmp = g->adj[i];
    while(tmp != NULL)
    {
        if(tmp->num > i)
            fprintf(dst, "%d %d\n", i, tmp->num);
        tmp = tmp->svt;
    }
   }
    fclose(dst);
    char cmd[128];
    char* path = getenv("TAG");
    sprintf(cmd, "mv %s %s/entrees/", nom, path);
    system(cmd);
}

void minilire(char* nom)
{
    FILE* src = ouvrir(nom);
    int nbs, x, y;
    while(0==fscanf(src, "nbs=%d", &nbs)) fgetc(src);
    printf("ordre=%d\n",nbs);
    //allocation
    while(!feof(src))
    {
        if(fscanf(src, "%d%d", &x, &y) > 1)
            printf("x=%d y=%d\n", x, y);
        else fgetc(src);
    }
}



void dessiner(char* nom, graphe* g)
{
    if(nom == NULL) //Si il n'y a pas de nom de fichier. Nom par défaut.
    {
        nom = "Sans_Nom";
    }

    FILE* dst;  //Création du fichier "nom".dot.
    char buffer[64];
    sprintf(buffer, "%s.dot", nom);
    dst = fopen(buffer, "w");   //Ouverture du fichier en écriture.

    if(dst == NULL) //Si le fichier n'existe pas erreur.
    {
        perror(buffer);
        exit(1);
    }

    //Le but est de construire un fichier .dot comme si on le faisait à la main.
    fprintf(dst, "graph %s  {\n", nom);
    enrliste* tmp = NULL;
    for(int i = 0; i < g->nbs; i++)
    {
        //Avec la matrice d'adjacence (la liste d'adjacence sera préférée car plus efficace).
        /*int flg = 0;
        for(int j = i+1; j < g->nbs; j++)
        {
            flg |= g->mat[i][j];
            if(g->mat[i][j] == 1)   //Deux sommets reliés.
                fprintf(dst, "  %d--%d;\n", i, j);
        }
        if(flag == 0)
            fprintf(dst, "  %d;\n", i); //Sommet isolé.
        */
        
        tmp = g->adj[i];
        if(tmp == NULL) //Sommet isolé.
        {
            fprintf(dst, "%d[shape=circle];\n", i);
            
        }
        else
        {   
            fprintf(dst, "%d[shape=circle];\n", i);
            while(tmp != NULL)
            {
                if(tmp->num > i)    //Pour ne pas avoir d'arrêtes doublés.
                {
                    //ajouter le poids dans la structure de graphe
                    //fprintf(dst, "  %d--%d [label=\"%f\"];\n", i, tmp->num, );
                    fprintf(dst, "  %d--%d [label=\"%.1f\"];\n", i, tmp->num, tmp->poids);
                }
                tmp = tmp->svt;
            }
        }
    }
    //Cloture le .dot.
    fprintf(dst, "}\n");
    //Ferme le fichier.
    fclose(dst);

flag |= G.mat[i][j];
    //Le but est d'écrire une commande sur le terminal, avec l'intérmédiaire d'un buffer de caractères puis on éxecute la commande avec "system".
    char cmd[128];
    char* libpath = getenv("TAG");
    sprintf(cmd, "neato -Tpng %s.dot -o %s/sorties/%s.png", nom, libpath, nom);
    system(cmd);

    //Si tu veux supprimer les .dot.
    //sprintf(cmd, "rm %s.dot", nom);
    //system(cmd);
}

void afficheAdj(graphe* g)
{
    for(int s = 0; s < g->nbs; s++)
    {
        enrliste* tmp = g->adj[s];
        printf("Sommet %d : [", s);
        while(tmp != NULL)
        {
            printf("%d -%.1f->", tmp->num, tmp->poids);
            tmp = tmp->svt;
        }
        printf("]\n");
    }
}

