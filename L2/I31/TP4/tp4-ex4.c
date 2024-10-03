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

void inverse(int t[], unsigned n) {

	int i = 0;
	int tmp;
	while (i < n/2) {
		tmp = t[n-(1+i)];
		t[n-(1+i)] = t[i];
		t[i] = tmp;
		i ++;
	}

}

void main() {
	
	int t[5];
	for(int i = 0; i < 5;i++){
		scanf("%d",&t[i]);
	}
	inverse(t,5);

	affiche(t,5);
}
