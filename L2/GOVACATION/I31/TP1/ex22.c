#include <stdio.h>

int main() {
	char c = 65;
	int i = 2;
	float f = 3.0;
	double d = 4.0;

	printf("c = %c i = %d f = %f d = %lf",c,i,f,d);

	c += 4;
	i += 4;
	f += 4;
	d += 4;


	printf("c = %c i = %d f = %f d = %lf",c,i,f,d);

	return 0;
}
