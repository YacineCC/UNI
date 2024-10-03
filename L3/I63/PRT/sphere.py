from objet import Objet
from couleur import Couleur
from point import Point
from vecteur import Vecteur
from ray import Ray


class Sphere(Objet):

    def __init__(self, pos : Point, coul=Couleur(Point(255, 0, 0)), ambiant=0.2, diffu=0.7, spec=0.8, reflex = 100, ombr=False, r=0.5, coef_r=0):
        super().__init__(pos, coul, ambiant, diffu, spec, reflex, ombr, coef_r)
        self.rayon = r

    def __str__(self):
        return f'{super().__str__()} \n rayon = {self.rayon}'

    def __repr__(self) -> str:
        return str(self)

    def normale(self, point : Point):
        return Vecteur(point, self.position) / self.rayon

    def intersection(self, rayon_vue : Ray):
        # (P - C)² = r²
        # Vecteur(rayon_vue.origine, self.position) + t * rayon_vue.direction)² = self.rayon²
        #  CP² + 2CP * rayon.direction + rayon.direction² - self.rayon² = 0
        # a = rayon.direction²
        # b = 2CP * rayon.direction
        # c = CP² - self.rayon²


        cp = Vecteur(rayon_vue.origine, self.position)
        #print("Vecteur F centre sphere", cp)
        a = rayon_vue.direction.prod_scal(rayon_vue.direction)

        b = 2 * rayon_vue.direction.prod_scal(cp)
        c = cp.prod_scal(cp) - self.rayon ** 2
        #c = ((Vecteur(rayon_vue.origine, self.position)).norme()) ** 2 - self.rayon ** 2
        #a = 1
        
        delta = b * b - 4 * a * c
        #print(cp, b, c, delta)
        if delta > 0:
            #print(f"Delta: {delta} avec a: {a}, b: {b} et c: {c}")
            #print(b, delta)
            t1 = (-b + (delta ** 0.5)) / (2 * a) 
            t2 = (-b - (delta ** 0.5)) / (2 * a)
            #print(t1,t2)
            if t1 > 0 and t2 > 0 :
                
                return min(t1, t2)
            # else:
            #     return float('inf')

        
        elif delta == 0:
            return -b/(2 * a)
        else:
            return float('inf')
     
    



if __name__ == "__main__":

    sphere1 = (Sphere(Point(1,1,1), r=0.2))
    print(sphere1.couleur)

