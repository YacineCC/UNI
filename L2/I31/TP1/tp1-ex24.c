#include <stdio.h>

int main()
{
	float x;
	float y;
	float z;
	float u;
	float v;
	float w;

	x = 1.0;
	y = 2.0;
	z = 3.0;
	u = 4.0;
	v = 5.0;
	w = 6.0;

	float expr1;
	float expr2;
	float expr3;
	float expr4;

	expr1 = (x+2)/(y+4);
	expr2 = x*(y+z*(3-u));
	expr3 = (x*y)/(v+2);
	expr4 = u*(x*x*x) + v*(x*x)+(w*x);

	printf("(x+2)/(y+4) = %f\n",expr1);
	printf("x*(y+z(3-u)) = %f\n",expr2);
	printf("(x*y)/(v+2) = %f\n",expr3);
	printf("u*(x*x*x) + v*(x*x)+(w*x) = %f\n",expr4);
}
