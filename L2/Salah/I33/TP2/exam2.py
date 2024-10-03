"""
On représente un ensemble A d'entiers positifs par une liste Python (non nécessairement ordonnée) contenant les éléments de A

.

Exemple: l'ensemble A={2,5,8,9}

peut être représenté par la liste [2,5,8,9] ou [9,5,2,8].

On décide à présent de représenter un ensemble A
d'entiers positifs par un unique entier t de la façon suivante :  au début t vaut zéro. Pour chaque élément e de l'ensemble A, on met un 1 en position e dans la décomposition en base 2 de t

.

Exemple : Si A =[2,5,8,9], on obtiendra ainsi t

=804. En effet en base 2,  l'entier 804  s'écrit  1 1 0 0 1 0 0 1 0 0. Les positions sont numérotées à partir de 0 et lues de droite à gauche. On constate donc bien ici qu'il y a un 1 en position 2, 5, 8 et 9.

Afin de positionner un 1 dans la décomposition en base 2 d'un entier t

, il faut utiliser les opérateurs de décalage << et l'opérateur logique |  (ou-logique).

Ecrire la fonction ens_to_int(A) qui à partir d'une liste A représentant un ensemble renvoie l'entier codant cet ensemble. Cette fonction s'écrit en une seule boucle, sans utiliser les opérateurs *, **, +, -, /
"""


def ens_to_int(A):
	res = 0
	for n in A :
		i=1<<n
		res= res|i
		#print(bin(res))
	return res	
#print(ens_to_int([2,5,8,9]))	

"""
A partir d'un entier t

codant un ensemble comme expliqué dans l'exercice précédent écrire la fonction int_to_ens(t) qui renvoie la liste des éléments de cet ensemble.


Exemple : Si t = 804 , la fonction renvoie la liste [2,5,8,9]. Cette fonction s'écrit en une seule boucle, sans utiliser les opérateurs *, **,  /, %
"""
def int_to_ens(t):
	i=0
	L=[]
	while t!=0 :
		if t&1 :
			L+=[i,]
		i=i+1
		t=t>>1
	return L
#print(int_to_ens(804))

"""
A partir d'un entier t codant un ensemble A, écrire la fonction ajoute_dans(t,e) qui renvoie l'entier codant l'ensemble correspondant à A

auquel on a ajouté l'élément e.

Cette fonction s'écrit en une seule ligne !
"""
def ajout_dans(t,e):
	return t|(1<<e)
#print(ajout_dans(366724,10))


"""
A partir d'un entier t codant un ensemble A, écrire la fonction retire_dans(t,e) qui renvoie l'entier codant l'ensemble correspondant à A

auquel on a retiré l'élément e.

Cette fonction s'écrit en une seule ligne !
"""
def retire_dans(t,e):
	return t^(1<<e) 
#print(retire_dans(236910,11))

"""
A partir d'un entier t codant un ensemble, écrire la fonction est_dans(t,e) qui renvoie True si e est un élément de l'ensemble représenté par t et False

sinon.

Cette fonction s'écrit en une seule ligne !
"""
def est_dans(t,e):
	return ( 1==(t>>e)&1 )

"""
Soient t1  et t2 deux entiers codant respectivement les ensembles A et B, écrire la fonction est_inclus_dans(t1,t2) qui renvoie True si A⊂B, renvoie False

sinon.

Cette fonction s'écrit en une seule ligne !
"""	
def est_inclus_dans(t1,t2):
	return t1&t2==t1

"""
Soient t1  et t2 deux entiers codant respectivement les ensembles A et B, écrire la fonction intersection(t1,t2) qui renvoie l'entier codant l'ensemble A∩B

.

Cette fonction s'écrit en une seule ligne !
"""	
def intersection(t1,t2):
	return t1&t2


"""
Soient t1  et t2 deux entiers codant respectivement les ensembles A et B, écrire la fonction union(t1,t2) qui renvoie l'entier codant l'ensemble A∪B

.

Cette fonction s'écrit en une seule ligne !
"""	
def union(t1,t2):
    return t1|t2
    
"""
Soient t1  et t2 deux entiers codant respectivement les ensembles A et B, on note A∖B la différence ensembliste de A et B, il s'agit des éléments qui appartiennent à A mais qui n'appartiennent pas à B

.

Exemple : si A={2,3,6,7,8}
et B={1,3,7,9} alors A∖B={2,6,8}


Ecrire la fonction difference(t1,t2) qui renvoie l'entier codant A∖B

.

Cette fonction s'écrit en une seule ligne !
""" 
def difference(t1,t2):
	 return (t1^t2)&t1 


"""
Soient t1  et t2 deux entiers codant respectivement les ensembles A et B, on note AΔB la différence symétrique de A et B, il s'agit des éléments qui appartiennent soit à A soit à B mais pas au deux.
"""
def difference_sym(t1,t2):
	return t1^t2
"""
Soient a et n deux entiers, l'algorithme d'Euclide étendu permet de calculer u et v dans Z tels que au+vn=pgcd(a,n)

.

Ecrire la fonction euclide_e(a,n)
qui renvoie la liste [u,v,pgcd(a,n)]

.

Voici un exemple du déroulement de cet algorithme lorsque a=54
et n=39. La fonction doit renvoyer la liste [-5,7,3]. Vous devez gérer 4 variables u, v, u1 et v1 qui seront initialisées comme suit : u=1, v=0, u1=0 et v1=1.  Ceci correspond aux deux premières lignes du tableau. Vous devez ensuite gérer la mise à jour de ces variables ainsi que celle de a et de n. Lorsque n atteint la valeur 0, la valeur courante de a contient le pgcd de a et de n et u et v contiennent les valeurs recherchées. 
"""
def euclide_e(a,n):
    u , v, u1, v1= 1 ,0 ,0 ,1
    while a%n>0 :
    	q=a//n
    	a ,n = n ,a%n
    	n_u1=u-u1*q
    	n_v1=v-v1*q
    	u ,v = u1 ,v1
    	u1 ,v1 = n_u1 ,n_v1
    a ,n = n ,a%n
    return [u1,v1,a] 
    
"""
Soit p un nombre premier et soit a∈(Z/pZ)∗

.

Ecrire la fonction inverse(a,p)
qui renvoie le symétrique de l'élément a dans (Z/pZ)∗. Cet algorithme s'écrit en utilisant une seule boucle while.
"""
def inverse(a,p):
    n, a = a, p
    u , v, u1, v1= 1 ,0 ,0 ,1
    while a%n>0 :
    	q=a//n
    	a ,n = n ,a%n
    	n_u1=u-u1*q
    	n_v1=v-v1*q
    	u ,v = u1 ,v1
    	u1 ,v1 = n_u1 ,n_v1
    a ,n = n ,a%n
    return (v1+p)%p

"""
La fonction φ d'Euler est définie pour tout entier n

par :

φ(n)=card({i∈N t.q. i⩽n et pgcd(i,n)=1})

Ecrire la fonction euler_phi(n)

qui réalise ce calcul.
"""
def euler_phi(n):
    cpt=0
    for i in range(1,n) : 
        m=n
        while m!=0 :
            i, m = m, i%m
        if i ==1 :
            cpt+=1
    return cpt


"""
L'objectif de cet exercice est de comprendre comment est programmé la fonction pow(x,y,n) de Python qui permet de réaliser de façon efficace le calcul de z=xymod n

.

Supposons que la décomposition en base 2 de l'entier y
soit égale à [a3,a2,a1,a0], c'est à dire que y=a0+2a1+22a2+23a3 avec ai=0 ou 1

. Alors

xy=xa0+2a1+22a2+23a3=xa0×(x2)a1×(x4)a2×(x8)a3

.

L'algorithme à écrire va parcourir un à un les symboles de la décomposition en base 2 de l'entier y
en partant de a0. Remarquons que pour chaque symbole lu, on a besoin successivement de x, x2, x4 et x8 et que x4=(x2)2 et x8=(x4)2. Ainsi x

devra être mis à jour au fur et à mesure de l'algorithme afin de toujours être élevé à la bonne puissance, une simple multiplication permet de réaliser cette mise à jour.

En partant de z=1
, on va multiplier z par x uniquement si a0 = 1, puis on multipliera la valeur de z par (x2)a1 uniquement si a1=1 et ainsi de suite.  Ces opérations seront effectuées modulo l'entier n y compris la mise à jour de la variable x

.

Ecrire la fontion puissance(x,y,n)
qui réalise le calcul de xy mod n. L'algorithme utilise une unique boucle while et n'utilise pas l'opérateur /.  L'opérateur % est uniquement utilisé pour la réduction modulo n.
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

def puissance_2(x,y,n):
	res = 0
	while y != 0 :
		if y&1==1 :
			if res==0 :
				res = 1
			res*=x
		res=res%n
		x=x*x
		y = y>>1
	return res 
	
print(puissance(3,3,9))
print(pow(3,3,9))











