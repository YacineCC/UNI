def decompose(n):
    x = n
    decomp = []
    puissance = 0

    while x % 2 == 0:
        x = x // 2
        puissance += 1
    if puissance > 0:
        decomp.append([2, puissance])
    i = 3
    while x > 1:
        puissance = 0
        while x % i == 0:
            x = x // i
            puissance += 1
        if puissance > 0:
            decomp.append([i, puissance])
        i += 2
    return decomp




def euler_phi(n):
    
    phi = 1
    dec = decompose(n)
    for facteur_premier in dec:
        phi = phi * (facteur_premier[0] ** facteur_premier[1] - facteur_premier[0] ** (facteur_premier[1] - 1) )

    return phi



print(euler_phi(10800))

