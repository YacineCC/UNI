#include <stdio.h>

int main() {

	int a;
	int b;
	char op;
	char test = 'Y';
	while(test == 'Y') {
	
		printf("Entrer une expression de la forme : a op b. (op E {+,-,*,/,%%})\n");	
		scanf("%d %c %d", &a, &op, &b);

		switch(op) {

			case '+' :

				printf("%d + %d = %d \n", a, b, a + b);
				break;
			case '-' :

				printf("%d - %d = %d \n", a, b, a - b);
				break;
			case '*' :

				printf("%d * %d = %d \n", a, b, a * b);
				break;
			case '/' :

				printf("%d / %d = %d \n", a, b, a / b);
				break;
			case '%' :

				printf("%d %% %d = %d \n", a, b, a % b);
				break;
			
			default:
				printf("erreur\n");
		}
		
		printf("Continue (Y/N) ?\n");
		getchar();
		scanf("%c",&test);
	}
	return 0;
}
