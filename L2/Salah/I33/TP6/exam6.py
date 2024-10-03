"""
On représente un vecteur x du R-espace vectoriel Rn par une liste à n

éléments.

On représente une famille de vecteurs de Rn
par une liste de liste. Par exemple pour n=3

, la liste

V = [ [1, 2, 0],  [0.5, 12, -6],  [3.67, -76, 11.29],  [176.7, 8.9, 54.2] ]

représente la famille dans R3

composée des vecteurs

(1,2,0),(0.5,12,−6),(3.67,−76,11.29),(176.7,8.9,54.2)

Ecrire la fonction combinaison_lineaire(c,V)
qui renvoie le vecteur obtenu en faisant la combinaison linéaire  des vecteurs de la famille V, les coefficients de cette combinaison linéaire étant spécifiés par la liste c

. Ainsi si

c=[c1,c2,…,cn]
avec ci∈R et V=[V1,V2,…,Vn] avec Vi∈Rn, la fonction renvoie le vecteur c1V1+c2V2+⋯+cnVn.
"""
def combinaison_lineaire(c,V):
    L =[0]*len(V[0])
    coef =0
    
    for v in V :
        i = 0
        for el in v :
            el = el * c[coef]
            L[i] += el
            i += 1
        coef += 1
    
    return L


"""
Pour représenter un vecteur x du F2-espace vectoriel Fn2, on utilise un entier dont la décomposition en base 2 sur n

symboles donne les composantes de ce vecteur.

Exemple :  pour n=4
, la décomposition en base 2 sur 4 symboles de l'entier 13 donne 1101. L'entier 13 représente donc le vecteur (1,1,0,1)∈F42

.

On représente une famille de vecteurs de Fn2
par une liste d'entiers. Par exemple pour n=3

, la liste

V = [ 1, 6, 3, 2 ]

représente la famille dans F32

composée des vecteurs

(0,0,1),(1,1,0),(0,1,1),(0,1,0)

Ecrire la fonction combinaison_lineaire(c,V)

qui renvoie l'entier représentant  le vecteur obtenu en faisant la combinaison linéaire  des vecteurs de la famille V, les coefficients de cette combinaison linéaire étant spécifiés par la décomposition en base 2 de l'entier c.
En considérant l'exemple précédent, si c=12, sa décomposition en base 2 vaut 1100, la combinaison linéaire à effectuer est donc

1.(0,0,1)+1.(1,1,0)+0.(0,1,1)+0.(0,1,0)=(1,1,1)

le résultat à renvoyer est donc l'entier 7.
"""
def combinaison_lineaire(c,V):
    res = 0
    i = -1 
    
    while c != 0 :
        if c&1 :
            res = res ^ V[i] 
        i -= 1
        c = c >> 1
    return res


"""
Pour représenter un vecteur x du Fp-espace vectoriel Fnp

, on utilise une liste.

Exemple :  pour n=4
, la liste [2,3,4,1] représente un vecteur de  F45


On représente une famille de vecteurs de Fnp
par une liste de liste. Par exemple pour n=4

, la liste

V = [  [2,3,4,1], [1,1,0,2], [3,2,1,1] ]

représente la famille dans F45

composée des vecteurs

(2,3,4,1),(1,1,0,2),(3,2,1,1)

Ecrire la fonction combinaison_lineaire(c,V,p)

qui renvoie le vecteur obtenu en faisant la combinaison linéaire  des vecteurs de la famille V, les coefficients de cette combinaison linéaire étant spécifiés par la liste c.
En considérant l'exemple précédent, si c=[2,2,3], la combinaison linéaire à effectuer est donc

2.(2,3,4,1)+2.(1,1,0,2)+3.(3,2,1,1)
"""
def combinaison_lineaire(c,V,p):
    L =[0]*len(V[0])
    coef =0
    
    for v in V :
        i = 0
        for el in v :
            el = (el * c[coef])%p
            L[i] = (L[i] + el)%p
            i += 1
        coef += 1
    
    return L


"""
Ecrire la fonction liste_vecteurs(n) qui renvoie la liste des vecteurs du F2-espace vectoriel Fn2

.

Exemple: pour n=3, la fonction renvoie (dans cet ordre) :

[ [0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0] , [1,1,1] ]
"""
def liste_vecteurs(n):
    i = 0
    L = [] 
    
    for i in range(2<<(n-1)) :
        tmp = []
        for count in range(n) :
            tmp += [(i>>(n-count-1))&1,]
        L += [tmp,]
    return L 

"""
Ecrire la fonction liste_vecteurs(p,n) qui renvoie la liste des vecteurs du Fp-espace vectoriel Fnp

.

Exemple: pour p=3 et n=2, la fonction renvoie (dans cet ordre) :

[ [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2] ]
"""
def liste_vecteurs(p,n):
    L = []
    
    for i in range(p**n) :
        tmp = [0]*n
        j = -1
        for count in range(n) :
            tmp [j] = i%p
            i = i//p
            j -= 1
        L += [tmp,]
        
    return L


"""
On considère dans cette question un ensemble E composé de vecteurs (x1,x2,…,xn) de Rn dont les composantes sont liées par une équation linéaire du type a1x1+a2x2+⋯+anxn=0

.

Par exemple, pour n=3
, on peut considérer l'ensemble E1 des vecteurs (x1,x2,x3) t.q x1+x2+x3=0 ou l'ensemble E2 des vecteurs t.q 2x1−3x2+5x3=0

.

Pour coder l'équation linéaire qui relie les composantes des vecteurs considérés, on utilise en Python une liste qui contient les coefficients a1,a2,…,an

.

Ainsi pour l'ensemble E1
la relation est codée par la liste [1,1,1] et pour l'ensemble E2, la relation est codée par la liste [2,-3,5]. Vous avez vu en cours et TD que de tels ensembles peuvent se mettre sous la forme Vect(v1,v2,…) pour une certaine famille de vecteurs (v1,v2,…

).

Pour l'ensemble E1
, on a E1=Vect((−1,1,0),(−1,0,1)) car les vecteurs de E1 sont de la forme (−x2−x3,x2,x3)

.

Pour l'ensemble E2
, on a E2=Vect((3/2,1,0),(−5/2,0,1)) car les vecteurs de E2 sont de la forme (32x2−52x3,x2,x3)

.

On codera en Python un vecteur de taille n par une liste de n éléments.

Ecrire la fonction build_Vect(relation)
qui, pour un ensemble E de vecteurs de Rn dont les composantes sont liées par une équation linéaire donnée par la liste relation, renvoie la liste des vecteurs v1,v2,… t.q E=Vect(v1,v2,…)

.
"""
def build_Vect(relation):
    L = [] 
    i = 1 
    while  i < len(relation) :
        tmp = [0] * len(relation)
        tmp[0] =  -relation[i]/relation[0]
        tmp[i] = 1
        L += [tmp,]
        
        i += 1
    return L
"""
Fn2 est un F2-espace vectoriel. On représente un élément de Fn2 par une liste de n

éléments. De même, on représentera une famille de vecteurs de cet espace par une liste de listes.

Par exemple, pour n=4
, dans  F42

, la famille :

(1,0,0,1), (0,1,1,1), (1,1,0,1),(1,0,1,0)

sera représentée par la liste L=[[1,0,0,1], [0,1,1,1], [1,1,0,1],[1,0,1,0]].

Ecrire la fonction vect(L)
qui renvoie la liste de tous les éléments de l'espace Vect(v1,…,vk) où (v1,…,vk)

est la famille de vecteurs représentée par la liste L.

Pour cet exercice, vous avez accès (si vous le souhaitez) à la fonction to_int(L)

. Cette fonction prend en entrée une liste constituée uniquement de 0 et de 1 et renvoie l'entier dont la décomposition en base 2 correspond à la liste.

Par exemple to_int([1,0,1,0])

renvoie 5 (le bit de poids faible est à gauche dans la liste).

Vous pouvez aussi utiliser la fonction set(L)
qui transforme la liste L en un ensemble L. On rappelle qu'un ensemble ne contient que des éléments distincts.
"""
def vect(L):
    res = []
    for i in range(2<<(len(L)-1)) :
        tmp = 0
        for count in range(len(L)) :
            if i&1 :
               tmp = tmp ^ to_int(L[count])
            i = i >> 1
        liste = []
        for j in range(len(L[0])) :
            if tmp&1 :
                liste += [1,]
            else :
                liste += [0,]
            tmp = tmp >> 1
        res += [liste,]
    return res 


