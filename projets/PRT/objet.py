from __future__ import annotations
from couleur import Couleur
from point import Point
from vecteur import Vecteur
from materiaux import Materiaux

class Objet:
    """ Métaclasse qui sert à créer nos sphères, plans et parallélépipèdes.
    Chaque objets aura sa méthode d'intérsection et de normale propre."""


    def __init__(self, pos : Point, couleur : Couleur, materiaux : Materiaux):
        self.position = pos 
        self.couleur = couleur
        self.materiaux = materiaux

    def __str__(self) -> str:
        return f'position : {self.position}\n couleur {self.couleur}\n{self.materiaux}'
    
    def __repr__(self) -> str:
        return str(self)


if __name__ == "__main__":

    print(Objet(Point(1,1,1)))