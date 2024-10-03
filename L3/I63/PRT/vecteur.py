from narray import Narray
from point import Point
import numpy as np


class Vecteur(Narray):


    def __init__(self, arrivee : Point, depart=Point(0,0,0)):


        vec =  arrivee.arr - depart.arr 
        super().__init__(vec[0], vec[1], vec[2])
        #self.__composantes = p2.arr - p1.arr


    def __mul__(self, scal): # Méthode spéciale surcharge de l'opérateur *


        """ Produit vecteur scalaire. Retourne un Vecteur."""
        vec = self.arr * scal
        return Vecteur(Point(vec[0], vec[1], vec[2]))
    
    

    def __rmul__(self, scal): # Méthode spéciale surcharge de l'opérateur *


        """ Produit vecteur scalaire. Retourne un Vecteur."""
        vec = self.arr * scal
        return Vecteur(Point(vec[0], vec[1], vec[2]))
    
    def prod_vec(self, v2):


        """ Produit vectoriel. Retourne un Vecteur."""
        vec = np.cross(self.arr, v2.arr)
        return Vecteur(Point(vec[0], vec[1], vec[2]))
    
    def prod_comp(self, v2):
        """ Produit composante à composante. Utile pour Phong"""

        x = self.x * v2.x
        y = self.y * v2.y
        z = self.z * v2.z
        return Vecteur(Point(x, y, z))

    def prod_scal(self, v2) -> int: 


        """ Produit scalaire de deux vecteurs."""
        return np.dot(self.arr, v2.arr)
    

    def __add__(self, v2): # Méthode spéciale surcharge de l'opérateur +


        """ Addition de deux Vecteurs. Retourne un Vecteur."""
        vec = self.arr + v2.arr
        return Vecteur(Point(vec[0], vec[1], vec[2]))
    
    
    def __sub__(self, v2): # Méthode spéciale surcharge de l'opérateur - pour soustraction


        """ Soustraction de deux Vecteurs. Retourne un Vecteur."""
        vec = self.arr - v2.arr
        return Vecteur(Point(vec[0], vec[1], vec[2]))
    
    def __truediv__(self, scal):
        vec = self.arr / scal
        return Vecteur(Point(vec[0], vec[1], vec[2]))

    def __neg__(self): # Méthode spéciale pour le - unaire
        """ Retourne -V"""

        return Vecteur(Point(-self.x, -self.y, self.z))

    def norme(self) -> float:
            

        return np.dot(self.arr, self.arr) ** 0.5


    def normalisation(self):


        norme = self.norme()
        vec = self.arr / norme
        return Vecteur(Point(vec[0], vec[1], vec[2]))

    def reflet(self, N):
        """ Retourne le Vecteur du rayon refleté."""
        moins_I = -self
        I = self
        
        R = ((2 * (moins_I.prod_scal(N))) * N) + I
        return R



if __name__ == "__main__":


    I = Vecteur(Point(0, -3, 5))
    N = Vecteur(Point(0, 1/(2**0.5), 1/(2**0.5)))
    R = I.reflet(N)
    V = Vecteur(Point(0, 0, -1))
    res = R.prod_scal(V)



    print(res)
