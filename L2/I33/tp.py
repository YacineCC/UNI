def pgcd(a,b):
    while b!= 0:
        a,b = b,a%b

    return a 

def somme(L,M):

    aux = [L[0]*M[1]+M[0]*L[1],L[1]*M[1]]

    A = aux[0]
    B = aux[1]
    if A % B != 0:

        A = A // pgcd(aux[0],aux[1])
        B = B // pgcd(aux[0],aux[1])
        
        return [A,B]

    else:
        return A//B

L = [6,2]
M = [9,3]



def sommefibo(j):
    F0 = 0
    F1 = 1
    som = 0

    i = 1
    while i < j:
        F2 = F1 + F0
        F0 = F1
        som += F1
        F1 = F2
        i += 1
    return som
print(sommefibo(10))

"""def recherche(L,S,p):
    tab = []
    i = 0

    while i < len(L):"""

def som_div_propre(n):
    if n == 1:
        return 0

    som = 1
    i = 2

    while i < int(n**0.5)+1:
        if n % i == 0:
            som += i
            if i != n//i:
                som += n//i
        i += 1

    return som

print(som_div_propre(90))
print(som_div_propre(36))

def mini(L):
    i = 0
    minim = L[0]
    while i < len(L):
        if L[i] < minim:
            minim = L[i]
        i += 1
    return minim
L = [3,2,5,7,2]
print(mini(L))
def minimum_posi(L):
    tab = []
    i = 1
    minim = L[0]
    while i < len(L):
        if L[i] <= minim:
            tab += [i]

            minim = L[i]
        i += 1
    return tab

L = [3,2,5,7,2]
print(minimum_posi(L))
