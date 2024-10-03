#include <stdio.h>

void main(void)
{
	printf("Evaluation de l'expression ++x || (++y > z && (y*++z))\n");

	int x,y,z;

	int expr;

	x = 1;
	y = 1;
	z = 1;
	expr =  ++x || (++y > z && (y*++z));
	printf("Pour x = %d y = %d z = %d expr = %d\n",x,y,z,expr);

	x = -1;
	y = 1;
	z = 3;
	expr =  ++x || (++y > z && (y*++z));
	printf("Pour x = %d y = %d z = %d expr = %d\n",x,y,z,expr);

	x = -1;
	y = 1;
	z = 0;
	expr =  ++x || (++y > z && (y*++z));
	printf("Pour x = %d y = %d z = %d expr = %d\n",x,y,z,expr);

}
