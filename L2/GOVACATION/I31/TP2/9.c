#include <stdio.h>

int main() {
	int i;
	int n, x, y;
	printf("Saisir le binôme (x+y) et sa puissance n : ");
	scanf("%d %d %d", &x, &y, &n);
	int k = 0; int som = 0;
	int FactN, FactK, FactNK,combi, puissx,puissy;
	for(k; k <= n; k++) {
		
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
		

		i = 0;
		puissx = 1;
		for(i; i < (n-k); i++) {

			puissx *= x;
		}

		i = 0;
		puissy = 1;
		for(i; i < k; i++) {

			puissy *= y;
		}


		som += combi * puissx * puissy;	
	}
	printf("(%d + %d)^%d = %d\n", x, y, n, som);
	return 0;
}
	
