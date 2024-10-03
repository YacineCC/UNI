def transpose(M):
    res = []
    for i in range(len(M[0])) :
        tmp = []
        for l in M :
            tmp += [l[i],]
        res += tmp,
    return res
    
    
Ecrire la fonction gensym(n,t) qui renvoie une matrice symétrique à n lignes et n colonnes composée d'entiers choisis aléatoirement dans l'intervalle [0,t−1]. Servez-vous de la fonction gentrianginf(n,t), inutile de la redéfinir.  Cette fonction n'utilise pas l'instruction if


Rappel: la fonction gentrianginf(n,t)
renvoie une matrice triangulaire inférieure à n lignes et n colonnes composée d'entiers choisis aléatoirement dans l'intervalle [0,t−1].

def gensym(n,t):
    m = gentrianginf(n,t)
    i = 1
    while i < n :
        j = 0
        while j < i :
            m[j][i] = m[i][j]
            j += 1
        i += 1
    return m


Ecrire la fonction is_symetrique(M) qui renvoie True si M est une matrice symétrique et False sinon. Attention M peut être une matrice quelconque.
def is_symetrique(M):
    i = 1
    if len(M) != len(M[0]):
        return False
    while i < len(M) :
        j = 0
        while j < i and M[j][i] == M[i][j] :
            j += 1
        if j != i:
            return False
        i += 1
    return i == len(M)
    
    
Soit M une matrice p×n. La  norme 1 de M

est définie comme :

max1⩽j⩽n(∑pi=1|mij|)

Il s'agit donc de calculer pour chaque colonne la somme des valeurs absolues des éléments et de trouver la plus grande de ces sommes.

Ecrire la fonction norme(M)
qui renvoie la norme 1 de M, cette fonction s'écrit sans utiliser la fonction max de Python.
def norme(M):
    maxi = 0
    for i in range(len(M[0])) :
        som = 0
        for l in M :
            som += abs(l[i])
        if som > maxi :
            maxi = som
    return maxi
    



Ecrire la fonction matvec(M,V)

qui renvoie le résultat du produit de la matrice M par le vecteur V.

Par exemple, l'appel de matvec([[2, 1, 2], [2, 1, 2], [2, 1, 0]],[1,0,2])
doit renvoyer la liste [6,6,2]
def matvec(M,V):
    res = []
    for i in range(len(M)) :
        j = 0
        som = 0
        while j < len(V) :
            som += M[i][j]*V[j]
            j += 1
        res += [som,]
    return res
    
Écrire la fonction matmat(A,B) qui renvoie le résultat du produit de la matrice A par la matrice B

.

Par exemple, l'appel de matmat([[1, 1, 2], [1, 0, 2]],[[1, 2, 0, 1], [1, 1, 1, 0], [0, 2, 2, 1]])
doit renvoyer la liste [[2, 7, 5, 3], [1, 6, 4, 3]]
def matmat(A,B):
    res = []
    i = 0
    while i < len(A) :
        tmp = []
        j = 0
        tmp = []
        while j < len(B[0]) :
            f = 0
            som = 0
            while f < len(B) :
                som += A[i][f]*B[f][j]
                f += 1
            tmp += [som,]
            j += 1
        res += tmp,
        i += 1
    return res
    
    
On considère dans cet exercice l'ensemble Mn(F2), i.e. les matrices carrés n×n à coefficients dans F2

. Chaque ligne d'une matrice de cette espace ne comporte que des 0 et des 1, on peut donc considérer une ligne de la matrice comme la décomposition en base 2 d'un certain entier. On peut donc représenter une telle matrice par une liste d'entiers.

Par exemple la matrice

⎡⎣⎢110011010111⎤⎦⎥

peut être représentée en Python par la liste [9,15,5]
. De même un vecteur d'éléments de F2

peut être considéré comme la décomposition en base 2 d'un certain entier et peut donc être représenté par un entier.

Par exemple le vecteur 

⎡⎣⎢⎢⎢0111⎤⎦⎥⎥⎥

peut être représenté par l'entier 7.

Le produit matrice-vecteur se fait en utilisant l'arithmétique de F2

, ainsi

⎡⎣⎢110011010111⎤⎦⎥⎡⎣⎢⎢⎢0111⎤⎦⎥⎥⎥=⎡⎣⎢110⎤⎦⎥

Le résultat de l'opération précédente peut être représenté par l'entier 6.

L'objectif de cet exercice est d'écrire la fonction prod_mat_vec_F2
qui prend en paramètre une matrice de F2 représentée sous forme de liste d'entiers, un vecteur représenté par un entier, qui réalise le produit matrice vecteur en considérant l'arithmétique de F2

et qui renvoie sous forme d'un entier le vecteur résultant.

En Python, l'arithmétique de F2
se fait en utilisant les opérateurs logiques ^ et &. Vous devrez écrire votre programme en utilisant uniquement les opérateurs logiques ^, &,  <<, et |

. Tout autre opérateur arithmétique est interdit.

Il suffit d'une seule boucle pour écrire le programme. Votre programme s'exécutera dans un environnement dans lequel vous avez accès à la fonction poids
qui renvoie le nombre de 1 dans la décomposition en base 2 d'un entier. Ainsi poids(17)=2

car en base 2, l'entier 17 s'écrit 10001.

Pour l'exemple traité dans l'énoncé, l'appel à prod_mat_vec_F2([9,15,5],7)
doit renvoyer l'entier 6
def prod_mat_vec_F2(M,V):
    res = 0
    for i, m in enumerate(reversed(M)):
        bit = poids(m & V) & 1
        res = res ^ (bit << i)
    return res


Soit P(x) un polynôme irréductible sur F2 de degré m utilisé pour construire le corps (F2m,+,×). On considère dans cet exercice l'ensemble Mn(F2m), i.e. les matrices carrés n×n à coefficients dans F2m

.  L'objectif est de multiplier les matrices de cet ensemble.

Votre fonction s'exécutera dans un environnement où vous avez accès à la fonction multiplie(a,b,P) qui pour deux entiers a et b représentant deux éléments u et v du corps fini construit à partir de P
, renvoie l'entier représentant le résultat du produit de u par v dans le corps fini construit à partir de P

. 

Le polynôme P

est codé par un entier dont la décomposition en base 2 représente la liste des coefficients du polynôme.

Ecrire la fonction matmat(A,B,P)
qui renvoie le résultat du produit de la matrice A par la matrice B,  avec A,B∈Mn(F2m)

.

Note : les coefficients de A
et de B

sont les représentations des éléments correspondants dans le corps fini.

Par exemple, l'appel de matmat([[14, 8, 9], [0, 4, 12], [12, 10, 12]],[[11, 12, 8], [7, 8, 15], [4, 9, 5]],19)
doit renvoyer la liste [[7, 5, 3], [10, 0, 0], [11, 6, 15]]

def matmat(A, B, P):
    p = len(A)
    k = len(B)
    n = len(B[0])

    result = []
    for i in range(p):
        result.append([])
        for j in range(n):
            val = 0

            for u in range(k):
                val = val ^ multiplie(A[i][u], B[u][j], P)

            result[i].append(val)

    return result

