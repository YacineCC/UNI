from copy import deepcopy

def LineIndexMax(M, i1, i2, j):

    i = i1
    maxi = abs(M[i1][j])

    while i <= i2:

        if abs(M[i][j]) > maxi:
            maxi = abs(M[i][j])
            k = i
        i += 1
    
    return k


def LineMultScal(M, i, s):

    j = 0
    while j < len(M[i]):

        M[i][j] *= s 
        j += 1 

def LineAddMultScal(M, i, l, s):

    tmp = deepcopy(M[i])

    j = 0
    while j < len(M[i]):
        M[i][j] += s * M[l][j]
        j += 1


def echange_ligne(M, i, j):

    tmp = M[i]
    M[i] = M[j]
    M[j] = tmp

    return M

# def GaussJordanQ(M):
#     n = len(M)
#     m = len(M[0])

#     p = 0 # Indicce de ligne du pivot
#     j = 0 # Indice decrivant les colonnes

#     while j < m and p < n:

#     return

M = [[1, 2, 3], [4, 5, 6]]

# print(LineIndexMax(M, 0, 1, 2))

# print(LineAddMultScal(M, 1, 0, 2))

print(echange_ligne(M, 0, 1))