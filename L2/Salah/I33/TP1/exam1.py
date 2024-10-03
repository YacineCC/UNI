"""
Ecrire la fonction somme_pair(L) qui renvoie la somme des éléments pairs de la liste L

.

Eexmple : pour L=[3,2,5,7,4,1]


somme_pair(L)
renvoie 6.
"""
def somme_pair(L):
	s=0
	for i in L :
		if (i%2==0):
			s+=i
	return s

"""
Ecrire la fonction somme_ind_pair(L) qui renvoie la somme des éléments d'indice pair de la liste L

.

Eexmple : pour L=[3,2,5,7,4,1]


somme_ind_pair(L)
renvoie 12.
"""
def somme_ind_pair(L):
	i=0
	s=0
	while i<len(L):
		s+=L[i]
		i+=2
	return s
	
"""
On peut représenter une fraction pq par une liste à 2 éléments [p,q]. Ecrire la fonction somme(L,M)

qui à partir de 2 listes L et M représentant chacune une fraction calcule la somme de ces fractions et renvoie :

    si le résultat est une fraction, la liste représentant cette fraction sous forme irréductible,
    si le résultat est un entier, l'entier correspondant.
"""
def somme(L,M):
	return [(L[0]*M[1]+M[0]*L[1]),(L[1]*M[1])]

print(somme([24, 20],[3, 9]))

"""
La suite de Fibonacci est définie par F0=0, F1=1 et pour tout n⩾2, Fn=Fn−1+Fn−2. Ecrire la fonction sommefibo(j) qui renvoie la somme des j premiers termes de la suite de Fibonacci.
"""
def sommefibo(j):
    L = [0,1,1]
    s = 0
    i = 0
    while i < j :
        s += L[0]
        L[0] = L[1]
        L[1] = L[2]
        L[2] = L[0] + L[1]

        i += 1
    return s

"""
Soit L une liste de n entiers. On se fixe deux entiers S et p<n. On cherche alors s'il existe dans la liste, p+1 éléments consécutifs dont la somme est au moins égal à S, i.e. on cherche les indices k tels que ∑p+ki=kL[i]⩾S

.

Ecrire la fonction recherche(L,S,p)
qui évalue pour tout entier k la valeur ∑p+ki=kL[i] et qui renvoie sous forme de liste les entiers k pour lesquels cette somme est supérieure ou égale à S

.
"""
def recherche(L,S,p):
	k=0
	liste =[]
	while p+k<len(L):
		som=0
		for el in range(k,p+k+1):
			som+=L[el]
		if som>=S :
			liste+=[k,]
		k+=1
	return liste

"""
Dans l'exercice précédent, on pose Sk=∑p+ki=kL[i]. Que vaut Sk+1 en fonction de Sk ? Déduisez-en une fonction recherche2(L,S,p)

qui effectue le travail précédent en un temps d'exécution linéaire.
"""
def recherche2(L,S,p):
	liste=[]
	som=0
	for el in range(p+1):
		som+=L[el]
	if som>=S:
		liste+=[0]
	k=1
	deb=0
	fin=p
	while k+p<len(L):
		som = som+L[fin+1]-L[deb]
		fin+=1
		deb+=1
		if som>=S:
			liste+=[k,]
		k+=1
	return liste 


"""
Pour n∈N, on appelle diviseur propre de n tout diviseur de n excepté n

lui même.

Exemple : pour n=6
, les diviseurs propres de n

sont les entiers, 1, 2 et 3.

Ecrire la fonction som_div_propres(n)
qui renvoie la somme des diviseurs propres de l'entier n.
"""
def som_div_propres(n):
    return sum(div_propres(n))


def div_propres(n):
    if n == 1:
        return set()
    l = {1}
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            l.add(i)
            l.add(n//i)
        i += 1
    return l




"""
Ecrire la fonction minimum(L) qui renvoie la valeur du plus petit élément de L

. Ecrire cet algorithme une boucle while.

Eexmple : pour L=[3,2,5,7,2]


minimum(L)
renvoie 2.
"""
def minimum(L):
    mini=L[0]
    for el in L :
        if el<mini :
            mini=el
    return mini
    
"""
Ecrire la fonction minimum_posi(L) qui renvoie sous forme de liste la ou les positions du plus petit élément de L

.

Eexmple : pour L=[3,2,5,7,2]


minimum_posi(L)
renvoie [1,4].
"""
def minimum_posi(L):
    mini=L[0]
    liste=[0]
    for i in range(1,len(L)):
        if L[i]<mini :
            liste=[i]
            mini=L[i]
        elif L[i]==mini:
            liste+=[i,]
    return liste


"""
Ecrire la fonction minimum2(L) qui renvoie la valeur du deuxième plus petit élément de L, la liste  L

n'étant composée que d'éléments distincts.

Eexmple : pour L=[3,5,7,2,4]


minimum2(L)
renvoie 3.
"""
def minimum2(L):
    min1=L[0]
    min2=L[1]
    if min1>min2:
        qq=min1
        min1=min2
        min2=qq
    for i in range(2,len(L)):
        if L[i]<min1:
            min2=min1
            min1=L[i]
        elif L[i]<min2:
            min2=L[i]
    return min2


"""
Le tri à bulles consiste à partir du dernier élément d'une liste et à le comparer à l'avant dernier.

    Si le dernier élément est plus petit que l'avant dernier, on échange les deux éléments,
     sinon on ne fait rien. 

On recommence ce principe de comparaison à partir de l'avant dernier élément en le comparant avec l'élément qui le précède et ainsi de suite.

On s'arrête lorsque l'on effectue une comparaison avec le premier élément. A cette étape de l'algorithme, le plus petit élément de la liste se trouve en première position.

On recommence alors le processus en partant du dernier élément et en effectuant des comparaisons successives jusqu'à atteindre le deuxième élément et ainsi de suite ...

Ecrire la fonction tri_bulle(L)
qui renvoie la liste des éléments de L rangés dans l'ordre croissant.

def tri_bulle(L):
    i=len(L)-1
    j=0
    modifi=1
    while j<len(L) and modifi==1:
        modifi=0
        while i>j :
            if L[i]<L[i-1]:
                qq=L[i]
                L[i]=L[i-1]
                L[i-1]=qq
                modifi=1
            i-=1
        i=len(L)-1
    return L
"""
def tri_bulle(L):
    d = len(L)
    while d > 0:
        for i in range(d - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
        d -= 1
    return L
 

"""
Soit A une liste de longueur n

, on considère la méthode de tri suivante nommée tri par extraction:

    On cherche le plus petit élément de la liste. Soit j

sa position, on échange alors le premier élément de la liste avec l'élément en position j

    .
    On considère à présent la liste à partir du 2ème élément , et on cherche dans cette sous-liste, le plus petit élément que l'on permutera (une fois trouvé), avec le deuxième élément.
    On recommence ainsi le processus jusqu'à  la recherche du plus petit élément dans la sous-liste constituée de l'avant dernier élément et du dernier élément.

Ecrire la fonction tri(L)
qui renvoie sous forme de liste les éléments de la liste L rangés dans l'ordre croissant.
"""

def tri(L):
    for i in range(len(L) - 1):
        imin = i
        for j in range(i + 1, len(L)):
            if L[j] < L[imin]:
                imin = j
        L[i], L[imin] = L[imin], L[i]
    return L



"""
On veut  partitionner une liste dont les éléments ne prennent que 10 valeurs (de 0 à 9) en respectant les critère suivants :

    tous les éléments dont la valeur est strictement inférieure à 3 doivent se retrouver au début de la liste,
    on doit trouver ensuite tous les éléments dont la valeur est comprise entre 3 et 6,
    ceux de valeur strictement supérieure à 6 sont en fin de liste.

Exemple :
Liste 	: 	3 	  	6 	  	9 	  	1 	  	7 	  	9 	  	8 	  	0 	  	4 	  	6
Liste partitionnée
	: 	1 	  	0 	  	3 	  	6 	  	4 	  	6 	  	9 	  	7 	  	9 	  	8


On remarquera que la solution n'est pas unique puisqu'à toute permutation de chacune des 3 parties correspond une liste qui satisfait le critère de classement. Pour résoudre un tel problème on considère les 4 intervalles suivants:

    [1,d1[

  : intervalle des indices des éléments de la liste strictement inférieurs à 3,
[d1,i[
: intervalle des indices des éléments de la liste compris entre 3 et 6,
[i,d2]
: intervalle des indices des éléments de la liste en cours de traitement par l'algorithme,
]d2,n[

    : intervalle des indices des éléments de la liste strictement supérieurs à 6.

Quelles sont les valeurs d'initialisation de d1
, d2 et i

?

Situation intermédiaire: à l'étape i

de l'algorithme, la situation est la suivante :



Discutez en fonction de la valeur du ième élément de la liste  des actions à réaliser et de la mise à  jour des variables i
, d1 et d2

afin que la situation décrite soit encore vraie une fois que l'on se trouve sur l'élément i+1.

Déduisez-en la fonction partition(L)
qui renvoie les éléments de la liste L une fois l'algorithme de partitionnement appliqué. Attention en Python les indices de liste débute à 0 ! 

"""
def partition(L) :
    d1 = 0
    d2 = 0
    fin = len(L)-1
    while d2 <= fin :
        if 3<=L[d2]<=6 :
            d2 += 1
        elif L[d2]>6 :
            L[fin] ,L[d2] =L[d1] , L[fin]
            fin -= 1
        else :
            L[d2] ,L[d1] =L[d1] ,L[d2]
            d2 += 1
            d& += 1
    return L

"""
Ecrire la fonction puiss(x,y,n) qui calcule xymodn.
"""

def puissance(x,y,n) :
	e = y
	r = 1
	p = x 
	while (e > 0) :
		if e & 1 == 1 :
			r = r * p
		p *= p
		e = e >> 1
	return r % n 