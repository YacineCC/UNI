#include <stdio.h>

int pgcd(int a, int b){
	int aux;

	while (b != 0){
		aux = a;
		a = b;
		b = aux % b;
	}
	return a;
}

int ppcm(int a, int b){
	return (a*b)/ pgcd(a,b);

}


int factorielle(int n){

	if(n == 0){
		return 1;
	}
	else{
	
	int fact = 1;
	while(n>0){

		fact *= n;
		n--;
	}

	return fact;
	}
}

int puissance(int x, int n) {
	int pui = 1 ;
	while(n > 0) {
		pui *= x;
		n --;
		 
	}
	return pui;
}

unsigned int arrangement(unsigned int n, unsigned int k) {
	return factorielle(n) / factorielle(n-k);
}

unsigned int combinaison(unsigned int n, unsigned int k){
	return (arrangement(n,k))/(factorielle(k));
}

int binome(int n) {

	for(int k = 0; k < n; k++) {
		printf("%dx^%d\n",combinaison(n,k),n-k);

}
}
void main(void){
	/*int a,b;
	printf("Saisir deux entier pour avoir leur pgcd : \n");
	scanf("%d %d",&a,&b);
	printf("%d\n",pgcd(a,b));
	
		
	float c,d;
	printf("Saisir deux entier pour avoir leur ppcm : \n");
	scanf("%d %d",&a,&b);
	printf("%d\n",ppcm(a,b));
	
	int fact;
	scanf("%d",&fact);
	printf("Factorielle %d\n",factorielle(fact));

	printf("%d\n",arrangement(2,10)); 

	printf("%d\n",combinaison(8,3)); */

	binome(10);

}
