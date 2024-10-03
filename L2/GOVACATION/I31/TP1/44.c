#include <stdio.h>

int main() {

	int x = 1;
	int y = 1;
	int z = 1;
	
	printf(" ++x || (++y > z && (y*++z)) pour x = %d y = %d z = %d\n",x,y,z);
	printf("%d\n",++x || (++y > z && (y*++z)));

	x = -1;
	y = 1;
	z = 3;
	
	printf(" ++x || (++y > z && (y*++z)) pour x = %d y = %d z = %d\n",x,y,z);
	printf("%d\n",++x || (++y > z && (y*++z))); 

	x = -1;
	y = 1;
	z = 0;
	
	printf(" ++x || (++y > z && (y*++z)) pour x = %d y = %d z = %d\n",x,y,z);
	printf("%d\n",++x || (++y > z && (y*++z))); 

	return 0;
}
