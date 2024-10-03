from __future__ import annotations
from math import tan, pi
from point import Point
from vecteur import Vecteur
from ray import Ray

class Camera():
    """ La caméra est une classe fondamentale du projet, elle peut être plus
        ou moins sophistiquée (ajout d'un aspect ration, d'un fov, d'un look at
        etc.). Ici elle est définie par son origine, son up vecteur, le vecteur
        de la direction regardée (initialisé par un look at), son right vecteur
        qui est le produit vectoriel des deux derniers. La taille de l'image
        (la hauteur est définie avec la largeur et l'aspect ratio), et sa
        résolution. On procède à un sur-échantillonnage pour réduire l'angle des
        rayons de vues. """  


    def __init__(self, origine : Point, up : Vecteur, look_at : Point,
                  focale : int, resolution : int, largeur_image : int,
                    aspect_ratio : float, fov : int) -> None:
        self.origine = origine
        self.up = up.normalisation()
        #self.direction = direction.normalisation()
        self.direction = Vecteur(look_at, self.origine).normalisation()
        self.focale = origine - self.direction * focale
        self.resolution = resolution
        self.largeur_image = largeur_image
        self.hauteur_image = int(largeur_image // aspect_ratio)
        self.fov = fov
        self.droite = self.direction.prod_vec(up).normalisation()

        self.nl = int(resolution // aspect_ratio)
        self.nc = resolution
        self.delta_x = self.largeur_image / self.nc #* tan(self.fov / 2 * pi / 180)
        self.delta_y = self.hauteur_image / self.nl #* tan(self.fov / 2 * pi / 180)
        self.Phg = (origine + up * ((self.hauteur_image/2 - self.delta_y/2)) - self.droite * ((self.largeur_image / 2 - self.delta_x / 2))) 
        

    def rayon_vue(self, x : int, y : int) -> Ray:
        """ Renvoi un rayon qui a pour origine le foyer et comme direction le centre du pixel(x,y)."""


        Pxy = self.Phg - self.up * y * self.delta_y + self.droite * x * self.delta_x
        ray_direction = Vecteur(Pxy, self.focale)
        return Ray(self.focale, ray_direction)






if __name__ == "__main__":
    #exemple du td
    cam = Camera(Point(0, 0, 0), 1600, 1600, Vecteur(Point(0, 0, 1)), Vecteur(Point(0, 1, 0)), 10)
    print("pixel",cam.pixel(800, 450))
