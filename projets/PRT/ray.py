from __future__ import annotations
from point import Point
from vecteur import Vecteur

class Ray:

    def __init__(self, origine: Point, direction: Vecteur):
        """
        un rayon de vue est une demie droite définie par une origine et un
        vecteur directeur on dira que l'origine est le foyer de l'image et non
        pas le centre du pixel
        """
        
        self.origine = origine
        self.direction = direction.normalisation()

    def get_point(self, t : float):
        """ Renvoi les coordonnées du point d'intersection à partir d'un rayon,
        et de la distance retournée par l'intersection."""
        x = self.origine.x + t * self.direction.x
        y = self.origine.y + t * self.direction.y
        z = self.origine.z + t * self.direction.z
        return Point(x, y, z) 
    

if __name__ == "__main__":

    rayon = Ray(Point(0, 0,0), Vecteur(Point(0, -3/(34**0.5), 5/(34**0.5))))

    normale = Vecteur(Point(0, (2**0.5) / 2, (2**0.5) / 2))
    print(rayon.reflet(normale))