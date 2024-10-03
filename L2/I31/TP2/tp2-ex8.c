#include <stdio.h>

void main(void) {

	int factN = 1,factK = 1,factNK = 1,i,j,NK,combi;
	int n;
	int k = 0;
	int k1;
	
	printf("saisir une  puissance n :\n");
	scanf("%d",&n);

	j = 0;
	if(n == 0)
		factN = 1;
	else {
		while(j<n) {
			factN *= (n-j);
			j++;
		}
	}
		
	
	for(k;k<n;k++){
		switch(k) {
			
			case 0:
				factK = 1;
				break;
			
				
			default:
				factK = 1;
				j = 0;
				while(j<k) {

					factK *= (k-j);
					j++;
				break;	
				}
		}
		NK = n - k;
		switch(NK) {
			
			case 0:
				factNK = 1;
				break;
			
				
			default:
				factNK = 1;
				j = 0;
				while(j<NK) {

					factNK *= (NK-j);
					j++;
				break;	
				}

		}


		
		combi = factN/(factK*factNK);
	

		printf("%d x^%d + ",combi,n);
		n--;

	}

}
