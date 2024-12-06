

class Plateau:
    def __init__(self, joueur1, joueur2):
        """initialisation du plateau avec les deux joueur à chaque extremité il faut mettre le joueur à l'id 1 pour le paramètre joueur 1 sinon çà foire"""
        self.piste = [0] * 21
        self.piste[0] = 1
        self.piste[20] = 2
        joueur1.case = 0
        joueur2.case = 20
