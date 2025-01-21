#include <stdio.h>
#include <time.h>
#include <gmp.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int k; //parametre pour la probabilite
  
  int flag = 1;
  mpz_t n; // entier a tester
  mpz_t n_moins1; // n-1
  mpz_t aux; // variable auxiliaire initialisée à n-1
  mpz_t a; // nombre aléatoire
  mpz_t un;
  mpz_t a_pow_t; // a^t
  mpz_t two_pow_i; // 2^i
  mpz_t two_pow_i_xt; // 2^i * t
  mpz_t cal; // a^((2^i)*t)

  

 // on teste si le nombre de parametres d'appels est correct
    if (argc < 3)
    {
        printf("Usage : ./miller_rabin t n\n");
        exit(-1);
    }
 // récupération de la valeur de t sur la ligne de commande
    k = atoi(argv[1]);
 // récupération de la valeur de n sur la ligne de commande  
    mpz_init(n);
    mpz_set_str(n,argv[2],16);
    //mpz_set_str(n,argv[2],10);   
 // initialisation du générateur aléatoire 
    gmp_randstate_t state;        // variable nécessaire pour le générateur aléatoire
    gmp_randinit_default(state);
    gmp_randseed_ui(state,time(NULL));


/*A COMPLETER, la variable state est à utiliser dans toute fonction générant de l'aléatoire.*/
  

    // Déclarations et initialisations
    mpz_init(a);
    mpz_init(aux); // t
    mpz_init(n_moins1); // n-1
    mpz_init(un);
    mpz_init(two_pow_i); // 2^i
    mpz_init(two_pow_i_xt); // 2^i * t
    mpz_init(a_pow_t); // a^t
    mpz_init(cal); // a^((2^i)*t)


    mpz_set_ui(un, 1);
    // Initialisation des variables auxiliaires à n-1
    mpz_sub_ui(aux, n, 1);
    mpz_sub_ui(n_moins1, n, 1);

    
    // Calcul de s et de t (ici dans aux)
    // TQ il y a des bits de poids faible = à 0 dans aux on fait aux = aux >> 1
    int s = 0;
    while(mpz_tstbit(aux, 0)) {
        mpz_cdiv_q_2exp(aux, aux, 1); // aux = aux >> 1
        s++;
    }

	
    // Chaque tour de la boucle k fait diminuer la probabilité de dire qu'un nombre est premier alors qu'il ne l'est pas.
    for(int j = 0; j < k; j++) {
        // a une valeur aléatoire entre 2 et n-1 (si on tombe sur 0 ou 1 on recommence pour les exclures)
	    mpz_urandomm(a, state, n);
        while(mpz_cmp_ui(a, 0) == 0 || mpz_cmp_ui(a, 1) == 0) {
            mpz_urandomm(a, state, n);
        }

        // Calcul des tous les a^((2^i)*t) pour tout i compris entre 1 et n-1
        flag = 1;
        for(int i = 1; i < s; i++) {
            
            mpz_mul_2exp(two_pow_i, un, i); // 2^i (1 << i)
            mpz_mul(two_pow_i_xt, two_pow_i, aux); // 2^i * t
            mpz_powm(cal, a, two_pow_i_xt, n); // a^(2^i * t)
            
            // Pour que le nombre soit composé il faut que tous les a^((2^i)*t) soit différent de -1 mod n (ici n-1)
            if(mpz_cmp(cal, n_moins1) == 0)
                flag = 0;
          
        
        }

        mpz_powm(a_pow_t, a, aux, n); // a^t

        // Si a^t != 1 et a^t != 1 et pour tous i compris entre 1 et n-1, a^((2^i)*t) différent de -1 mod n, alors n est composé
        if(mpz_cmp_ui(a_pow_t, 1) != 0 && mpz_cmp(a_pow_t, n_moins1) != 0 && flag) {

                printf("\nn est composé. \n");
                // Libération de la mémoire.
                mpz_clear(n);
                mpz_clear(a);
                mpz_clear(aux);
                mpz_clear(n_moins1);
                mpz_clear(two_pow_i);
                mpz_clear(two_pow_i_xt);
                mpz_clear(a_pow_t);
                mpz_clear(un);
                // mpz_clear(state); //pour ne pas avoir de fuites mémoire mais cause un warning à la compilation
                printf("\n\nDans la liste donnée à http://veron.univ-tln.fr/M2/primes.html \nLes entiers numéro 3, 5, 7, 9, 10 de la liste sont probablement premier testé avec k = 15 donc une probabilité de mauvaise réponse bornée par 2^-30.\nRésulats confirmés par SageCell !\n\n");

                return 0;

        }
    }
    

    printf("\nn est probablement premier avec une probabilité de faux positif bornée par 1/4^%d\n", k);

    // Libération de la mémoire.
    mpz_clear(n);
    mpz_clear(a);
    mpz_clear(aux);
    mpz_clear(n_moins1);
    mpz_clear(two_pow_i);
    mpz_clear(two_pow_i_xt);
    mpz_clear(a_pow_t);
    mpz_clear(un);
    // mpz_clear(state); //pour ne pas avoir de fuites mémoire mais cause un warning à la compilation

    printf("\n\nDans la liste donnée à http://veron.univ-tln.fr/M2/primes.html \nLes entiers numéro 3, 5, 7, 9, 10 de la liste sont probablement premier testé avec k = 15 donc une probabilité de mauvaise réponse bornée par 2^-30.\nRésulats confirmés par SageCell !\n\n");
    return 0;

    /*
    Dans la liste donnée à http://veron.univ-tln.fr/M2/primes.html 
Les entiers numéro 3, 5, 7, 9, 10 de la liste sont probablement premier testé avec k = 15 donc une probabilité de mauvaise réponse bornée par 2^-30.
Résulats confirmés par SageCell !

test N° 1 : 10f69c9fd992994ea4ee0ba15db392a6bc3a2bc2e41668e4f457902e36daebc27db3e435ee2295e76ca9304a1486821892247acbd2c5db932c7a5628af42367a703712792ed58612d9de8ba6f621a5128def4a944d6efeae4196770b32ead100e74c978099159d131e89d3f4041694fc46994ee87d72f7e96d8a35ff0ad

n est composé

test N°2 : 12c5b3fb0a194847006399177be7abbeb8b7f0bb66ff24fe199756d1cfd28f639b210fdd62f2ee92bf3c225ad846b4d69412103958096270089b8cb3c0e421fd2b03f7dbd0d375b45cd7b1b0f6ac8caca766d3be874d74480cd9a2af479eca68e922526ce9132a09cf492a11860c858730f96ca7d1c531f501c2efc6e57

n est composé

test N°3 :
16aea18f3db9680fad21cfd6b10c8d7ba79dbdb54de3dbe7c124cb89c4f4e8789347fc5eaf0d2a29fc03d523d2a26ebc3e437bdb0f89e80731ac86c77df13735126fc4ed701291ec48662ec61f28dc6f5054da2eba08837ab3e6f44ccd33d13c96454d481384ffef766cc2f9cde12c06740bbb7e7bbad111040374b65ff

n est probablement premier avec une probabilité de faux positif bornée par 1/4^15

test N°4:
1526aa01fa5c319302fe0667c196b275193ae8ed399503ee8a5eaf47d7f303ff69340680e97eafacd785b6293529d8e5973d3454db376c941907e6929ba5a8b29764a91c9cb5d3544a22876641a45ae7b366a8ba4d29113a4a0c53bd3c8085353c36a594d0eda9da979c3f985c3a7965d7ffe458f28daadef9193f558b3

n est composé

test N°5:
1997ac7dd6b8a28685e62f035de43a531630235d69569bba58678a0449d68718fa9d67d59fdf6c785cab7d0e19e521f9b0050f865531c29d8bdcbab4496e85626c21e79b2156e70d708c296cf78c481366089ce194072d89966a8bd6ff9f1ffbddcc561b38b5ca844013666750c22e44034bb51e6d76fb2eb903529dde7

n est probablement premier avec une probabilité de faux positif bornée par 1/4^15

test N°6:
1dc2b71b6bb476ca77ae200043932253947b04e9bdc5d37283569ab16ebf426bb0f690430f12e7f5bc6c45723a577547dda6ad792b8e433ac687cf2b78fe5187f8d78dae3ba35fb36a70eab11950ce78a464fd78ad66f21c83d6e175db4c3ce6f21e86795e1ef55aa3eca8d523d7279e240a83c56e0e30ea5d6e27106ba

n est composé

test N°7:
1dcd2cb7a891a05f1ef6d4420eae5963fe8fa672fcdb88a679b3705d7f9ee2f5d322855d23b94e0329eed5bdb91f8b32a9a6e2424ee53f40c5319838585c9f537b191e2af36449ec8e3b3a98414ab9ecfcd6339d5fedc0c1d916f2268c6add16bc2b1738c51eae1c8665570acd6eb1f2943307900bfab7d01c7658d55c1

n est probablement premier avec une probabilité de faux positif bornée par 1/4^15

test N°8:
14fb6d917c6047a94dfcb5eba4e6031f6b035eb0c4aee1e78b46b207a965bb26de2c601f39378690a1e02bb334b16d8b5b0bc940c9d78e5e6a060ea5edd66152387cb57ce930957a0f3dff547dce4804f8d50b91a9355f6d714fb74a6df457a09c2b4c76904bfad0246691d21204a78377cf2996847f5968a9b88157f46

n est composé

test N°9:
14c51ed74f6c97c20139c01568ab4ceb771f17c1ac7d8db3d9446cc275a2952bde8b7d10095a38eab12268d2d3784430c479dae11eff1dca1b469ebbb7fa94851eb75d14a9ecbf5f3316b0add136a69d176373c9067238adbe62f11cb4658af2c3859c1044526f5e390034fe6e1ead3d460010996f167c2e1d9bf47c8d3

n est probablement premier avec une probabilité de faux positif bornée par 1/4^15

test N°10:
184cd23b0b3aad8b808b30a4ed43ba7f9db5ed1a05afa467ee7d157115bfd19d1b965ac5b5c7731bf57dfb14956a3e9691cbeae5ae3363cb880559c2daccb20a40bd1345b2fc84f43fb46c061917792d9490448cfa194ed725d523ac43c16a6d0b1967081f4f8d638731074a6393ccf765a841dbea14377f7fe23338e2b

n est probablement premier avec une probabilité de faux positif bornée par 1/4^15


    */
}