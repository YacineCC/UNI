from cartes import *
from joueur import *
from plateau import *

if __name__=="__main__":
    pioche = Pioche()
    j1 = Joueur("coc", 1, pioche)
    j2 = Joueur("zob", 2, pioche)
    plateau = Plateau(j1, j2)
    print(j1.main)
    j1.avancer(j1.main.liste[1], plateau)
    print(plateau.piste)
    print(j1.main)
