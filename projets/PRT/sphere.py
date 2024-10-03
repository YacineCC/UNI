from __future__ import annotations
from objet import Objet
from couleur import Couleur
from point import Point
from vecteur import Vecteur
from ray import Ray
from materiaux import Materiaux

class Sphere(Objet):
    """ Une sphère hérite de la métaclasse Objet, elle est mathématiquement
    définie par son centre et son rayon, dans le cadre de l'infographie on y 
    ajoute une couleur et un matériau."""


    def __init__(self, pos : Point, couleur : Couleur, rayon : float, materiaux : Materiaux):
        super().__init__(pos, couleur, materiaux)
        self.rayon = rayon

    def __str__(self):
        return f'{super().__str__()} \n rayon = {self.rayon}'

    def __repr__(self) -> str:
        return str(self)

    def normale(self, point : Point):
        """ Retourne la normale d'une sphère à partir de son centre et du point
        d'intersection, le rayon sert à normaliser et économiser une
        normalisation classique plus coûteuse. Car dans ce cas particulier la
        longueur du vecteur et littéralement celui du rayon."""
        return Vecteur(point, self.position) / self.rayon

    def intersection(self, rayon_vue : Ray):
        """ Renvoi le distance t de l'intersection d'un rayon avec une sphère si
        il y en une, renvoi une valeur infinie sinon."""
        # (P - C)² = r²
        # Vecteur(rayon_vue.origine, self.position) + t * rayon_vue.direction)² = self.rayon²
        #  CP² + 2CP * rayon.direction + rayon.direction² - self.rayon² = 0
        # a = rayon.direction²
        # b = 2CP * rayon.direction
        # c = CP² - self.rayon²


        cp = Vecteur(rayon_vue.origine, self.position)
        a = rayon_vue.direction.prod_scal(rayon_vue.direction)
        b = 2 * rayon_vue.direction.prod_scal(cp)
        c = cp.prod_scal(cp) - self.rayon ** 2
        #a = 1
        
        # Résolution de l'équation du 2nd degré, si t1 et t2 < 0 la sphère est
        # derrière la caméra, si t1 > 0 et t2 < 0  caméra est dans la sphère.
        delta = b * b - 4 * a * c
        if delta > 0:
            t1 = (-b + (delta ** 0.5)) / (2 * a) 
            t2 = (-b - (delta ** 0.5)) / (2 * a)
            if t1 > 0 and t2 > 0 :
                
                return min(t1, t2)
            else:
                return float('inf')
        elif delta == 0:
            return -b/(2 * a)
        else:
            return float('inf')
     
    



if __name__ == "__main__":

    sphere1 = (Sphere(Point(1,1,1), r=0.2))
    print(sphere1.couleur)

