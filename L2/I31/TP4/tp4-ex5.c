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
	while(permute)
		permute = 0;
		mini = t[0];
		j = i;
		while(j < n){
			if( t[j] < mini){
				swap(t,i,j);
				permute = 1;
			}
			j ++;
		}
		i ++;
}
void tri_selection(int t[], unsigned n) {
	int mini;
	int j;
	int i = 0;
	while(i < n){
		mini = i;
		j = i+1;
		while(j < n){
			if( t[j] < t[mini]){
				mini = j;
			}
		j ++;

		}
		swap(t,i,mini);
		i ++;
	}

}


void main() {
	
	int t[5];
	for(int i = 0; i < 5;i++){
		scanf("%d",&t[i]);
	}
	tri_selection(t,5);

	affiche(t,5);
}
