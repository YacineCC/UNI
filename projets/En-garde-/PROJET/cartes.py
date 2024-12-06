import tkinter as tk
import random as rand

carte_id = 0

class Carte:
    """definitions d'une carte plus affichage"""
    valeur = 0

    def __init__(self, val):
        self.valeur = val

    #def affiche_carte(self, canv, i, j):
        """affiche la carte au coordoner i j"""
        
class Pioche:
    n = 0
    liste = []#[-1] * 25
    vide = True

    def __init__(self):
        """initisalisation de la pioche 25 carte mélangé"""
        self.n = 25
        #self.liste = [Carte(1), Carte(1), Carte(1), Carte(1), Carte(1), Carte(2), Carte(2), Carte(2), Carte(2), Carte(2), Carte(3), Carte(3), Carte(3), Carte(3), Carte(3), Carte(4), Carte(4), Carte(4), Carte(4), Carte(4), Carte(5), Carte(5), Carte(5), Carte(5), Carte(5)]

        for i in range(1, 6):
            self.liste += [Carte(i)] * 5
        # for i in range(1, 6):
        #    for j in range(5):
        #        self.liste[(i - 1) * 5 + j] = Carte(i)

        for i in range(24):
            r = rand.randrange(i + 1, 25)
            self.liste[i], self.liste[r] = self.liste[r], self.liste[i]
        self.vide = False

    
    def pioche_carte(self):
        """ pioche et retourne la carte en haut du paquet """
        if self.n <= 0:
            self.vide = True
        elif self.n > 0:
            carte = self.liste[self.n - 1]
            self.n -= 1
            return carte


    def __str__(self):
        """affiche le contenue de la pioche"""
        s = ""
        for i in range(self.n):
            s += str(self.liste[i].valeur) + " "
        return s

class Deck:
    n = 0
    liste = []
    
    def __init__(self, pioche):
        """initialse la main de départ à 5 carte à utiliser qu'au début de la partie !!"""
        self.n = 5
        for i in range(5):
            self.liste += [pioche.pioche_carte()]

    def remplir_deck(self, pioche):
        """rempli la main tant que la pioche n'est pas vide"""
        while (self.n < 5 and pioche.n > 0):
            self.liste += [pioche.pioche_carte()]
            self.n += 1

    def deffausser(self, carte):
        i = 0
        #on cherche la carte
        while self.liste[i].valeur != carte.valeur:
            i += 1

        #ensuite on l'enlève
        self.liste.pop(i)
        self.n -= 1


    def __str__(self):
        """affiche le deck"""
        s = ""
        for i in range(self.n):
            s += str(self.liste[i].valeur) + " "
        return s

    


if __name__=="__main__":
    p = Pioche()
    d = Deck(p)
    d.deffausser(d.liste[0])
    d.deffausser(d.liste[0])
    d.deffausser(d.liste[0])
    d.deffausser(d.liste[0])
    for i in range(24):
        p.liste.pop(0)
    p.n = 1
    print("--------")
    d.remplir_deck(p)
    print(d)




