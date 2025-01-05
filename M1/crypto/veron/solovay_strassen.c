#include <stdio.h>
#include <time.h>
#include <gmp.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int t; //parametre pour la probabilite
  mpz_t n; // entier a tester
  mpz_t a; // nombre aléatoire
  mpz_t exp; // exposant n-1//2
  mpz_t n_moins1;
  mpz_t jacobi_test; // jacobi "partie droite de l'égalité"
  mpz_t a_pow_exp; // a^((n-1)//2) "partie gauche de l'égalité"
  gmp_randstate_t state; // variable nécessaire pour le générateur aléatoire

 // on teste si le nombre de parametres d'appels est correct
    if (argc < 3)
    {
        printf("Usage : ./solovay_strassen t n\n");
        exit(-1);
    }
 // récupération de la valeur de t sur la ligne de commande
    t = atoi(argv[1]);
 // récupération de la valeur de n sur la ligne de commande  
    mpz_init(n);
    mpz_set_str(n,argv[2],16);
    //mpz_set_str(n,argv[2],10);   
 // initialisation du générateur aléatoire 
    gmp_randinit_default(state);
    gmp_randseed_ui(state,time(NULL));

    gmp_printf("%Zd\n",n);

/*A COMPLETER, la variable state est à utiliser dans toute fonction générant de l'aléatoire.*/
  

    // Déclarations et initialisations
    mpz_init(a);
    mpz_init(exp);
    mpz_init(n_moins1);
    mpz_init(jacobi_test);
    mpz_init(a_pow_exp);


    int jacobi;
    mpz_sub_ui(n_moins1, n, 1);

    // Calcul de l'exposant (n-1 // 2)
    mpz_cdiv_q_ui(exp, n_moins1, 2);

	
    for(int i = 0; i < t; i++) {
        // a une valeur aléatoire entre 1 et n-1 (si on tombe sur 0 on recommence pour l'exclure)
	    mpz_urandomm(a, state, n);
        while(mpz_cmp_ui(a, 0) == 0) {
            mpz_urandomm(a, state, n);
    }

    // Calcul du symbole de Jacobi
	jacobi = mpz_jacobi(a, n);

    // Partie droite de l'égalité
    // Si le symbole de Jacobi est égale à -1 on calcul -1 mod n c'est à dire n-1
	if (jacobi == -1)
	    mpz_sub_ui(jacobi_test, n, 1);
	else
        //sinon on met simplement 1
		mpz_set_ui(jacobi_test, 1);
	

    // Calcul de a^(n-1)/2 mod n
	mpz_powm(a_pow_exp, a, exp, n);


    // Test de Solovay-Strassen : symbole de jacobi (a/n) = a^(n-1)/2 mod n
    // Si les deux valeurs sont différentes alors n est composé
	if (mpz_cmp(jacobi_test, a_pow_exp) != 0){
		printf("n est composé\n");
        return 0;
    }





    }
    // Si après t itérations le symbole de jacobi mod n est toujours égale à a^(n-1)/2 mod n
    // alors n est probablement premier avec une probabilité de faux positif bornée par 2^-t
    printf("n est probablement premier avec une probabilité de faux positif bornée par 2^-%d\n", t);


    // Libération de la mémoire
    mpz_clear(n);
    mpz_clear(a);
    mpz_clear(exp);
    mpz_clear(n_moins1);
    mpz_clear(jacobi_test);
    mpz_clear(a_pow_exp);
    gmp_randclear(state);

    return 0;
}
