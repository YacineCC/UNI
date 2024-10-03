from couleur import Couleur
from point import Point
from vecteur import Vecteur
class Objet:

    def __init__(self, pos : Point, coul=Couleur(Point(255, 0, 0)), ambiant=0.2, diffu=0.7, spec=0.8, reflex = 100, ombr=False, coef_r=0.1):
        self.position = pos # centre de la sphere
        self.couleur = coul
        self.ka = ambiant
        self.kd = diffu
        self.ks = spec
        self.n = reflex
        self.ombre = ombr
        self.coef_r = coef_r
    


    def __str__(self) -> str:
        return f'position : {self.position}\n couleur {self.couleur}\n ambiant : {self.ambiant}\n diffus : {self.diffus}\n speculaire : {self.speculaire}\n reflexion : {self.reflexion}\n ombre : {self.ombre}'
    
    def __repr__(self) -> str:
        return str(self)



    def normale():
        pass


if __name__ == "__main__":

    print(Objet(Point(1,1,1)))