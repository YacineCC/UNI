#
# Jeu du pendu
# 

from random import randrange
from time import time
import cProfile

def pos_lettre(mot, lettre):
    """Retourne la liste des indices ou apparait <lettre> dans la chaine
       de caracteres <mot>

    """
    lpos=[]
    for i in range(len(mot)):
        if lettre == mot[i]:
            lpos += [i]
    return lpos

def remplace_lettre(mot, lettre, lpos):
    """Retourne une copie de la chaine <mot> en remplacant les caracteres
       d'indices se trouvant dans la liste <lpos> par <lettre>

    """
    copie=""
    for i in range(len(mot)):
        if i in lpos:
            copie += lettre
        else:
            copie += mot[i]
    return copie


if __name__=="__main__":
    f = open("dico-fr.txt")
    dico=[]
    for line in f:
        dico.append(line[:-1])
    f.close()
    
    longueur = int(input('Choisir la longueur du mot à trouvé: '))
    if longueur < 4 or longueur > 25:
        print('longueur non valide')
        longueur = 10
    lmot = []
    for m in dico:
        if len(m)==longueur:
            lmot.append(m)

    mot  = lmot[randrange(len(lmot))]
    secret = '*'*len(mot)
    proposition = False
    while input('Faire un proposition de mot: (o)ui/(n)on ?')!='o':
        car = input('Proposer une lettre: ')
        lpos = pos_lettre(mot, car)
        secret=remplace_lettre(secret,car,lpos)
        print(secret)
    trouve = input('Proposition: ')
    if trouve == mot:
        print('Gagné')
    else:
        print('Perdu')
    #cProfile.run('f()')
