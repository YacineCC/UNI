
"""
Ecrire la fonction generateurs(n) qui renvoie sous forme de liste les générateurs du groupe (Z/nZ,+). Votre code s'exécutera dans un environnement où la fonction  pgcd(a,b)

existe, inutile de la redéfinir. Cette fonction s'écrit avec une seule boucle.

Exemple : generateurs(6)
renvoie la liste [1,5]
"""
def generateurs(n):
    L=[]
    i=1
    while i<n :
        if pgcd(i,n)==1 :
            L+=[i,]
        i+=1
    return L
    
   
"""
Soit a un élément de (Z/nZ,+,×), écrire la fonction sous_groupe_gen_add(a,n) qui renvoie la liste des éléments du sous-groupe <a>+

.

Exemple : pour n = 10 et a = 4,  sous_groupe_gen_add(4,10)

renvoie la liste  [4,8,2,6,0]
"""
 
def sous_groupe_gen_add(a,n):
    L=[a,]
    i=a
    a=(a+a)%n
    while a not in(L) :
        L+=[a,]
        a=(a+i)%n
    return L
    
"""
Tout entier n se décompose de façon unique sous la forme n=∏ipeii où les pi sont des nombres premiers. L'objectif de cet exercice est de programmer la fonction decompose(n) qui renvoie la liste des pi

.

Exemple : decompose(99999876400)
renvoie la liste [2,5,29,1483,5813] car 99999876400=24×52×29×1483×5813

.

Pour obtenir la décomposition de l'entier n

en facteurs premiers, on peut procéder de la façon suivante:

    on commence par regarder si n

est pair et si c'est le cas on divise n
par 2 tant que cela est possible et 2 est ajouté à la liste des facteurs premiers.
en parcourant les entiers i par pas de 2 à partir de i=3
, si i divise n on le rajoute dans la liste et on divise n par i tant que cela est possible. On arrête ce parcours lorsque n=1.

"""
def decompose(n):
    L=[]
    if n%2==0 :
        L+=[2]
        while n%2==0 :
            n=n/2
    i=3
    while n!=1:
        if n%i==0 :
            L+=[i,]
            while n%i==0 :
                n=n/i
        i+=2
    return n
    
"""
Soit p un nombre premier, pour vérifier si un élément g∈(Z/pZ)∗ est un générateur, il suffit de vérifier si gp−1k≠1 mod p, pour tout diviseur premier k de p−1

.

Ecrire la fonction generateurs(p)
qui renvoie la liste des générateurs de (Z/pZ)∗. Votre fonction sera évaluée dans un environnement où la fonction decompose(n) existe, il est donc inutile de la redéfinir. Vous  utiliserez la fonction python pow(x,y,n) qui calcule de façon efficace xy(modn). Aucun module n'est à inclure pour pouvoir utiliser cette fonction. Cet algorithme s'écrit en utilisant deux boucles.
"""    
    
def generateurs(p):
    div_p_1=decompose(p-1)
    L=[]
    i=2
    while i<p :
        condition = True
        for el in div_p_1:
            if pow(i,((p-1)//el),p)==1 :
                condition = False 
        if condition :
            L+=[i,]
        i+=1
    return L
    
"""
Un nombre premier de Sophie Germain est un nombre premier q tel que p=2q+1

soit aussi un nombre premier.

Par exemple, les 5 premiers entiers de Sophie Germain sont :

2,3,5,11,23


Ecrire la fonction generateur(p)
qui renvoie un générateur de (Z/pZ)∗ pour p=2q+1 avec q

premier.

Inutile de tester si p

est bien un premier de ce type, votre fonction ne sera évaluée qu'avec des premiers de ce type. Votre fonction s'écrit :

    avec une seule boucle,
    sans la boucle for,
    sans utiliser l'instruction if

    ,
    sans utiliser les opérateurs de comparaison <, >
    sans utiliser l'opérateur +.

 Vous utiliserez la fonction python pow(x,y,n)
qui calcule de façon efficace xy(modn)

.

Attention : le deuxième argument de la fonction pow(x,y,n)

doit être de type entier.

Vous utiliserez aussi la fonction randrange(a,b)
qui renvoie un entier aléatoire dans l'intervalle [a,b−1] (inutile d'importer la librairie random, votre fonction s'exécutera dans un environnement où cette librairie a déjà été importée).

"""    
    
def generateur(p):
    g=randrange(2,p-1)
    while pow(g,((p-1)//2),p)==1:
        g=randrange(2,p-1)
    return g
    
    
"""
Soit a un élément de (Z/nZ,+,×), écrire la fonction sous_groupe_gen_mult(a,n) qui renvoie la liste des éléments du sous-groupe <a>×

.

Exemple : pour n = 10 et a = 3,  sous_groupe_gen_mult(3,10)

renvoie la liste  [3,9,7,1].

Lors de la phase de test, votre fonction ne sera testée qu'avec des éléments a
de (Z/nZ)∗.
"""   
    
def sous_groupe_gen_mult(a,n):
    L=[a,]
    i=a
    a=(a*a)%n
    while a not in(L) :
        L+=[a,]
        a=(a*i)%n
    return L
    
"""
Soit n⩾2 un entier, écrire la fonction ord(a,n) qui renvoie la valeur de l'ordre additif de a dans (Z/nZ,+). Cette fonction s'écrit avec une unique boucle et sans les opérateurs +,* et -.
"""    
    
def ord(a,n):
	x , y = n ,a
	while y!=0 :
		x, y = y, x%y
	return n//x
	
"""
Ecrire la fonction is_of_order(a,t,n) qui renvoie True si a est d'ordre t dans(Z/nZ,+), False sinon. Cette fonction s'écrit sans utiliser de boucle et sans utiliser l'instruction if. Votre fonction sera évaluée dans un environnement où la fonction pgcd(a,b) existe.
"""	
def is_of_order(a,t,n):
    return (t==(n/pgcd(n,a)))
"""
Ecrire la fonction is_sym_add(x,y,n) qui renvoie True si y est le symétrique de x dans (Z/nZ,+), False sinon. Cette fonction s'écrit sans utiliser de boucle et sans utiliser l'instruction if.
"""   
def is_sym_add(x,y,n):
    return ((x+y)%n==0)
"""
Ecrire la fonction is_sym_mul(x,y,n) qui renvoie True si y est le symétrique de x dans (Z/nZ)∗, False sinon. Cette fonction s'écrit sans utiliser de boucle et sans utiliser l'instruction if.
"""   
def is_sym_mul(x,y,n):
    return ((x*y)%n==1)
"""
Pour représenter un élément x=ab de Q, on utilise une liste à 2 éléments [a,b]

.

Ecrire la fonction is_sym_add(x,y)
qui renvoie True si y est le symétrique de x dans (Q,+), False sinon. Cette fonction s'écrit sans utiliser de boucle et sans utiliser l'instruction if.
"""    
def is_sym_add(x,y):
    return ( (x[0]*y[1]) + (y[0]*x[1]) ) == 0
"""
Pour représenter un élément x=ab de Q, on utilise une liste à 2 éléments [a,b]

.

Ecrire la fonction is_sym_mul(x,y)
qui renvoie True si y est le symétrique de x dans (Q)∗, False sinon. Cette fonction s'écrit sans utiliser de boucle et sans utiliser l'instruction if et sans utiliser l'opérateur /.
"""  
def is_sym_mul(x,y):
    return (x[0]*y[0]) == (x[1]*y[1]) 

"""Soit p un nombre premier, écrire la fonction ord(a,p) qui renvoie la valeur de l'ordre multiplicatifde a dans (Z/pZ)∗

.

Cet algorithme s'écrit avec une seule boucle et fera O(p–√)
appels à la fonction pow(x,y,n) qui calcule de façon efficace xy mod n

.

Pensez à utiliser la propriété stipulant que l'ordre multiplicatif de a
est forcément un diviseur de p−1.
"""
def ord(a,p):
    i=1
    ordre=p-1
    while i*i <= (p-1) :
        if (p-1)%i==0 :
            if pow(a,i,p)==1 :
                ordre = min(ordre,i)
            elif pow(a,(p-1)//i,p)==1 :
                ordre = min(ordre,(p-1)//i)
        i+=1
    return ordre


"""
Dans un groupe (G,∘), si pour un élément a

, on a:

a∘a∘a∘⋯∘a=e
(où a  apparaît t

fois)

alors t
est un multiple de l'ordre a. Si de plus, pour tout diviseur j de t

, on a

a∘a∘a∘⋯∘a≠e
(où a  apparaît j

fois)

alors dans ce cas t
est égal à l'ordre de a

.


Ecrire la fonction is_of_order_mult(a,t,n)
qui renvoie True si a est d'ordre t dans(Z/nZ)∗, False sinon. Cette fonction devra pouvoir effectuer cette vérification en O(t√)

calculs.

Cette fonction utilise une unique boucle while et une seule instruction if.
"""
def is_of_order_mult(a,t,n):
    is_order = (a==1 and t==1) or (a!=1 and pow(a,t,n)==1)
    i = 2
    while i*i <= t and is_order :
        if t%i == 0 :
            is_order = is_order and pow(a,i,n)!=1 and pow(a,t//i,n)!=1 
        i += 1
    return is_order 
	

