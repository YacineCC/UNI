#include <stdio.h>

typedef unsigned int uint;

uint PairOuImpair(uint n){
    
    n = (n%2) ? 3*n+1 : n/2;
    return n;

}

uint Syracuse(uint u0){
    
    uint i = 0;

    while(u0 != 1){
        u0 = PairOuImpair(u0);
        i += 1;
    }
    return i;
}

void CourbeSyr(uint n){
     int i = 0;
     FILE *f = fopen("test.txt","w");
     while(n != 1){
        n = PairOuImpair(n);
        fprintf(f,"%u %u\n",i,n);
        i += 1;
    }
    fclose(f);
}
void Courbe2Syr(uint n){
    FILE *f = fopen("test.txt","w");
    uint i = 1;
    while(i < n){
        fprintf(f,"%u %u\n",i,Syracuse(i));
        i++;
    }
    fclose(f);
}



int main(){
    uint n = 1500;
    //CourbeSyr(n);
    Courbe2Syr(n);
    return 0;
}
