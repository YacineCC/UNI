#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <string.h>


typedef unsigned int uint;
typedef unsigned long long ullong;
typedef unsigned char uchar;

typedef struct
{
	uint nbc;
	uint *chiffres;
}tnombre;

void affiche_nombre(tnombre *T)
{
	printf("[%u", T->chiffres[0]);
	for(int i = 1; i < T->nbc; i++)
	{
		printf(", %u", T->chiffres[i]);
	}
	printf("]\n");
}



uint logarithme(int n, uint base)
{
	uint logarithme = 0;

	while(n > 1)
	{
		logarithme++;
		n = n/base;
	}
	return logarithme;
}

tnombre *I2N(int n, uint base)
{
	tnombre *T = (tnombre *)malloc(sizeof(tnombre));
	T->nbc = floor(log(n)/log(base)) + 1;
	uint *chiffres = (uint *)malloc(sizeof(uint)*T->nbc);

	int x = n;
	int r = 0;
	int i = 0;
	

	while(i < T->nbc)
	{
		r = x % base;
		chiffres[i] = r;
		x = x/base;
		i++;
	}
	T->chiffres = chiffres;

	return T;
		

}


void destroy_nombre(tnombre *T)
{
	T-> nbc = 0;
	free(T->chiffres);
	T->chiffres = NULL;
	free(T);
	T = NULL;
}


ullong Factorielle(uchar n)
{
	uchar x = n;
	ullong fact = 1;
	while(x >= 1)
	{
		fact = fact*x;
		x--;
	}
	return fact;
}

tnombre *S2N(char *chaine)
{	
	uint len = strlen(chaine);
	tnombre *T = (tnombre *)malloc(sizeof(tnombre));
	uint *chiffres = (uint *)malloc(sizeof(uint)*len);
	int i = 0;
	while(i < len)
	{
		chiffres[i] = (uint)chaine[len-i-1]-48;
		
		i++;
	}
	T->nbc = len;
	T->chiffres = chiffres;
	return T;
}

char *N2S(tnombre *N)
{
	if( N == NULL)
		return "";
	char *S = (char *)malloc(sizeof(char)*N->nbc);
	if(N->chiffres[N->nbc-1] == 0)
		N->nbc--;
	
	for(int i = 0; i < N->nbc; i++)
	{
		S[i] = (char)(N->chiffres[N->nbc-i-1] + 48);
	}
	
	
	return S;
}

tnombre *Addition(tnombre *A, tnombre *B, uint base)
{
	tnombre *R = (tnombre *)malloc(sizeof(tnombre));
	R->nbc = (A->nbc > B->nbc) ? A->nbc +1 :  B->nbc +1;
	uint *chiffres = malloc(sizeof(uint)*R->nbc);
	
	uchar retenue = 0;
	uint test = 0;

	for(int i = 0; i < R->nbc; i++)
	{
		test = A->chiffres[i] + B->chiffres[i] + retenue; 
		if(test>= base)
		{
			retenue = 1;
			test = test - base;
		}
		else
		{
			retenue = 0;
		}	
		chiffres[i] = test;
	}
	R->chiffres = chiffres;
	return R;
}

tnombre *Multiplication(tnombre *A, tnombre *B, uint base)
{
	tnombre *R = (tnombre *)malloc(sizeof(tnombre));

	uint test = 	A->nbc+B->nbc;	
		 
	uint *chiffres = (uint *)calloc(test,sizeof(uint));

	R->nbc = test;
	uint retenue = 0;
	uint testi = 0;
	int i = 0;
	int j = 0;
	while(i < A->nbc)
	{
		j = 0;
		while(j < B->nbc)	
		{
			testi = A->chiffres[i]*B->chiffres[j] + retenue; 
			chiffres[i+j] += testi % base;
			retenue = testi / base;
			j++;
		}
		i++;
	}
	chiffres[i+j-1] = retenue;
	R->chiffres = chiffres;
	return R;
}

tnombre *FactMP(uint n)
{
	tnombre *fact = I2N(1,10);
	char *S;
	while(n > 1)
	{
		fact = 	Multiplication(fact, I2N(n,10), 10);
		S = N2S(fact);
		printf("%s\n", S);
		n--;
	}
	return fact;
}

int main(int argc, char** argv)
{
	/*
	tnombre *T = S2N(argv[1]);
	affiche_nombre(T);
	char *S = N2S(T);
	printf("%s\n", S);
	destroy_nombre(T);
	free(S);
	*/
	/*
	tnombre *A = S2N(argv[1]);
	tnombre *B = S2N(argv[2]);
	affiche_nombre(A);
	affiche_nombre(B);
	tnombre *R1 = Addition(A,B,2);
	tnombre *R2 = Multiplication(A,B,2);
	affiche_nombre(R1);
	affiche_nombre(R2);
	
	char *S1 = N2S(R1);
	printf("%s\n",S1);
	char *S2 = N2S(R2);
	printf("%s\n",S2);


	destroy_nombre(A);
	destroy_nombre(B);
	destroy_nombre(R1);
	destroy_nombre(R2);
	*/
	tnombre *fact = FactMP(10);
	destroy_nombre(fact);
	
	return 0;
}
