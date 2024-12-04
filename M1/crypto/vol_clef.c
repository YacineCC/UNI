#include <stdio.h>
#include <gmp.h>

int main() {
    mpz_t p, p_moins1,q, q_moins1, n, phi_n, d, e, c, dechifree;  //déclaration
    mpz_init(p);  // Initialisation de 'p'
    mpz_init(q);  // Initialisation de 'q'
    mpz_init(n);  // Initialisation de 'n'
    mpz_init(phi_n);  // Initialisation de 'n'
    mpz_init(p_moins1);  // Initialisation de 'n'
    mpz_init(q_moins1);  // Initialisation de 'n'
    mpz_init(d);  // Initialisation de 'n'
    mpz_init(e);  // Initialisation de 'n'
	mpz_init(c);
	mpz_init(dechifree);

    // Définir les valeurs de 'a' et 'b'
    mpz_set_str(p, "4aa55829181056994b47e8c26e3ed27780892a2679901510ab2769bcec3ea77f098a03d28be3c7834978d92ba57f74f19aff", 16);  // Base 16
    mpz_set_str(q, "f4197a54665c00d21df5ca59a6d8c1632b2c781e29284573d10dfcd0d06c251f858fcf5b86914a9858157a727c2e62e2fdadb", 16);  // Base 16


	mpz_set_str(c, "16b92f99d4cfcd5513e5cf5d0a1d5803a43bea28c0", 16);
	
	mpz_mul(n, p, q);


	mpz_sub_ui(p_moins1, p, 1);
	mpz_sub_ui(q_moins1, q, 1);
	mpz_mul(phi_n, p_moins1, q_moins1);


	mpz_add_ui(e, e, 3);

	// Calcul de d : l'inverse de e modulo phi_n
	mpz_invert(d, e, phi_n);


	// Déchiffrage de c.
	mpz_powm(dechifree, c, d, n);
	// Affichage
	printf("Clé publique : \n");
	gmp_printf("n : %Zx\n", n);
	gmp_printf("e : %Zx\n", e);


	printf("\n\nClé privée : \n");
	gmp_printf("p : %Zx\n", p);
	gmp_printf("q : %Zx\n", q);

	gmp_printf("phi_n : %Zx\n", phi_n);
	gmp_printf("d : %Zx\n", d);

	gmp_printf("dechifree : %Zx\n", dechifree);

    // Libérer la mémoire
    mpz_clear(p);
    mpz_clear(q);
    mpz_clear(n);
    mpz_clear(phi_n);
    mpz_clear(p_moins1);
    mpz_clear(q_moins1);
    mpz_clear(d);
    mpz_clear(e);
	mpz_clear(c);
	mpz_clear(dechifree);

    return 0;
}
