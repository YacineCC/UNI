On considère dans cet exercice l'ensemble Mn(R), i.e. les matrices carrés n×n à coefficients dans R

. 

Ecrire la fonction det(A)
qui renvoie la valeur du déterminant de A∈Mn(R), en utilisant la méthode d'élimination de Gauss (la version modifiée) vue en cours.  On rappelle que pour cette méthode, chaque ligne Li située sous la ligne Lj contenant le pivot subit la transformation Li←ajjLi−aijLj. 

def det(A):
    s = 1
    d = 1
    p = 1
    j = 0
    n = len(A)
    while j < n-1 :
        i = j
        while i < n and A[i][j] == 0 :
            i += 1
        if i > n-1 :
            return 0
        if i > j :
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            s = -s
        d *= A[j][j]
        for i in range(j+1,n):
            tmp = [0]*(n)
            for el in range(n):
                tmp[el] = (A[j][j]*A[i][el]) - (A[i][j]*A[j][el])
            A[i] = tmp
            p = p * A[j][j]
        j += 1
    d = (d*A[n-1][n-1]*s)/p
    return d


On considère dans cet exercice l'ensemble Mn(Z/26Z), i.e. les matrices carrés n×n à coefficients dans Z/26Z

. 

Ecrire la fonction det(A)
qui renvoie la valeur du déterminant de A∈Mn(Z/26Z), en utilisant la méthode d'élimination de Gauss (la version modifiée) vue en cours.  On rappelle que pour cette méthode, chaque ligne Li située sous la ligne Lj contenant le pivot subit la transformation Li←ajjLi−aijLj

. 

IMPORTANT : il faudra à chaque fois s'assurer que le pivot choisi est premier avec 26, donc impair et non multiple de 13. Les opérations sont à effectuer dans Z/26Z

.

Remarque : si pgcd(a, 26) = 1, alors l'inverse de a modulo 26 peut être calculé avec l'opération pow(a,11,26), car ϕ(26)=12
.

def det(A):
    s = 1
    d = 1
    p = 1
    j = 0
    n = len(A)
    while j < n-1 :
        i = j
        while i < n and A[i][j] == 0 and A[i][j]%2 != 0 and A[i][j]%13 != 0 :
            i += 1
        if i > n-1 :
            return 0
        if i > j :
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            s = -s
        d *= A[j][j]
        for i in range(j+1,n):
            tmp = [0]*(n)
            for el in range(n):
                tmp[el] = ((A[j][j]*A[i][el]) - (A[i][j]*A[j][el])) % 26
            A[i] = tmp
            p = (p * A[j][j]) % 26
        j += 1
    p = pow(p,11,26)
    d = (d*A[n-1][n-1]*s) * p
    return d % 26


Soit A∈Mn(R). On dit que A possède une décomposition LU, s'il existe une matrice triangulaire inférieure L∈Mn(R) et une matrice triangulaire supérieure U∈Mn(R) tel que A=L×U

.

Ecrire la fonction is_LU(A,L,U) qui renvoie True si :

    L est bien une matrice triangulaire inférieure, et
    U est bien une matrice triangulaire supérieure, et
    A = L x U

dans le cas contraire la fonction doit renvoyer False.

Une matrice est codée en Python par une liste de listes et lors de l'évaluation de votre fonction cette dernière ne sera appelée qu'avec des matrices carrées, il est donc inutile de vérifier les dimensions des matrices. 

ATTENTION : votre code sera exécutée pour 3 exemples sur des matrices de taille importante, il est donc primordial d'écrire votre code afin qu'il soit le plus efficace possible. Dans le cas contraire, vous risquez de dépasser la limite de temps autorisée par Moodle.Pour ces 3 exemples, la valeur des matrices ne sera pas affichée dans le résultat renvoyé par Moodle car ceci dépasse la limite d'affichage autorisée.



Soit A∈Mn(R) une matrice possédant une décomposition LU

.

Ecrire la fonction transpose_LU(L,U) qui renvoie  la matrice transposée de A
à partir de sa décomposition LU

. Cette fonction ne nécessite que 3 boucles.

def transpose_LU(L,U):
    n = len(L)
    res = []
    j = 0
    while j < n :
        tmp = []
        i = 0
        tmp = []
        while i < n :
            f = 0
            som = 0
            while f < n :
                som += L[i][f]*U[f][j]
                f += 1
            tmp += [som,]
            i += 1
        res += tmp,
        j += 1
    return res


Soit A une matrice triangulaire inférieure à n lignes et n colonnes. Soit b un vecteur colonne à n

composantes.

On cherche le vecteur colonne x
à n composantes tel que A.x=b

.

Exemple: pour n=3
, considérons la matrice A=⎛⎝⎜21−1022001⎞⎠⎟ et le vecteur b=
⎛⎝⎜123⎞⎠⎟

Le vecteur recherché est x=⎛⎝⎜0.50.752⎞⎠⎟

En utilisant la forme particulière d'une matrice triangulaire inférieure, écrire la fonction resolution(A,b)
qui renvoie le vecteur x solution de l'équation Ax=b. 

def resolution(A,b):
    res = [b[0]/A[0][0]]
    for i in range(1,len(b)): 
        s = 0
        for j in range(i):
            s += A[i][j]*res[j]
        res += [(b[i]-s)/A[i][i]]
    return res
    

Soit A une matrice triangulaire supérieure à n lignes et n colonnes. Soit b un vecteur colonne à n

composantes.

On cherche le vecteur colonne x
à n composantes tel que A.x=b.

def resolution(A,b):
    n = len(b)
    res= [0]*n
    #res[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-1,-1,-1): 
        s = 0
        for j in range(n-1,i-1,-1):
            s += A[i][j]*res[j]
        res[i] = (b[i]-s)/A[i][i]
    return res


Soit A∈Mn(R) une matrice possédant une décomposition LU. Soit b un vecteur colonne à n

composantes.

On cherche le vecteur colonne x
à n composantes tel que A×x=b. Etant donné que A=L×U ceci est donc équivalent à trouver x tel que L×U×x=b

.

Ceci peut se décomposer en deux étapes :

    Trouver un vecteur y

à n colonnes tel que L×y=b
,
Chercher alors le vecteur x
tel que U×x=y.

def resolution(L,U,b):
    y = [b[0]/L[0][0]]
    for i in range(1,len(b)): 
        s = 0
        for j in range(i):
            s += L[i][j]*y[j]
        y += [(b[i]-s)/L[i][i]]
    n = len(y)
    x = [0]*n
    #res[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-1,-1,-1): 
        s = 0
        for j in range(n-1,i-1,-1):
            s += U[i][j]*x[j]
        x[i] = (y[i]-s)/U[i][i]
    return x
