def somme_pair(L):
    som = 0

    for i in L:

        if i %2 == 0:
            som += i
    return som

print(somme_pair([3,2,5,7,4,1]))
