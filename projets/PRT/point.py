from __future__ import annotations
from narray import Narray
import numpy as np

class Point(Narray):
    """ Simple classe Point qui représente un point 3D, utile pour définir la
    position d'un objet, d'une lumière et de la caméra."""


    """ Quelques méthodes spéciales pour pouvoir additionner et soustraire deux
    points."""
    def __add__(self, p2):
        
        tmp = self.arr + p2.arr
        return Point(tmp[0], tmp[1], tmp[2])
    
    def __sub__(self, p2):
        tmp = self.arr - p2.arr
        return Point(tmp[0], tmp[1], tmp[2])



    def distance(self, p2):
        """ Retourne la distance entre deux points 3D, utile pour l'algorithme
        de l'ombre portée."""
        return (((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2 + (p2.z - self.z) ** 2) ** 0.5)
    

if __name__ == "__main__":
    A = Point(0,0,0)
    B = Point(5,5,5)
    print(A + B)
