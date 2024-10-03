def somme_ind_pair(L):
    i = 0
    som = 0
    while i<len(L):
        som +=L[i]
        i += 2
    return som

print(somme_ind_pair([3,2,5,7,4,1]))

