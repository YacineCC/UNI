#include <stdio.h>

float inverse(float n) {

	if(n != 0) 
		return(1/n);

	return n;
}

int main() {

	float n;
	printf("Saisir le réel que vous voulez inverser : ");
	scanf("%f", &n);

	printf("%f\n", inverse(n));

	return 0;
}
