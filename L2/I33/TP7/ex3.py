def is_symetrique(M):
    if len(M) != len(M[0]):
        return False
    i = 0
    
    while i < len(M):
        j = 0
        while j < len(M):
            if M[j][i] != M[i][j]:
                return False
            j += 1
        i += 1
    return True
