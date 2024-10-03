#include <stdio.h>

int main() { 

	float x = 1.0;
	float y = 2.0;
	float z = 3.0;
	float u = 4.0;
	float v = 5.0;
	float w = 6.0;

	printf("%f %f %f %f",(x+2)/(y+4),x*(y+z*(3-u)),(x*y)/(v+2),u*(x*x*x)+v*(x*x)+w*x);

	return 0;
}

