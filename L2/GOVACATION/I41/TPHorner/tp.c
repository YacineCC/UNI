#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef unsigned int uint;

float naif_pow(uint x, uint n, uint *NbMul)
{	
	*NbMul = 0;
	int i;
	float resultat = 1;
	for(i = 0; i < n; i++)
	{
		resultat = resultat * x;
		*NbMul += 1;
	}

	return resultat;
}

float SM_pow(uint x, uint n, uint *NbMul)
{
	*NbMul = 0;
	float resultat = 1;
	float aux = x;
	while(n > 0)
	{
		if(n & 1)
		{	
			resultat = resultat * aux;
			*NbMul += 1;
		}
		aux = aux * aux;
		*NbMul += 1;
		n = n >> 1;

	}
	return resultat;
}

float Eval_naif(float *P, uint n, float a, uint *NbMulT)
{	
	*NbMulT = 0;
	uint *NbMul;
	*NbMul= 0; 
	int i;
	float resultat = 0;
	float pow;
	for(i = 0; i <= n; i++)
	{
		
		pow = naif_pow(a,i,NbMul);
		*NbMulT += *NbMul;
		*NbMul = 0;
		resultat += pow*P[i];

		
	}
	return resultat;
}
	


float Eval_SM(float *P, uint n, float a, uint *NbMulT)
{
	*NbMulT = 0;
	uint *NbMul;
	*NbMul= 0;
	int i;
	float resultat = 0;
	float pow;
	for(i = 0; i <= n; i++)
	{
		pow = SM_pow(a,i,NbMul);
		*NbMulT += *NbMul;
		*NbMul = 0;
		resultat += pow*P[i];
	}
	return resultat;


}


float Eval_Horner(float *P, uint n, float a, uint *NbMulT)
{
	*NbMulT = 0;
	int i;
	float resultat = 0;
	for(i = 0; i <= n; i++)
	{
		resultat = resultat * a + P[n-i];
		*NbMulT += 1;
	}
	return resultat;
}
	

float *Creer_Poly(uint n)
{
	int i;
	float *P = (float *)malloc((n+1)*sizeof(float));
	for(i = 0; i <= n; i++)
	{
		P[i] = random()%2 + 1;
	}
	
	return P;
}

void afficher_poly(float *P, uint n)
{
	int i;
	printf("[%f",P[0]);
	for(i = 1; i <= n; i++)
	{
		printf(", %f",P[i]);
	}
	printf("]\n");
}


int main(void)
{	

	srand(time(NULL));
	/*
	uint n = 100;
	float *P = Creer_Poly(n);
	afficher_poly(P,n);
	float a = 2;

	float resultat = Eval_naif(P, n, a, &NbMulT);
	printf("%f %hhu\n",resultat, NbMulT);

	resultat = Eval_SM(P, n, a, &NbMulT);
	printf("%f %hhu\n",resultat, NbMulT);

	resultat = Eval_Horner(P, n, a, &NbMulT);
	printf("%f %hhu\n",resultat, NbMulT);
	*/
	
	FILE *fichierNaif;
	FILE *fichierSM;
	FILE *fichierHorner;

	fichierNaif = fopen("fichierNaif.txt","w");
	fichierSM = fopen("fichierSM.txt","w");
	fichierHorner = fopen("fichierHorner.txt","w");
	
	uint NbMulNaif;
	uint NbMulSM;
	uint NbMulHorner;
	
	NbMulNaif = 0;
	NbMulSM = 0;
	NbMulHorner = 0;
	float *P;
	float a = 3;
	for(uint i = 0; i <= 100; i++)
	{
		P = Creer_Poly(i);
		//afficher_poly(P,i);			
		Eval_naif(P, i, a, &NbMulNaif);
		Eval_SM(P, i, a, &NbMulSM);
		Eval_Horner(P, i, a, &NbMulHorner);
		//printf("%hhu %hhu %hhu %hhu\n", NbMulNaif, NbMulSM, NbMulHorner, i);
		
		fprintf(fichierNaif,"%u %u\n", i, NbMulNaif);
		fprintf(fichierSM,"%u %u\n", i, NbMulSM);
		fprintf(fichierHorner,"%u %u\n", i, NbMulHorner);

		free(P);
		P = NULL;
		

		
	}
	
	fclose(fichierNaif);
	fclose(fichierSM);
	fclose(fichierHorner);
	
	return 0;
}
