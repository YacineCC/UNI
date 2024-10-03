#include <stdio.h>
#include <stdlib.h>

typedef int* VECTEUR;
typedef int** MATRICE;

int pow2(unsigned int n)
{
    return 1 << n;
}

VECTEUR vecteur_vide(unsigned int n)
{
    VECTEUR vide = (int*) calloc(n, sizeof(int));
    return vide;
}

void affiche_vecteur(VECTEUR v, unsigned int n)
{
    if(v == NULL)
    {
        return;
    }
    printf("(%d", v[0]);
    for(int i = 1; i < n; i++)
    {
        printf(", %d", v[i]);
    }
    printf(")");
}

VECTEUR vecteur(unsigned int n, unsigned int valeur)
{
    if(valeur >= pow2(n))
    {
        return NULL;
    }
    VECTEUR v = vecteur_vide(n);
    int x = valeur;
    int i = 0;
    while(x > 0)
    {
    
        //v[n-1-i] = x & 1;
        v[i] = x & 1;

        x = x >> 1;
        i++;
    }
    return v;
}

int valeur(VECTEUR v, unsigned int n)
{
    if(v == NULL)
    {
        return -1;
    }
    int res = 0;
    for(int i = 0; i < n; i++)
    {
        res += v[i] * pow2(n-1-i);
    }
    return res;
}

VECTEUR* mots(unsigned int k)
{
    if(k <= 0)
    {
        return NULL;
    }
    int pow2_k = pow2(k);
    VECTEUR* mots = (VECTEUR*)malloc(pow2_k*sizeof(VECTEUR));
    mots[0] = vecteur(k, 0);
    for(int i = 1; i < pow2_k; i++)
    {
        mots[i] = vecteur(k, i);
    }
    return mots;
}

void affiche_mots(VECTEUR* mots, unsigned int k)
{
    int pow2_k = pow2(k);
    printf("{");
    affiche_vecteur(mots[0], k);
    for(int i = 1; i < pow2_k; i++)
    {
        printf(",");
        affiche_vecteur(mots[i], k);
        
    }
    printf("}");
}


unsigned int poids(VECTEUR v, int n)
{
    int poids = 0;
    int x = n;
    for(int i = 0; i < n; i++)
    {
        if(v[i] & 1)
        {
            poids += 1;
        }
        x = x >> 1;
    }
    return poids;
}

VECTEUR diff(VECTEUR v, VECTEUR u, unsigned int n)
{
    if(n == 0)
    {
        return NULL;
    }
    VECTEUR res = vecteur_vide(n);
    for(int i = 0; i < n; i ++)
    {
        res[i] = v[i] ^ u[i];
    }
    return res;
}

unsigned int hamming(VECTEUR u, VECTEUR v, int n)
{
    if(n == 0)
    {
        return 0;
    }
    VECTEUR d = diff(u, v, n);
    unsigned int ham = poids(d, n);

    free(d);
    return ham;
}


void affiche_matrice(MATRICE mat, unsigned int l, unsigned int c)
{
    for(int i = 0; i < l; i++)
    {
        printf("[%d", mat[i][0]);
        for(int j = 1; j < c; j++)
        {
            printf(", %d", mat[i][j]);
        }
        printf("]\n");
    }
}

VECTEUR encode(MATRICE g, VECTEUR v, unsigned int k, unsigned int n)
{
    VECTEUR res = vecteur_vide(n);
    int tmp = 0;
    for(int i = 0; i < n; i++)
    {
        
        //printf("%d ", i);
        for(int j = 0; j < k; j++)
        {
            res[i] = res[i] ^ (v[j] & g[j][i]);
        }
        
        
    }
    return res;
}

MATRICE mat_vide(unsigned int l, unsigned int c)
{
    MATRICE mat = (int**)calloc(l, sizeof(int*));

    for(int i = 0; i < l; i++)
    {
        mat[i] = (int*)calloc(c, sizeof(int));
    }
    return mat;
}

void free_mat(MATRICE m, unsigned int l)
{
    for(int i = 0; i < l; i++)
    {
        free(m[i]);
    }
    free(m);
}

void free_mots(VECTEUR* mots, unsigned int l)
{
    for(int i = 0; i < l; i++)
    {
        free(mots[i]);
    }
    free(mots);
}

void affiche_mots_encode(MATRICE gen, VECTEUR* mots, unsigned int k, unsigned int n)
{
    int pow2_k = pow2(k);
    printf("{");
    affiche_vecteur(mots[0], k);
    for(int i = 1; i < pow2_k; i++)
    {
        printf(",");
        affiche_vecteur(mots[i], k);
        
    }
    printf("}");
}



int main(void)
{
    unsigned int n = 4;
    int val = 7;
    // VECTEUR v = vecteur(n, val);
    // affiche_vecteur(v, n);
    // unsigned int k = 3;
    // VECTEUR* test_mots = mots(k);
    // affiche_mots(test_mots, k);
    // printf("\npoids : %d\n", poids(v, n));

    VECTEUR v = vecteur(n, val);
    VECTEUR u = vecteur(n, 6);
    VECTEUR xor = diff(v, u, n);
    affiche_vecteur(xor, n);
    unsigned int ham = hamming(u, v, n);
    printf("\nhamming %d\n", ham);
    free(v);
    free(u);
    free(xor);
    //MATRICE mat_gen = mat_vide(4, 7);
    unsigned int k = 4;
    n = 7;
    MATRICE mat_gen = mat_vide(k, n);
    mat_gen[0][0] = 1;mat_gen[0][1] = 0;mat_gen[0][2] = 0;mat_gen[0][3] = 0;mat_gen[0][4] = 1;mat_gen[0][5] = 0;mat_gen[0][6] = 1;

    mat_gen[1][0] = 0;mat_gen[1][1] = 1;mat_gen[1][2] = 0;mat_gen[1][3] = 0;mat_gen[1][4] = 1;mat_gen[1][5] = 1;mat_gen[1][6] = 1;

    mat_gen[2][0] = 0;mat_gen[2][1] = 0;mat_gen[2][2] = 1;mat_gen[2][3] = 0;mat_gen[2][4] = 1;mat_gen[2][5] = 1;mat_gen[2][6] = 0;

    mat_gen[3][0] = 0;mat_gen[3][1] = 0;mat_gen[3][2] = 0;mat_gen[3][3] = 1;mat_gen[3][4] = 0;mat_gen[3][5] = 1;mat_gen[3][6] = 1;



    // int mat_gen[4][7] = {{1, 0, 0, 0, 1, 0, 1}
    //                 , {0, 1, 0, 0, 1, 1, 1}
    //                 , {0, 0, 1, 0, 1, 1, 0}
    //                 , {0, 0, 0, 1, 0, 1, 1}};
    
    VECTEUR* test_mots = mots(k);
    affiche_mots(test_mots, k);
    //affiche_vecteur(test_mots[0], k);
    // free_mots(test_mots, pow2(k));
    // free_mat(mat_gen, k);
    // VECTEUR ecode = encode(mat_gen, test_mots[0], k, n);
    // affiche_vecteur(ecode, k);
    for(int i = 0; i < pow2(k); i++)
    {
        VECTEUR tmp = encode(mat_gen, test_mots[i], k, n);
        affiche_vecteur(tmp, n);
        printf("\n");
        free(tmp);
    }

    
    return 0;
}