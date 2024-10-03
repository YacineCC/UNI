#include <stdio.h>
#include <limits.h>
int collatz(unsigned int x) {

    if(x%2)
        return 3*x + 1;
    else
        return x / 2;
}

void syracuse(unsigned int x) {

    if(x != 1){

        printf("%d\n",collatz(x));
        x = collatz(x);
        syracuse(x);
    }
}
int n = 0;
int temps_de_vol(unsigned int x) {
    if(x != 1){
        x = collatz(x);
        n +=1;
        temps_de_vol(x);
    }
    return n;
}
int max = INT_MIN;
int altitude(unsigned int x){

    if(x != 1) {
        x = collatz(x);
        altitude(x);
        if(max < collatz(x))
            max = x;




    }

    return max;
}


int main() {

    int n,x,z;

    printf("Entrer un entier : ");
    scanf("%d", &n);
    printf("Collatz(%d) = %d \n", n, collatz(n));
    printf("Entrer un entier : ");
    scanf("%d", &x);
    z = x;
    syracuse(x);

    printf("Temps de vol : %d\n",temps_de_vol(x));
    printf("Altitude : %d\n", altitude(x));
    return 0;
}
