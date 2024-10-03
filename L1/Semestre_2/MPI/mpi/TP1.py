#####################################################
# CORRECTION TP1 (MATHEMATIQUES POUR L'INFORMATIQUE)
#
# NB. Les listes et dictionnaires sont mutables mais
# pas les chaÃ®nes ni les tuples. D'autre part les
# listes Ã©tant des rÃ©fÃ©rences, les modifications des
# valeurs d'une liste dans une fonction sont en fait
# rÃ©alisÃ©es sur la liste d'appel.
#
# Dans cette correction, le tri est effectuÃ© par
# l'algorithme du tri Ã  bulles et non par la
# mÃ©thode Python .sort().
###################################################n##

#-----------------------------------------------------
# Echange les valeurs aux indices i et j dans une
# structure Ã©numÃ©rÃ©e mutable. Didactique pour Ã©viter 
# l'emploi de x,y = y,x spÃ©cifique au Python et qui
# donne de mauvaises habitudes de programmation.
# Noter qu'il n'y a pas de valeur de retour car les
# listes sont des rÃ©fÃ©rences.
#-----------------------------------------------------
def Echanger(L,i,j):
    aux = L[i]
    L[i] = L[j]
    L[j] = aux

#-----------------------------------------------------
# Principe fondateur du tri Ã  bulles:
# Fait remonter la plus grande valeur de l'intervalle
# [i,j] de la liste L en position j en comparant les
# termes d'indices k et k + 1 pour k allant de i Ã 
# j - 1
#-----------------------------------------------------
def Propager(L,i,j):
    k = i
    while k < j:
        if L[k] > L[k + 1]:
            Echanger(L,k,k+1)
        k = k + 1
    return L

#-----------------------------------------------------
# Algorithme du tri Ã  bulles
# On rÃ©pÃ¨te la propagation 
#-----------------------------------------------------
def TriBulles(L):
    d = len(L) - 1
    while (d > 0):
        Propager(L,0,d)
        d = d - 1
    return L

#-----------------------------------------------------
# Extraction des variables boolÃ©ennes
# (Sans prÃ©occupation d'efficacitÃ©...)
#-----------------------------------------------------
#def ListerVariables(expression):
#    variables = []
#    lexique = "abcdefghijklmnopqrstuvwxyz"
#    for symbole in expression:
#        if (symbole in lexique) and not (symbole in variables):
#            variables.append(symbole)
#    return variables

#-----------------------------------------------------
# Extraction des variables boolÃ©ennes.
# Plus efficace, utilise les types adaptÃ©s.
# On part d'une structure d'ensemble, ainsi la mÃ©thode 
# .add ne rajoute pas un Ã©lÃ©ment dÃ©ja prÃ©sent dans
# un ensemble conformÃ©ment Ã  l'objet mathÃ©matique.
#-----------------------------------------------------
def ListerVariables(expression):
    variables = set()
    for symbole in expression.lower():
        if symbole.isalpha():
            variables.add(symbole)
    return list(variables)

#-----------------------------------------------------
# Construction du dictionnaire Ã  partir de la liste
# des variables. On associe Ã  une variable sa position
# dans la liste, sachant qu'elles ont Ã©tÃ© triÃ©es dans
# l'ordre alphabÃ©tique au prÃ©alable.
#-----------------------------------------------------
def DicoVariables(liste):
    dico = {}
    i = 0
    while i < len(liste):
        dico[liste[i]] = i
        i = i + 1
    return dico

#-----------------------------------------------------
# Convertit un entier en binaire sur n bits en
# complÃ©tant par des 0 Ã  gauche si sa reprÃ©sentation
# comporte moins de n bits. 
#----------------------------------------------------
def Int2Bin(entier,n):
    bits = bin(entier)[2:]
    if len(bits) < n:
        bits = "0" * (n - len(bits)) + bits
    return bits
        
#-----------------------------------------------------
# Conversion d'une chaÃ®ne de caractÃ¨res de 0 ou 1
# en un tuple de boolÃ©ens correspondant.
# NB. Remarquer l'absence de if ! 
#-----------------------------------------------------
def Bin2Bool(bits):
    booleens  = ()
    for b in bits:
        booleens = booleens + (b == "1",)
    return booleens

#-----------------------------------------------------
# Convertit une expression logique formelle en 
# expression logique Ã©quivalente du langage Python.
# On balaie les symbole de l'expression en
# testant si le symbole courant est une
# variable, un opÃ©rateur ou autre.
#-----------------------------------------------------
def Math2Python(expression, vecteur, dicovar):
    pexp = ""
    operateurs = {"!":" not ","*":" and ","+":" or "}
    for symb in expression:
        if symb in dicovar.keys():
            pexp = pexp + str(vecteur[dicovar[symb]])
        elif symb in operateurs.keys():
            pexp = pexp + operateurs[symb]
        else:
            pexp = pexp + symb
    return pexp

#-------------------------------------------------------
# Renvoie la table de vÃ©ritÃ© de l'expression passee en
# parametre sous forme de liste contenant les 2^n valeurs
# possibles de l'expression de n variables logiques. 
#-------------------------------------------------------
def TableVerite(expression,dicovar):
    nbvar = len(dicovar.keys())
    TDV = [0] * (2**nbvar)
    for entier in range(2**nbvar):
        vecteur = Bin2Bool(Int2Bin(entier,nbvar))
        chaine = Math2Python(expression,vecteur,dicovar)
        if eval(chaine):
            TDV[entier] = 1
    return TDV

#--------------------------------------------------------
# Formate la sortie de l'Ã©valuation de l'expression
# pour un tuple logique de nbvar variables codÃ© sous
# forme d'entier. UtilisÃ©e pour afficher la TDV.
#--------------------------------------------------------
def AfficherLigne(entier, nbvar, TDV):
    for bit in Int2Bin(entier,nbvar):
        print(bit.rjust(2), end='')       
    print(' |' + str(TDV[entier]).rjust(2))

#-------------------------------------------------------
# Affiche une table de vÃ©ritÃ©.
#-------------------------------------------------------
def AfficherTDV(TDV, dicovar):
    nbvar = len(dicovar.keys())
    for v in sorted(dicovar.keys()):
        print(v.rjust(2),end='')
    print(" | E".rjust(2))
    for entier in range(2**nbvar):
        AfficherLigne(entier,nbvar,TDV)

#-------------------------------------------------------
# Affiche la FND d'une expression Ã  partir de sa table de
# vÃ©ritÃ©. 
#-------------------------------------------------------     
def FND(TDV, listevar):
    n = len(listevar)
    debut = True
    print("FND = ", end='')
    entier = 0
    while entier < len(TDV):
        if (TDV[entier] == 1):
            bits = Int2Bin(entier,n)
            if debut:
                debut = False
            else:
                print(" + ",end='')
            i = 0
            while i < n:
                if bits[i] == "1":
                    print(listevar[i],end='')
                else:
                    print(listevar[i] + "\u0304",end='')
                i = i + 1
        entier = entier + 1
    print()

#-------------------------------------------------------
# Affiche la FNC d'une expression Ã  partir de sa table de
# vÃ©ritÃ©. 
#-------------------------------------------------------     
def FNC(TDV, listevar):
    n = len(listevar)
    print("FNC = ", end='')
    entier = 0
    while entier < len(TDV):
        if (TDV[entier] == 0):
            bits = Int2Bin(entier,n)
            debut = True
            i = 0
            while i < n:
                if debut:
                    print('(', end='')
                    debut = False
                else:
                    print("+", end='')
                if bits[i] == "0":
                    print(listevar[i],end='')
                else:
                    print(listevar[i] + "\u0304",end='')
                i = i + 1
            print(')',end='')
        entier = entier + 1
    print()
        
##########################################################
# PROGRAMME PRINCIPAL
##########################################################
"""expression = input("Expression = ")
listevar = ListerVariables(expression)
print(listevar)
listevar = TriBulles(listevar)
print(listevar)
dicovar = DicoVariables(listevar)
print(dicovar)
TDV = TableVerite(expression,dicovar)
AfficherTDV(TDV,dicovar)
FND(TDV,listevar)
FNC(TDV,listevar)"""

"""def Somme(f,g):
	F = ()
	G = ()
	for s in f:
		F += (bin(s)[3:],)
	for s in g:
		G += (bin(s)[3:],)
	
	T = ()
	for s in G:
		print(s)
		if s in F ^ s in G:
			T += (s,)
		
	print(T)
		
	
	return (F,G)

print(Somme((9,13,15),(12,13,10)))"""

def PlusFrequent(L):
	dico = {}
	
	for s in L:
		dico[s] = 0
	
	for s in L:
		dico[s] += 1
	T = set()
	maxi = 0
	for s in dico:
		if dico[s] >= maxi:
			maxi = dico[s]
			T = T | {s}
	
	
	return T
L = [1,'a',1,4,'a',2,'a','v',1]

print(PlusFrequent(L))

L=[0,1,0]
print(PlusFrequent(L))

