from point import Point
from vecteur import Vecteur
class Ray:

    def __init__(self, origine: Point, direction: Vecteur):
        """
        un rayon de vue est une demie droite définie par une origine et un vecteur directeur
        on dira que l'origine est le foyer de l'image et non pas le centre du pixel
        """
        
        self.origine = origine
        self.direction = direction.normalisation()
        #self.direction = direction

    def get_point(self, t : float):
        x = self.origine.x + t * self.direction.x
        y = self.origine.y + t * self.direction.y
        z = self.origine.z + t * self.direction.z
        return Point(x, y, z) 
    
    def reflet(self, N):
        """ Retourne le Vecteur du rayon refleté."""
        moins_I = -self.direction
        I = self.direction
        
        R = ((2 * (moins_I.prod_scal(N))) * N) + I
        return R
    
if __name__ == "__main__":

    rayon = Ray(Point(0, 0,0), Vecteur(Point(0, -3/(34**0.5), 5/(34**0.5))))

    normale = Vecteur(Point(0, (2**0.5) / 2, (2**0.5) / 2))
    print(rayon.reflet(normale))