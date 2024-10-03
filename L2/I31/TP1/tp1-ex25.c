#include <stdio.h>

int main()
{
	int a;
	int b;

	int expr;
	a = 0;
	b = 0;

	expr = (a && (!b)) || ((!a) && b);

	printf("a et non b ou non a et b\n");
	printf("Pour a = %d et b = %d\n",a,b);
	printf("%d\n",expr);

	a = 1;
	b = 0;
	
	expr = (a && (!b)) || ((!a) && b);	
	printf("a et non b ou non a et b\n");
	printf("Pour a = %d et b = %d\n",a,b);
	printf("%d\n",expr);
	
	a = 0;
	b = 1;
	
	expr = (a && (!b)) || ((!a) && b);	
	printf("a et non b ou non a et b\n");
	printf("Pour a = %d et b = %d\n",a,b);
	printf("%d\n",expr);
	
	a = 1;
	b = 1;
	
	expr = (a && (!b)) || ((!a) && b);	
	printf("a et non b ou non a et b\n");
	printf("Pour a = %d et b = %d\n",a,b);
	printf("%d\n",expr);







}
