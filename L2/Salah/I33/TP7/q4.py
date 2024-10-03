def norme(M):
    norme1 = -1
    p = len(M)
    n = len(M[0])

    for j in range(n):
        n1 = 0
        for i in range(p):
            n1 += abs(M[i][j])
        if n1 > norme1:
            norme1 = n1

    return norme1
