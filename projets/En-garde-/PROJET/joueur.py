from cartes import *
from plateau import *


class Joueur:
    case = -1 #pour savoir l'indice du joeur dans la piste

    def __init__(self, nom, idjoueur, pioche):
        """initialise un joueur avec son nom son id (1 ou 2) et sa main de départ"""
        self.nom = nom
        self.idjoueur = idjoueur
        self.score = 0
        self.main = Deck(pioche)




    def avancer(self, carte, plateau):
        """fait avancer le joueur sur la piste puis défausse"""
        print("c=",carte.valeur)
        plateau.piste[self.case] = 0
        if self.idjoueur == 1:
            self.case += carte.valeur
        if self.idjoueur == 2:
            self.case -= carte.valeur
        plateau.piste[self.case] = self.idjoueur
        self.deffausser(carte)

        


if __name__ == "__main__":
    c = Carte(1)
    p = Pioche()
    j = Joueur("coc", 1, p)
    print(j.nom)
