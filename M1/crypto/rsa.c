#include <stdio.h>
#include <time.h>
#include <gmp.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int taille; //taille de l'entier n
  gmp_randstate_t state; // variable nécessaire pour le générateur aléatoire

 // récupération de la valeur de taille sur la ligne de commande
    taille = atoi(argv[1]);
 // initialisation du générateur aléatoire 
    gmp_randinit_default(state);
    gmp_randseed_ui(state,time(NULL));

/*A COMPLETER, la variable state est à utiliser dans toute fonction générant de l'aléatoire.*/

	// Déclarations et initialisations
	mpz_t p, p_moins1, q, q_moins1, n, phi_n, e, pgcd_e_phi_n, d, m, c, dechiffree;
	mpz_init(p);
	mpz_init(p_moins1);
	mpz_init(q);
	mpz_init(q_moins1);
	mpz_init(n);
	mpz_init(phi_n);
	mpz_init(e);
	mpz_init(pgcd_e_phi_n);
	mpz_init(d);
	mpz_init(c);
	mpz_init(m);
	mpz_init(dechiffree);
	

	// Trouver p et q deux grands nombres premiers.
	mpz_urandomb(p, state, taille/2);	
	mpz_urandomb(q, state, taille/2);	

	while(mpz_probab_prime_p(p, 30) == 0) {
		
		mpz_urandomb(p, state, taille/2);
	}


	while(mpz_probab_prime_p(q, 30) == 0) {
		
		mpz_urandomb(q, state, taille/2);	
	}

	// Calcul de n et phi_n
	mpz_sub_ui(p_moins1, p, 1);
	mpz_sub_ui(q_moins1, q, 1);

	mpz_mul(n, p, q);
	mpz_mul(phi_n, p_moins1, q_moins1);

	// Trouver e un grand nombre < phi_n et premier avec phi_n
	mpz_urandomm(e, state, phi_n);

	mpz_gcd(pgcd_e_phi_n, e, phi_n);
	while(mpz_cmp_ui(pgcd_e_phi_n, 1) != 0) {
		mpz_urandomm(e, state, phi_n);
		mpz_gcd(pgcd_e_phi_n, e, phi_n);
	}

	// Trouver d : l'inverse de e modulo phi_n
	mpz_invert(d, e, phi_n);	

	// Génration du message m.
	mpz_urandomb(m, state, taille);
	while(mpz_cmp(m, n) >= 0) {
		mpz_urandomb(m, state, taille);
	}

	// Génération du cryptogramme à partir de m.
	mpz_powm(c, m, e, n);

	// Vérification qu'après déchiffrement on retrouve le message d'origine.
	mpz_powm(dechiffree, c, d, n);
	
	
	// Affichage.
	gmp_printf("p : %Zd\n\n", p);
	gmp_printf("q : %Zd\n\n", q);
	gmp_printf("n : %Zd\n\n", n);
	gmp_printf("phi_n : %Zd\n\n", phi_n);
	gmp_printf("e : %Zd\n\n", e);
	gmp_printf("d : %Zd\n\n", d);
	gmp_printf("m : %Zd\n\n", m);
	gmp_printf("c : %Zd\n\n", c);
	gmp_printf("dechiffree : %Zd\n", dechiffree);
	
	if(mpz_cmp(m, dechiffree) == 0) {
		printf("\nRSA réussi !\n");
	}
	else {
		printf("\nRSA raté ...\n");
	}
	
	// Libération de la mémoire.
	mpz_clear(p);
	mpz_clear(q);
	mpz_clear(n);
	mpz_clear(phi_n);
	mpz_clear(p_moins1);
	mpz_clear(q_moins1);
	mpz_clear(e);
	mpz_clear(pgcd_e_phi_n);
	mpz_clear(d);
	mpz_clear(m);
	mpz_clear(c);
	mpz_clear(dechiffree);


	
	return 0;
}
