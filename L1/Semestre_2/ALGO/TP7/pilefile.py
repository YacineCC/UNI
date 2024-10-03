from copy import deepcopy

def pile_init():
    """Retourne une pile vide"""
    return []

def pile_copie(P):
    """Retourne une copie de la pile <P>"""
    return deepcopy(P)

def pile_lire(P):
    """Retourne l'element au sommet de la pile <P>"""
    return P[-1]

def pile_vide(P):
    """Retourne True si la pile <P> est vide, False sinon"""
    return P == []

def empiler(P,x):
    """Ajoute l'element <x> au sommet de la pile <P>"""
    P.append(x)

def depiler(P):
    """Depile l'element au sommet de la pile <P> et le retourne"""
    return P.pop()



def file_init():
    """Retourne une file vide"""
    return []

def file_copie(F):
    """Retourne une copie de la file <F>"""
    return deepcopy(F)

def file_lire(P):
    """Retourne l'element a la tete de la file <F>"""
    return F[-1]

def file_vide(F):
    """Retourne True si la file <F> est vide, False sinon"""
    return F == []

def enfiler(F,x):
    """Ajoute l'element <x> a la queue de la file <F>"""
    F.append(x)
    for i in range(len(F)-1,0,-1):
        F[i],F[i-1] = F[i-1],F[i]
    
def defiler(F):
    """Defile l'element en tete de la File <F> et le retourne"""
    return F.pop()
