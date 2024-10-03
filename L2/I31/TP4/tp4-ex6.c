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

void swap(int t[], int a,int b) {
	int tmp;
	tmp = t[a];
	t[a] = t[b];
	t[b] = tmp;
}

void tri_bulle(int t[], unsigned n) {
	int mini;
	int j;
	int i = 0;
	int permute = 1;
	while(permute){
		permute = 0;
		j = 0;
		while(j < (n-(1+i))){
			if( t[j] > t[j+1] ){
				swap(t,j,j+1);
				permute = 1;
			}
		
			j ++;

		}
		i ++;
	}
		
}
void main() {
	
	int t[5];
	for(int i = 0; i < 5;i++){
		scanf("%d",&t[i]);
	}
	tri_bulle(t,5);

	affiche(t,5);
}
