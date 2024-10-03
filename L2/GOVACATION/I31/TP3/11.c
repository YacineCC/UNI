#include <stdio.h>

int saisie_date(unsigned int* j, unsigned int* m, unsigned int* a) {
	

	if((*j > 31) || ((*m > 12))) {
		printf("Erreur saisie");
		return 0;
		}
	printf("%u/%u/%u\n", *j, *m, *a);
	return 1;
}

int main() {
	
	unsigned int j, m, a;
	printf("Saisir la date sous le format jj mm aaaa : ");
	scanf("%u %u %u", &j, &m, &a);
	saisie_date(&j, &m, &a);
	
	return 0;
}
