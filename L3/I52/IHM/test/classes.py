
class Cartes:

    def __init__(self, val):

        self.valeur = val;

    def afficher_cartes(self):
        print(self.valeur)

class Deck:
    def __init__(self,hand):
        self.hand = [-1]*5
        for i in range(len(hand)):
            self.hand[i] = hand[i]

    def afficher_Deck(self):
        print(self.hand)
une_carte = Cartes(val = 5)


une_carte.afficher_cartes()

main = [1,3,5,4,2]
test = Deck(hand=main)
test.afficher_Deck()
