#include <stdio.h>

int main() {

	int a,b,expr;

	a = 0;
	b = 0;

	expr = (a && (!b)) || ((!a) && b);
	printf("%d",expr);

	a = 0;
	b = 1;

	expr = (a && (!b)) || ((!a) && b);
	printf("%d",expr);
		
	a = 1;
	b = 0;

	expr = (a && (!b)) || ((!a) && b);
	printf("%d",expr);

	a = 1;
	b = 1;


	expr = (a && (!b)) || ((!a) && b);
	printf("%d",expr);

	return 0;
}
