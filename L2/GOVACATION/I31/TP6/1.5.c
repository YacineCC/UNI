#include <stdio.h>

int pgcd(unsigned int n, unsigned int m) {

    if(m == 0)
        return n;

    return pgcd(m, n % m);
}

int main() {
    printf("Saisir deux entiers non signés : ");
    int n,m;
    scanf("%u %u", &n, &m);
    printf("PGCD(%u,%u) = %d\n", n, m, pgcd(n,m));
    return 0;
}
