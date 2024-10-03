from point import Point
from couleur import Couleur


class Lumiere:

    def __init__(self, pos : Point, coul=Couleur(Point(255, 255, 255))):
        self.position = pos
        self.couleur = coul
        