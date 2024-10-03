from objet import Objet
from vecteur import Vecteur
from couleur import Couleur
from point import Point
from ray import Ray

class Plan(Objet):
    def __init__(self, pos : Point, coul=Couleur(Point(255, 0, 0)), ambiant=0.2, diffu=0.7, spec=0.8, reflex = 100, ombr=False, dir=Vecteur(Point(0, 1, 0)), coef_r=0):
        super().__init__(pos, coul, ambiant, diffu, spec, reflex, ombr, coef_r)
        self.direction = dir.normalisation()

    def __str__(self):
        return f'{super().__str__()} \n direction = {self.direction}'

    def __repr__(self) -> str:
        return str(self)
    
    def normale(self, pt) -> Vecteur:
        """ Retourne la normale du plan"""
        return self.direction
    



    def intersection(self, ray : Ray):

        N = self.direction # Normale du plan.
        o_r = ray.origine # Origine du rayon de vue / de la demi-droite.
        o_d = ray.direction # Vecteur directeur du rayon de vue.

        A, B, C = N.x, N.y, N.z
        x1, y1, z1 = o_r.x, o_r.y, o_r.z
        i, j, k = o_d.x, o_d.y, o_d.z

        x, y, z = self.position.x, self.position.y,  self.position.z

        D = -(A*x + B*y + C*z)
        #print(D)

        t = - (A*x1 + B*y1 + C*z1 + D) / (A*i + B*j + C*k)
        
        if t >= 0:
            return t
        else :
            return float('inf')
        
        #print(t)

        #return t

        

if __name__ == "__main__":

    print(Plan((0, 0, 0)))