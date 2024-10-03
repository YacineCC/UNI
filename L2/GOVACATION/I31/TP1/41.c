#include <stdio.h>

int main() {

	int date;

	scanf("%d",&date);

	int annee = date / 10000;

	int mois = (date / 100) % 100;

	int jour = date % 100;


	switch(mois) {

		case 1:
			printf("%d Janvier %d\n",jour,annee);
			break ;
		case 2:
			printf("%d Fevrier %d\n",jour,annee);
			break ;
		case 3:
			printf("%d Mars %d\n",jour,annee);
			break ;
		case 4:
			printf("%d Avril %d\n",jour,annee);
			break ;
		case 5:
			printf("%d Mai %d\n",jour,annee);
			break ;
		case 6:
			printf("%d Juin %d\n",jour,annee);
			break ;
		case 7:
			printf("%d Juillet %d\n",jour,annee);
			break ;
		case 8:
			printf("%d Août %d\n",jour,annee);
			break ;
		case 9:
			printf("%d Septembre %d\n",jour,annee);
			break ;
		case 10:
			printf("%d Octobre %d\n",jour,annee);
			break ;
		case 11:
			printf("%d Novembre %d\n",jour,annee);
			break ;
		case 12:
			printf("%d decembre %d\n",jour,annee);
			break ;
							
		default :
			printf("Date invalide\n");
	}			
	
	return 0;
}
