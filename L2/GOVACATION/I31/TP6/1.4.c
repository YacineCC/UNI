#include <stdio.h>

int digits(int n) {

    if(n < 1)
        return 0;

    return 1 + digits(n/10);
}

int main() {

    printf("Saisir l'entier : ");
    int n;
    scanf("%d",&n);
    printf("L'entier %d est composé de %d chiffre(s).\n", n, digits(n));
    return 0;
}

