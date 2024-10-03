def gensym(n,t):
    M = gentrianginf(n,t)
 
    i = 0
    while i < n:
        j = 0
        while j < n:
            M[j][i] = M[i][j]
            j += 1
        i += 1
    
    return M
