#include <stdio.h>
int somme(int t[], unsigned n) {

	int i = 0;
	int som = 0;
	while (i < n) {

		som += t[i];
		i ++;
	}

	return som;
}

int main() {

	int a1,a2,a3,a4,a5;
	printf("Saisir les elements du tableau \n");
	scanf("%d %d %d %d %d", &a1,&a2,&a3,&a4,&a5);
	int t[] = {a1,a2,a3,a4,a5};
	printf("%d \n",somme(t,5));
}
