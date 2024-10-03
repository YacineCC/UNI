#include <stdio.h>

int somme(int n) {

        if(n < 1)
                return 0;
        return n + somme(n-1);
}

int main() {
        
        int n;
        printf(" Saisir un entier : ");
        scanf("%d",&n);
        printf("La somme des entiers de 1 à %d = %d\n", n, somme(n));
        return 0;
}
