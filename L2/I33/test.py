def somme_pair(L):
    som = 0
    for i in L:
        if i % 2 == 0:
            som += i
    return som

L = [3,2,5,7,4,1]
print(somme_pair(L))

def somme_ind_pair(L):
    som = 0
    i = 0
    while i < len(L):

        som += L[i]
        i += 2
    return som

print(somme_ind_pair(L))
def pgcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a 
print(pgcd(6,3))


def somme(L,M):
    tab = []
    a = L[1]
    b = M[1]
    if a > b:
        for i in range(1,b):
            if a % i == 0:
                tab += [i]
    else:
        for i in range(1,a):
            if b % i == 0:
                tab += [i]
    return tab

L = [8,4]
M = [9,5]

print(somme(L,M))

