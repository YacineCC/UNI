#include <stdio.h>

int main() {
	int i;
	int n;
	printf("Saisir la puissance du binôme : ");
	scanf("%d", &n);
	int k = 0;
	int FactN, FactK, FactNK,combi;
	for(k; k < n; k++) {
		
		FactN = 1;
		i = 0;
		while(n-i > 0) {

			FactN *= n-i;

			i++;
		}

		FactK = 1;
		i = 0;
		while(k-i > 0) {

			FactK *= k-i;

			i++;
		}
		FactNK = 1;
		i = 0;
		while((n-k)-i > 0) {

			FactNK *= (n-k)-i;

			i++;
		}
		combi = FactN / (FactK * FactNK);	
		printf("%d(X^%d) + ", combi, n-k);
	}
	printf("1(X^0)\n");
	return 0;
}
	
