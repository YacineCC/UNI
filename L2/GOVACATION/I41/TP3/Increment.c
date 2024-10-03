#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long ullong;
typedef unsigned char uchar;

void AfficheTab(uchar *tab, int n)
{
    printf("[%d",tab[0]);
    for(int i = 1; i < n; i++)
    {
        printf(", %d",tab[i]);
    }
    printf("]\n");
}

uchar NbChiffres(uchar A, uchar b)
{
    uchar nbchiffres = 0;
    while(A > 0)
    {
        A = A / b;
        nbchiffres++;
    }
    return nbchiffres;
}

uchar *Renverse(uchar A, uchar n, uchar b)
{
    uchar *res = (uchar *)malloc(sizeof(uchar)*n);
    for(uchar i = 0; i < n; i++)
    {
        res[i] = A % b;
        A = A / b;
    }

    return res;
}


uchar Increment(uchar *A, uchar n, uchar b)
{

    uchar i = 0;
    while((i < n) && (A[i] == b-1))
    {
        A[i++] = 0;
    }
    A[i]++;
    return ++i;

}
        

void test(uchar n, uchar b)
{
    uchar NBC;

    for(int i = 0; i < n;i++)
    {
        NBC = NbChiffres(i,b);
        AfficheTab(Renverse(i,NBC,b),NBC);
    }

}


int main()
{   /*
    uchar A,n,b;
    printf("Saisir le nombre [0,255] à incrementer et sa base : ");
    scanf("%hhu %hhu",&A,&b);
    n = NbChiffres(A,b);
    uchar *test = Renverse(A,n,b);
    AfficheTab(test,n);
    uchar res = Increment(test, n, b);
    AfficheTab(test,n);
    free(test);
    printf("Nb d'opérations : %hhu\n",res);
    */
    test(10,2);

    return 0;

}
