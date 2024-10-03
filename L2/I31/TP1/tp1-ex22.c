#include <stdio.h>

int main()
{
	char c;
	int i;
	float f;
	double d;

	c = 65;
	i = 2;
	f = 3.0;
	d = 4.0;

	printf("c=%c, i=%d, f=%f, d=%lf\n", c,i,f,d);

	c = c + 4;
	i = i + 4;
	f = f + 4;
	d = d + 4;
	printf("c=%c, i=%d, f=%f, d=%lf\n", c,i,f,d);
	
}
