#include <stdio.h>


typedef unsigned int uint;


uint PairOuImpair(uint n)
{
    return(n%2?(3*n)+1:n/2);
}


uint Syracuse(long u0, long* altmax)
{
    int n = 0;
    *altmax = 0;
    while(u0 > 1)
    {
        if(u0 > *altmax)
        {
            *altmax = u0;
        }
        u0 = PairOuImpair(u0);
        n++;
    }

    return n;
}


void AfficheStat(long u0)
{
    long altmax = 0;
    uint tmpdevol = Syracuse(u0,&altmax);
    printf("Temps de vol : %d\nAltitude maximale : %ld\n",tmpdevol,altmax);
}


int main(void)
{
    AfficheStat(4563281);
    AfficheStat(10);
    FILE *fichier = fopen("Syracuse.txt","w+");
    
    long altmax = 0;
    for(int n = 1; n < 10; n++)
     
    {
        fprintf(fichier,"%d %d\n",n,Syracuse(n,&altmax));
    }

    fclose(fichier);
}

