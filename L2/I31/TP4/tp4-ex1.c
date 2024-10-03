#include <stdio.h>
void affiche(int t[], unsigned n) {
	int i = 1;
	printf("[");
	if (n > 0) {
		printf(" %d",t[0]);
		while (i<n){
			printf(", %d",t[i]);
			i ++;
		}
	}

	printf(" ]\n");
	
}

int main() {

	int t[] = {1,2,3,4,5};	
	affiche(t,5);
	return 0;	
}
