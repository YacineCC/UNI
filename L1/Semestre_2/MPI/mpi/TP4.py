#########################################################
#
# CORRECTION TP4 (MATHEMATIQUES POUR L'INFORMATIQUE)
# Quelques variations autour du groupe des permutations
#
#########################################################

#------------------------------------------------------------------------
# Convertit la chaÃ®ne lue au clavier par un tuple d'entiers
# Ne vÃ©rifie pas s'il s'agit d'une permutation.
#------------------------------------------------------------------------
def Lire():
   chaine = input("Permutation = ")
   return tuple([int(x) - 1 for x in chaine.split()])

#------------------------------------------------------------------------
# Affiche une permutation en rajoutant 1 aux valeurs du tuple qui
# la code.
#------------------------------------------------------------------------
def Ecrire(s):
    print('(',end='')
    for i in range(len(s) - 1):
        print(s[i] + 1, end=',')
    print(s[len(s) - 1] + 1,end=')\n')
    
#------------------------------------------------------------------------
# DÃ©cide si un tuple d'entier est code une permutation.
# PlutÃ´t que de chercher pour chaque entier i dans [1,n] s'il est
# dans le tuple s (de longueur n) occasionnant ainsi n balayages de
# ce tuple, on crÃ©e une liste B de n boolÃ©ens initialisÃ©s Ã  False
# qui indique si chaque valeur appartient ou non Ã  la permutation
#------------------------------------------------------------------------
def EstPermutation(s):
    n = len(s)
    B = [False] * n
    for i in s:
        if ((i >= 0) and (i < n) and (not(B[i]))):
            # Mise Ã  jour de B[i] si ce n'est pas deja le cas
            B[i] = True
        else:
            # sinon on sait dÃ©jÃ  que ce n'est pas une perm.
            return False
    return True
 
#------------------------------------------------------------------------
# Renvoie la permutation inverse de celle passÃ©e en parametre s et
# codÃ©e sous forme de tuple s:=(s(1),s(2),...,s(n)).
# NB. Les tuples Ã©tant non-mutables, il est prÃ©fÃ©rable de crÃ©er d'abord
# une liste afin d'Ã©viter de balayer le tuple s pour ajouter le prochain
# terme du tuple rÃ©sultat.
#------------------------------------------------------------------------
def Inverser(s):
    retour = [0] * len(s)
    for i in range(len(s)):
        retour[s[i]] = i
    return tuple(retour)

#------------------------------------------------------------------------
# Renvoie la composition sÂ°t des deux permutations s et t passÃ©es
# en paramÃ¨tre. On suppose bien sÃ»r qu'il s'agit de deux permutations de
# mÃªme longueur.
#------------------------------------------------------------------------
def Composer(s,t):
    c = ()
    for i in range(len(s)):
        c = c + (t[s[i]],)
    return c

#------------------------------------------------------------------------
# Renvoie l'orbite de k suivant la permutation s
#------------------------------------------------------------------------
def Orbite(k,s):
   k = k - 1
   debut = k
   o = (k,)
   while (s[k] != debut):
      k = s[k]
      o = o + (k,)
   return o

#------------------------------------------------------------------------
# Renvoie le plus petit indice j > i tel que B[j] ou -1 s'il n'y en a pas
#------------------------------------------------------------------------
def Suivant(B,i):
   j = i + 1
   retour = -1
   while (j < len(B)) and (not B[j]):
      j = j + 1
   if (j < len(B)):
      retour = j        
   return retour

#------------------------------------------------------------------------
# Renvoie la dÃ©composition de s en produit de cycles Ã  supports
# disjoints. On crÃ©e une liste B de n boolÃ©ens (permutation de S_n)
# qui indique si oui ou non l'entier i a dÃ©jÃ  Ã©tÃ© inclus dans un
# cycle.
#------------------------------------------------------------------------
def Cycles(s):
   n = len(s)
   B = [True] * n
   i = 0
   produitcycles = ()
   while (i != -1):
      # tant qu'il reste des elements non collectÃ©s dans les
      # prÃ©cÃ©dents cycles, on initialise le nouveau cycle avec i
      cycle = (i,)
      B[i] = False
      debut = i
      while (s[i] != debut):
         cycle = cycle + (s[i],)
         i = s[i]
         B[i] = False
      if (len(cycle) > 1):
         # on ne conserve que les orbites de plus d'un Ã©lÃ©ment
         produitcycles = produitcycles + (cycle,)
      i = Suivant(B,i)
   return produitcycles

#------------------------------------------------------------------------
# Renvoie la dÃ©composition de s en produit de transpositions.
# S'appuie sur la dÃ©composition en produit de cycles et la preuve
# constructive du thÃ©orÃ¨me 29. Ex: (a,b,c) = (a,b)(b,c)
#------------------------------------------------------------------------
def Transpositions(s):
   produitcycles = Cycles(s)
   produittransp = ()
   for cycle in produitcycles:
      i = 0
      while i < len(cycle) - 1:
         produittransp = produittransp + ((cycle[i],cycle[i+1]),)
         i = i + 1
   return produittransp

#------------------------------------------------------------------------
# Renvoie la signature d'une permutation. Il faut recalculer le nombre
# d'orbites rÃ©duites Ã  un singleton. C'est
#------------------------------------------------------------------------
def signature(s):
   produitcycles = Cycles(s)
   somme = len(produitcycles)
   for cycle in produitcycles:
      somme = somme - len(cycle)
   return int((-1)**(somme))

#------------------------------------------------------------------------
# Renvoie la conjuguÃ©e de la permutation s par r
#------------------------------------------------------------------------
def Conjuguer(s,r):
   return Composer(r,Composer(s,Inverser(r)))


##########################################################################
# PROGRAMME PRINCIPAL
##########################################################################
s = Lire()
print(EstPermutation(s))
Ecrire(s)
#Ecrire(Inverser(s))
#print(Composer(s,t))
PC = Cycles(s)
print('PC',PC)
print("Cycles:")
for i in range(len(PC)):
    Ecrire(PC[i])
PT = Transpositions(s)
print("Transpositions:")
for i in range(len(PT)):
    Ecrire(PT[i])
print("Signature: ",end='')
print(signature(s))
Ecrire(Orbite(1,s))
#Ecrire(Conjuguer(s,s))


