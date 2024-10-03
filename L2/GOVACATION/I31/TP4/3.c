#include <stdio.h>
#include <limits.h> //pour INT_MIN et INT_MAX
#define N 5

void extremum(int t[], unsigned n, int* min, int* max) {
	*min = INT_MAX;
	*max = INT_MIN;
	for(int i = 0; i < n; i++) {
		if(t[i] < *min) *min = t[i];

		if(t[i] > *max) *max = t[i];
	}
}

int main() {
	int t[N];
	int min, max;
	
	for(int i = 0; i < N; i++) {
		printf("Element %d/%d : ", i+1, N);
		scanf("%d", &t[i]);
	}
	extremum(t, N, &min, &max);
	printf("\nMinimum tableau: %d\n", min);
	printf("\nMaximum tableau: %d\n", max);
}
