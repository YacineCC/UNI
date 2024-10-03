from vecteur import Vecteur
from point import Point


class Couleur(Vecteur):
    """ Triplets np.array RVB"""
    def __init__(self, rgb : Point):


        
        super().__init__(rgb)
        self.tup = (rgb.x, rgb.y, rgb.z)



if __name__ == "__main__":

    print(Couleur(Point(0,0,255)))