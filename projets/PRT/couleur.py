from __future__ import annotations
from vecteur import Vecteur
from point import Point

class Couleur():
    """ Une couleur est un triplet (R, V, B) appartient à [0, 1]^3, on y a
    ajouté des méthodes pour le mélange de couleurs, au final chaque couleurs de
    notre matrice sera transformé en simple tuple pour être utilisé par la
     bibliothèque PIL."""
    def __init__(self, r, v, b) -> None:
        self.r = r
        self.v = v
        self.b = b

    
    def prod_comp(self, c2):
        """ Produit composante à composante, utile pour l'illumination de Phong.
        """
        return Couleur(self.r * c2.r, self.v * c2.v, self.b * c2.b)
    


    """ Les méthodes suivantes sont des méthodes spéciales de surchage
    d'opérateurs. On aura l'addition et la soustraction de deux couleurs,
    la multiplication et la division d'une couleur par un coefficient.
    Toutes ces méthodes renvoient une nouvelle couleur."""

    def __add__(self, c2) :

        r = self.r + c2.r
        v = self.v + c2.v
        b = self.b + c2.b
        return Couleur(r, v, b)
    
    def __sub__(self, c2):

        r = self.r - c2.r
        v = self.v - c2.v
        b = self.b - c2.b
        return Couleur(r, v, b)
    
    def __neg__(self):

        r = -self.r
        v = -self.v
        b = -self.b
        return Couleur(r, v, b)
    
    def __mul__(self, k):

        r = self.r * k
        v = self.v * k
        b = self.b * k
        return Couleur(r, v, b)
    
    def __rmul__(self, k):

        r = self.r * k
        v = self.v * k
        b = self.b * k
        return Couleur(r, v, b)
    
    def __truediv__(self, k):
        r = self.r / k
        v = self.v / k
        b = self.b / k
        return Couleur(r, v, b)

    
    def __str__(self) -> str:
        """ Méthode spéciale pour pouvoir print une couleur."""
        return f'({self.r}, {self.v}, {self.b})'

ROUGE = Couleur(1, 0, 0)
VERT = Couleur(0, 1, 0)
BLEU = Couleur(0, 0, 1)
BLANC = Couleur(1, 1, 1)
NOIR = Couleur(0, 0, 0)
VIOLET = Couleur(1, 0, 1)
JAUNE = Couleur(1, 1, 0)

if __name__ == "__main__":

    test = Couleur(0.5, 0.3, 0.8)

    print(test)