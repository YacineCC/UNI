def matvec(M,V):
    res = []
    i = 0
    while i < len(M):
        j = 0
        som = 0
        while j < (len(M[0])):
            som += M[i][j] * V[j]
            j += 1
        res += [som]
        i += 1
    return res
