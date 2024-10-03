from __future__ import annotations
from narray import Narray
from point import Point
import numpy as np


class Vecteur(Narray):
    """ Vecteur à trois dimensions utile pour tous les calculs vectoriel, hérite
    de Narray donc utilisation d'un numpy array."""


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
        return Vecteur(Point(-self.x, -self.y, -self.z))

    def norme(self) -> float:
        return np.dot(self.arr, self.arr) ** 0.5


    def normalisation(self):
        """ Retourne une nouvelle instance du vecteur normalisé."""
        norme = self.norme()
        vec = self.arr / norme
        return Vecteur(Point(vec[0], vec[1], vec[2]))

    def reflet(self, N):
        """ Retourne le Vecteur du rayon refleté. Depuis la formule d'un rayon
        réfléchi 2*(-I.N) + I"""
        moins_I = -self
        I = self
        R =  moins_I.prod_scal(N)
        R = R * 2
        R = N * R
        R = R + I
        # On normalise toujours une direction.
        R = R.normalisation()
        
        return R

    def refraction(self, N, n1, n2):
        """ Retourne le Vecteur réfracté. Depuis la formule du TD mais aussi à
        partir de ce cours vidéo (qui transforme les cos en produit scalaire) :
        https://youtu.be/Tyg02tN9oSo?t=1840 de 30:40 à 56:20"""
        if ((self.prod_scal(N)) < 0):
            # Réfraction totale interne.
            return None
        # On a besoin de savoir l'indice réfraction du mileu courant et celui du
        # milieu dans lequel on va rentrer.
        indice_refraction = n1/n2
        return (indice_refraction * self.prod_scal(N) - (1 - (indice_refraction ** 2) * (1 - (self.prod_scal(N) ** 2)) ** 0.5)) * N - indice_refraction * self

    

if __name__ == "__main__":
    I = Vecteur(Point(0, 0, -1))
    N = Vecteur(Point(0, 1/2**0.5, 1/2**0.5))
    R = I.refraction(N, 1, 1.52)



