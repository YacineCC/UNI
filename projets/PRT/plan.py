from __future__ import annotations
from objet import Objet
from vecteur import Vecteur
from couleur import Couleur
from point import Point
from ray import Ray
from materiaux import Materiaux

class Plan(Objet):
    """ Un hérite de la métaclasse Objet, un plan est mathématiquement défini
    par sa position et sa normale. Dans le cadre de l'infographie on y ajoute
    une couleur et un matériau."""


    def __init__(self, pos : Point, couleur : Couleur, direction : Vecteur, materiaux : Materiaux):
        super().__init__(pos, couleur, materiaux)
        self.direction = direction.normalisation()

    def __str__(self):
        return f'{super().__str__()} \n direction = {self.direction}'

    def __repr__(self) -> str:
        return str(self)
    
    def normale(self, pt) -> Vecteur:
        """ Retourne la normale du plan, pas de calcul nécessaire."""
        return self.direction
    
    def intersection(self, ray : Ray):
        """ Intersection entre un rayon et un plan comme vu en TD."""
        N = self.direction # Normale du plan.
        o_r = ray.origine # Origine du rayon de vue / de la demi-droite.
        o_d = ray.direction # Vecteur directeur du rayon de vue.

        A, B, C = N.x, N.y, N.z
        x1, y1, z1 = o_r.x, o_r.y, o_r.z
        i, j, k = o_d.x, o_d.y, o_d.z

        x, y, z = self.position.x, self.position.y,  self.position.z

        D = -(A*x + B*y + C*z)
        denominateur = (A*i + B*j + C*k)
        if denominateur == 0:
            # Pas d'intersection, évite une division par 0.
            return float('inf')
        t = - (A*x1 + B*y1 + C*z1 + D) / denominateur
        
        if t >= 0:
            return t
        else :
            return float('inf')
        
        
if __name__ == "__main__":

    print(Plan((0, 0, 0)))