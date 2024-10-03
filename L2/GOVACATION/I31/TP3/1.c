#include <stdio.h>

int pgcd(int a, int b) {
	int tmp;
	while(b != 0) {
		
		tmp = b;
		b = a % b;
		a = tmp;
	}
	return a;
}





int main() {
	
	int a,b;
	printf("Saisir deux nombre pour avoir le pgcd : ");
	scanf("%d %d", &a, &b);	
	printf("%d\n",pgcd(a,b));
	return 0;
}
