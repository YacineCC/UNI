#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int* creation_serie(unsigned int n) {

	int* ptr= NULL;
	ptr = (int*) malloc(sizeof(int)*n);
	return ptr;

}

void affiche_serie(int* s, unsigned int n) {
	printf("[");
	if (n > 0) {
		printf("%d",s[0]);
		for(int i = 1; i < n; i++) {

			printf(", %d",s[i]);
		}
	}
	printf("]\n");
}

void destruction_serie(int** ps) {
	free(*ps);
	ps = NULL;
}

float moyenne(int* s, unsigned int n) {
	int som = 0;
	for(int i = 0; i < n; i++) {
		som += s[i];
	}
	float moy = (float) som/n;
	return moy;
}
		
float variance(int* s, unsigned int n) {
	float moy = moyenne(s,n);
	int som = 0;
	for(int i= 0; i < n; i++) {
		som += (s[i]-moy)*(s[i]-moy);
	}

	return (float) som/n;

	

}

int* tri_croissant(int* s, unsigned int n) {
	int j;
	int tmp;
	int x;
	for(int i = 1; i<n;i++){
		x = s[i];
		j = i;	
		while((j > 0) && (s[j-1] > x)) {
			s[j] = s[j-1];
			j --;
		}
		s[j] = x;
	}

}

float mediane(int* s, unsigned int n) { 
	tri_croissant(s,n);
	n = n - 1;
	if(n % 2 == 0){
		return s[n/2];
	}
	else{
		return s[(n+1)/2];
	}
}
int main() {
	int* ptr= NULL;
	int n = 5;
	ptr = creation_serie(n);
	int i = 0;
	for(i;i<n;i++) {

		scanf("%d",&ptr[i]);
	}

	affiche_serie(ptr, n);
	float moy;
	moy = moyenne(ptr,n);
	printf("Moyenne : %.3f\n",moy);
	float varian = variance(ptr,n);
	printf("Variance : %.3f\n",varian);
	tri_croissant(ptr,n);
	affiche_serie(ptr,n);
	printf("Medianne : %f\n",mediane(ptr,n));
	destruction_serie(&ptr);
	return 0;

}
