#####################################################
# CORRECTION TP2 (MATHEMATIQUES POUR L'INFORMATIQUE)
#
# NB. Les ensembles de dÃ©part et d'arrivÃ©e des
#     correspondances sont codÃ©s par des sets Python.
#     Le graphe, qui pourrait Ãªtre codÃ© comme un
#     ensemble de couples (set de tuples en Python),
#     est codÃ© sous forme de dictionnaire dont les
#     clÃ©s x sont les Ã©lements du domaine de dÃ©finition
#     de la correspondance c et les valeurs associÃ©es
#     les images c({x}).
#####################################################

import sys

#-----------------------------------------------------
# Renvoie une correspondance (X,G,Y) codÃ©e en tuple
# Python Ã  partir d'un fichier dont chaque ligne
# contient un couple (x,y) codÃ© par la chaÃ®ne "x>y".
# une chaÃ®ne ">y" sans x dÃ©signe un terme de Y sans 
# correspondant dans X et une chaine "x>" sans y
# dÃ©signe un terme de X sans correspondant dans Y.
#-----------------------------------------------------
def Lecture(nomfichier):
    fichier = open(nomfichier,"r")
    liste = fichier.readlines()
    X = set()
    Y = set()
    G = {}
    for fleche in liste:
        (x,y) = fleche.rstrip().split(">")
        # on s'assure de ne pas rajouter la chaÃ®ne vide
        # dans les ensembles de dÃ©part et d'arrivÃ©e
        if x != '':
            X = X | {x}
        if y != '':
            Y = Y | {y}
        # si la fleche relie bien deux objets
        # on rajoute le couple dans le graphe
        if (x != '') and (y != ''):
            if (x in G.keys()):
                G[x] = G[x] | {y}
            else:
                G[x] = {y}
    return (X,G,Y)

#---------------------------------------------------------------
# Renvoie la correspondance rÃ©ciproque.
#---------------------------------------------------------------

def ImDirRec(c,A,B):
    (X,G,Y) = c
    GR = {}
    for x in G.keys():        
        for y in G[x]:
            if y in GR.keys():                
                GR[y] = GR[y] | {x}
            else:
                GR[y] = {x}
                
    (X,G,Y) = c
    (x,g,y) = (Y,GR,X)
    IDA = set()
    IDB = set()
    for x in g.keys():
        if x in A:
        
        
            IDB = IDB | g[x]
            
            IDA = IDA | set(x) 
            
   	    
            
        
    return (IDA,IDB)
        

#---------------------------------------------------------------
# Renvoie l'image rÃ©ciproque d'une partie B pour la correspondance
# (X,G,Y) On suppose que B est un sous-ensemble de Y pour ne
# pas polluer le script avec des tests inutiles.
#---------------------------------------------------------------
def ImageReciproque(correspondance,B):
    creciproque = Reciproque(correspondance)
    return ImageDirecte(creciproque,B)

#---------------------------------------------------------------
# Renvoie la correspondance g o f, composÃ©e des deux
# correspondances f: X â†’ Y et g: Y â†’ Z.
#---------------------------------------------------------------
def Composer(g,f):    
    (X,Gf,Y) = f
    (Y,Gg,Z) = g
    Ggof = {}
    for x in Gf.keys():
        for y in Gf[x]:
            if y in Gg.keys():
                if x in Ggof.keys():
                    Ggof[x] = Ggof[x] | Gg[y] 
                else:
                    Ggof[x] = Gg[y]
    return (X,Ggof,Z)

#---------------------------------------------------------------
# DÃ©cide si une correspondance est une fonction   
#---------------------------------------------------------------
def EstFonction(correspondance):
    (X,G,Y) = correspondance
    for x in G.keys():
        if (len(G[x]) > 1):
            return False
    return True

#---------------------------------------------------------------
# DÃ©cide si une correspondance est une application
#---------------------------------------------------------------
def EstApplication(correspondance):
    (X,G,Y) = correspondance
    for x in X:
        if ((not x in G.keys()) or (len(G[x]) > 1)):
            return False
    return True

#---------------------------------------------------------------
# Affiche une correspondance plus lisiblement qu'un simple print
#---------------------------------------------------------------
def Affiche(infos, correspondance):
    print(infos)
    print("X = ",str(correspondance[0]).replace("'",''))
    print("G = ",str(correspondance[1]).replace("'",''))
    print("Y = ",str(correspondance[2]).replace("'",''),end='\n\n')

##########################################################
# PROGRAMME PRINCIPAL
##########################################################
nomfichier = input("Correspondance f : ")
f = Lecture(nomfichier)
"""nomfichier = input("Correspondance g : ")
g = Lecture(nomfichier)
"""

Affiche("f:",f)
#Affiche("g:",g)
print("f fonction: ", EstFonction(f))
#print("g fonction: ", EstFonction(g))
print("f application: ", EstApplication(f))
#print("g application: ", EstApplication(g),'\n')
#rf = Reciproque(f)
#Affiche("f^{-1}:", rf)
#rfof = Composer(rf, f)
#Affiche("f^{-1} o f:", rfof)
#gof = Composer(g,f)
#Affiche("g o f:", gof)


print(ImDirRec(f,'a,d','1,3'))
    




