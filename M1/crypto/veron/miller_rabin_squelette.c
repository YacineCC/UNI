#include <stdio.h>
#include <time.h>
#include <gmp.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
  int k;                        //parametre pour la probabilite
  mpz_t n;                      // entier a tester
  mpz_t nmu;                    // pour le calcul de n-1
  mpz_t t;                      // pour la decomposition n-1 = 2^s*t
  gmp_randstate_t state;        // variable nécessaire pour le générateur aléatoire

  unsigned long decalage;
  unsigned long s;

  // on teste si le nombre de parametres d'appels est correct
  if (argc < 3)
    {
      printf ("Usage : ./miller_rabin k n\n");
      exit (-1);
    }

  // initialisation du générateur aléatoire 
  gmp_randinit_default (state);
  gmp_randseed_ui (state, time (NULL));

  // récupération de la valeur de t sur la ligne de commande
  k = atoi (argv[1]);

  // récupération de la valeur de n sur la ligne de commande  
  mpz_init (n);
  mpz_set_str (n, argv[2], 16);

// calcul de n-1
  mpz_init (nmu);
  mpz_sub_ui (nmu, n, 1);

  mpz_init(t);
  s = 0;
  decalage = 1;  //sera utilisé pour mpz_mul_2exp, pour trouver s et t tel que n-1=2^s*t

/*A COMPLETER, la variable state est à utiliser dans toute fonction générant de l'aléatoire.*/
}
