from point import Point
from vecteur import Vecteur
from ray import Ray


class Camera():
    flag = False
    """
    la caméra est définie par son centre _position_ ça _dimension_[hauteur, largeur] en nombre de pixel
    ça _direction_ "look at mais main droite comme dans le td donc la scene est dans les z négatifs" (vecteur directeur)
    son _up_ vecteur pour son orientation et ça distance _focale_ qui donne un point
    """
    
    def __init__(self, position: Point, dimension, direction: Vecteur, up: Vecteur, focale: float):
        self.centre = position
        self.hauteur = dimension[0]
        self.largeur = dimension[1]
        self.direction = direction.normalisation()
        self.up = up.normalisation()

        #calcul de la distance focale
        foc = self.centre.arr + self.direction.arr * focale
        self.focale = Point(foc[0], foc[1], foc[2])
        #print("Focale", self.focale)

        #calcul du troisième vecteur "droite" de la camera en fesant up produit vectoriel direction
        self.droite = self.up.prod_vec(self.direction)

        #calcul du centre du pixel haut gauche (origine)
        origine = self.centre.arr + self.up.arr * (self.hauteur / 2 - 0.1 / 2) - self.droite.arr * (self.largeur / 2 - 0.1 / 2)
        self.hg = Point(origine[0], origine[1], origine[2])
        #print("HG", self.hg)

    def pixel(self, x: int, y: int) -> Point:
        """
        retourne les coordonnées dans l'espace 3D du centre du pixel de "coordonées" dans l'espace caméra _x_ _y_ grâce au pixel d'origine en haut a gauche
        """

        #test pour ne pas avoir de fausse coordonées
        #fois 10 car il y a 10 fois plus de pixel ar rapport à la longueur de la cam car pixel mesure 0.1
        if 0 <= x <= self.largeur * 10 and 0 <= y <= self.hauteur * 10:
            p = self.hg.arr - self.up.arr * y * 0.1 + self.droite.arr * x * 0.1
            return Point(p[0], p[1], p[2])
        else:
            print("Erreur coordonée pixel")
            exit()
    
    
    def rayon_vue(self, x: int, y: int) -> Ray:
        """
        creer un rayon a partir du foyer passant par le centre du pixel x y
        """

        #calcul du vecteur directeur du rayon
        
        vec = Vecteur(self.pixel(x, y), self.focale)
        r = Ray(self.focale, vec)
        # if not Camera.flag : 
        #     Camera.flag = True
        #     print("Rayon", r.direction, r.origine)
        #     print("Pixel", self.pixel(x,y))
        return r



if __name__ == "__main__":
    #exemple du td
    cam = Camera(Point(0, 0, 0), [11, 11], Vecteur(Point(0, 0, 1)), Vecteur(Point(0, 1, 0)), 10)
    print("pixel",cam.pixel(55, 55))
