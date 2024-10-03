#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef unsigned long long ullong;
typedef unsigned int uint;

typedef struct
{
    ullong tab[2][2];
}tmat;

typedef struct
{
    ullong **mat;

    int lignes;
    int colonnes;
}matrice;



tmat produit(tmat A, tmat B)
{   
    tmat res;
    res.tab[0][0] = A.tab[0][0]*B.tab[0][0] + A.tab[0][1]*B.tab[1][0];
    res.tab[0][1] = A.tab[0][0]*B.tab[0][1] + A.tab[0][1]*B.tab[1][1];
    res.tab[1][0] = A.tab[1][0]*B.tab[0][0] + A.tab[1][1]*B.tab[1][0];
    res.tab[1][1] = A.tab[1][0]*B.tab[0][1] + A.tab[1][1]*B.tab[1][1];
    return res;

}

tmat tabid()
{
    tmat C; 

    C.tab[0][0] = 1;
    C.tab[0][1] = 0;
    C.tab[1][0] = 0;
    C.tab[1][1] = 1;

    return C;

}


tmat puissance(tmat M, uint n)
{
    tmat C = tabid();
    for(uint i = 0; i < n; i++)
    {
        C = produit(C,M);
    }
    return C;
}

tmat SM(tmat M, uint n)
{
    tmat R = tabid();
    tmat P = M;
    uint i = 0;
    while(i < n)
    {
        if(n & 1)
        {   
            R = produit(R,P);
        }
        P = produit(P,P);
        n = n >> 1; 
    }
    return R;
}

ullong  Fib(uint n)
{
    int F0 = 0;
    int F1 = 1;
    int F2;
    for(int i = 0; i < n; i++)
    {
        F2 = F1+F0;
        F0 = F1;
        F1 = F2;
    }
    return F0;
}

ullong FibSM(uint n)
{
    tmat P;
    P.tab[0][0] = 1;
    P.tab[0][1] = 1;
    P.tab[1][0] = 1;
    P.tab[1][1] = 0;
    
    P = SM(P,n-1);
    return P.tab[0][0];
}

void affiche_tmat(tmat mat)
{
    for(int i = 0; i < 2; i++)
    {
        printf("[%llu", mat.tab[i][0]);
        for(int j = 1; j < 2; j++)
        {
            printf(", %llu", mat.tab[i][j]);
        }
        printf("]\n");
        

    }
}

//Séparation entre programmation statique et dynamique.

matrice * allocmat(int lignes, int colonnes)
{   
    matrice *C =(matrice*)malloc(sizeof(matrice));

    ullong **mat = (ullong**)malloc(sizeof(ullong*)*lignes);
    for(int i = 0; i < lignes; i++)
    {
        mat[i] = (ullong*)malloc(sizeof(ullong)*colonnes);
    }
    C->lignes = lignes;
    C->colonnes = colonnes;
    C->mat = mat;
    return C;

}

matrice * randommat(int lignes, int colonnes, int n)
{
    matrice *C = allocmat(lignes, colonnes);
    for(int i = 0; i < lignes; i ++)
    {
        for(int j = 0; j < colonnes; j++)
        {
            C->mat[i][j] = random()%n;
        }
    }
    return C;
}

void destroymat(matrice *mat)
{
    for(int i = 0; i < mat->lignes; i++)
    {
        free(mat->mat[i]);
    }
    free(mat->mat);
    free(mat);

}


matrice* xmat(matrice *A, matrice *B)
{   
    if(A->colonnes != B->lignes)
    {
        exit(EXIT_FAILURE);
    }

    matrice* C = allocmat(A->lignes,B->colonnes);


    for(int i = 0; i < A->lignes; i++)
    {
        for(int j = 0; j < B->colonnes; j++)
        {
            C->mat[i][j] = 0;
            
            for(int k = 0; k < B->lignes; k++)
            {
                C->mat[i][j] += A->mat[i][k] * B->mat[k][j];
            }
        }
    }
    return C;

}

void affiche_matrice(matrice *A)
{
    for(int i = 0; i < A->lignes; i++)
    {
        printf("[%llu", A->mat[i][0]);
        for(int j = 1; j < A->colonnes; j++)
        {
            printf(", %llu", A->mat[i][j]);
        }
        printf("]\n");
        

    }
}



matrice * ID(int n)
{
    matrice *C = allocmat(n,n);
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(i == j)
            {
                C->mat[i][j] = 1;

            }
            else
            {
                C->mat[i][j] = 0;
            }
        }
    }
    return C;
}



int main()
{   
    srand(time(NULL));
    /*
    tmat A;
    //tmat B = tabid();

    A.tab[0][0] = random()%5;
    A.tab[0][1] = random()%5;
    A.tab[1][0] = random()%5;
    A.tab[1][1] = random()%5;

    

    tmat test = SM(A,5);
    affiche_tmat(A);
    printf("\n");
    affiche_tmat(test);
    */
    /*
    for(int i = 0; i < 10; i++)
    {
        printf("%llu ",Fib(i));
    }
    printf("\n");
    */
    uint n = 5;
    printf("fibo(%hhu) = %llu\n",n,FibSM(1000000));
    return 0;
    
    /*
    int n = 3;
    int m = 5;
    matrice *A = randommat(random()%10,m,6);
    //matrice *B = ID(n);
    matrice *B = randommat(m,random()%10,6);

    matrice *C = xmat(A,B);

    affiche_matrice(A);
    printf("\n");
    affiche_matrice(B);
    printf("\n");
    affiche_matrice(C);
    destroymat(A);
    destroymat(B);
    destroymat(C);
    */
}
