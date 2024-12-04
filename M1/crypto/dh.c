#include <stdio.h>
#include <time.h>
#include <gmp.h>

int main(int argc, char *argv[])
{  
  gmp_randstate_t state; // variable nécessaire pour le générateur aléatoire
 
 // initialisation du générateur aléatoire 
    gmp_randinit_default(state);
    gmp_randseed_ui(state,time(NULL));

/*A COMPLETER, la variable state est à utiliser dans toute fonction générant de l'aléatoire.*/


	// Déclaration et initialisation des variables.
	// g_x : g ** x 
	mpz_t  y, g, p, p_moins2,g_x, g_y, g_xy;
	mpz_init(y);
	mpz_init(g);
	mpz_init(p);
	mpz_init(p_moins2);
	mpz_init(g_x);
	mpz_init(g_y);
	mpz_init(g_xy);

	mpz_set_str(p, "180976037326066581250015884868681568805219516166611511531052524875062481337487", 10);
	mpz_set_ui(g, 5);
 	mpz_set_str(g_x, "104179239409769252679221162390810469162114082195780656990465463720674086918823", 10);
	mpz_sub_ui(p_moins2, p, 2);
	mpz_urandomm(y, state, p_moins2);

	// Ce qui sera envoyé à Alice.
	mpz_powm(g_y, g, y, p);

	// La clef partagée.
	mpz_powm(g_xy, g_x, y, p);
	
	// Affichage des variables.
	gmp_printf("g : %Zd\n", g);
	gmp_printf("p : %Zd\n", p);
	gmp_printf("g_x : %Zd\n", g_x);
	gmp_printf("g_y : %Zd\n", g_y);
	gmp_printf("g_xy : %Zd\n", g_xy);


	// Libération de la mémoire.
	mpz_clear(y);
	mpz_clear(g);
	mpz_clear(p);
	mpz_clear(p_moins2);
	mpz_clear(g_x);
	mpz_clear(g_y);
	mpz_clear(g_xy);

	return 0;
}
