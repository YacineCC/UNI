from __future__ import annotations
from point import Point
from couleur import Couleur, BLANC


class Lumiere:
    """ Une lumière est simplement définie par sa position et sa couleur. En
    général une lumière est blanche mais on verra par la suite comment des
    lumières de couleurs interagissent avec des objets d'autres couleurs."""
    def __init__(self, pos : Point, couleur=BLANC):
        self.position = pos
        self.couleur = couleur
        