#include <stdio.h>

void main(void)

{
	int date;
	printf("Entrer une date sous format AAAA, MM, JJ\n");

	scanf("%d",&date);

	int jour = date % 100;

	int mois = (date / 100)  % 100;

	int annee = date / 10000;


	switch(mois)
	{
		case(1):
			printf("La date :\n%d janvier %d\n",jour, annee);
			break;

		case(2):

			printf("La date :\n%d février %d\n",jour, annee);
			break;

		case(3):
			printf("La date :\n%d mars %d\n",jour, annee);
			break;

		case(4):

			printf("La date :\n%d avril %d\n",jour, annee);
			break;
		case(5):
			printf("La date :\n%d mai %d\n",jour, annee);
			break;

		case(6):

			printf("La date :\n%d juin %d\n",jour, annee);
			break;

		case(7):
			printf("La date :\n%d juillet %d\n",jour, annee);
			break;

		case(8):

			printf("La date :\n%d aôut %d\n",jour, annee);
			break;
		case(9):
			printf("La date :\n%d septembre %d\n",jour, annee);
			break;

		case(10):

			printf("La date :\n%d octobre %d\n",jour, annee);
			break;
		case(11):
			printf("La date :\n%d novembre %d\n",jour, annee);
			break;

		case(12):

			printf("La date :\n%d décembre %d\n",jour, annee);
			break;
		default:
			printf("Mauvais format\n");
			
		}
								

}
