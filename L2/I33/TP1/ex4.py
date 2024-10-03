def sommefibo(j):
    if j == 1:
        return 0
    U0 = 0
    U1 = 1
    som = 1
    i = 2
    while i<j:
        i += 1
        U2 = U0 + U1
        aux = U1
        U1 = U2
        U0 = aux
        som += U2
    return som
print(sommefibo(19))
