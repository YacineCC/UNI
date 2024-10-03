#include <stdio.h>

void extremum(int t[], unsigned n, int* min, int*max) {
	*min = t[0];
	*max = t[0];
	int i = 0;
	while(i<n) {

		if (t[i] < *min)
			*min = t[i];

		else if (t[i] > *max)
			*max = t[i];

		i ++;
	}
	printf("Min = %d Max = %d\n",*min,*max);
}
int main() {
	int a1,a2,a3,a4,a5;
	int min,max;
	scanf(" %d %d %d %d %d",&a1,&a2,&a3,&a4,&a5);
	int t[] = {a1,a2,a3,a4,a5};
	extremum(t,5,&min,&max);

}
