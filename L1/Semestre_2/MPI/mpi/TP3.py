#####################################################
#
# CORRECTION TP3 (MATHEMATIQUES POUR L'INFORMATIQUE)
# Quelques variations autour de la combinatoire.
#
###################################################

#------------------------------------------------------------------------
# Renvoie la factorielle de l'entier passÃ© en paramÃ¨tre. Exemple
# typique de la fonction qu'IL NE FAUT PAS Ã©crire rÃ©cursivement.
# En effet, conserver les calculs intermÃ©diaires dans une pile ne
# sert Ã  rien ici, mÃªme pas pour simplifier l'Ã©criture de l'algo.
#------------------------------------------------------------------------
def factorielle(n):
    retour = 1
    for i in range(2, n + 1):
        retour = retour * i
    return retour

#------------------------------------------------------------------------
# Renvoie la liste des n+1 coefficients binomiaux C(n,p) sur la derniÃ¨re 
# ligne du triangle de Pascal. Remarque: la construction se passe de
# liste ou de variable auxiliaire car en parcourant de la droite vers
# la gauche on Ã©crase un terme dont on n'a plus besoin ce qui n'est pas
# le cas avec un parcours gauche droite.
#------------------------------------------------------------------------
def TrianglePascal(n):
    TP = [1] + ([0] * n)
    for k in range(1, n + 1):
        for i in range(k):
            TP[k - i] = TP[k - i] + TP[k - i - 1]
    return TP

#------------------------------------------------------------------------
# Renvoie la liste des codes phoque de longueur n. Version rÃ©cursive
# Base rÃ©currente : si n = 0, n = 1 ou n = 2 (if et elifs)
# AutodÃ©finition  : n > 2 (else)
#------------------------------------------------------------------------
def phoque(n):
    if n == 0:
        return []
    elif n == 1:
        return ['.']
    elif n == 2:
        return ['..','-']
    else:
        return [ '.' + x for x in phoque(n-1)] + [ '-' + x for x in phoque(n-2)] 

#------------------------------------------------------------------------
# Renvoie la liste des codes phoque de longueur n. Version itÃ©rative
#------------------------------------------------------------------------
def phoqueit(n):
    A = ['.']
    B = ['..','-']
    if n == 0:
        L = [0]
    elif n == 1:
        L = A
    elif n == 2:
        L = B
    else:
        for k in range(3,n+1):
            L = ['.' + x for x in B] + ['-' + x for x in A]
            A = B
            B = L
    return L

#------------------------------------------------------------------------
# Renvoie les n+1 premiers termes de la suite de Fibonacci dÃ©finie par
# F_{n+2} := F_{n+1} + F_{n} avec F_0:=0 et F_1:=1
# Ne DOIT PAS s'Ã©crire rÃ©cursivement, il n'y a que deux termes Ã 
# garder en mÃ©moire pour calculer le suivant et pas tout l'historique
# de la pile !
#------------------------------------------------------------------------
def Fibonacci(n):
    F = (0,1)
    for k in range(2,n+1):
        F = F + (F[k-1] + F[k-2],)
    return F

#------------------------------------------------------------------------
# Affiche tous les Ã©lÃ©ments de l'ensemble [1,m]^n (n-uplets)
#------------------------------------------------------------------------
def genuplet(n,m,nuplet):
    if (n == 0):
        print(nuplet)
    else:
        for i in range(m):
            genuplet(n - 1, m, nuplet + (i + 1,))

#########################################################################
# PROGRAMME PRINCIPAL
#########################################################################

n = int(input("Ordre n = "))
print('Coefficients binomiaux :',TrianglePascal(n))
print('Codes phoque de longueur',n,':',phoque(n))
print(Fibonacci(n))
n = int(input("Dimension n  = "))
m = int(input("Valeur max m = "))
genuplet(n,m,())

