def matmat(A,B):
    
    res = [[0]*(len(B)-1)] * len(A)
    
    for i in range(len(A)):
        for j in range(len(B)):
            som = 0
            for k in range(len(B)):
                som += A[i][k]*B[k][j]
            res[i][j] = som
    return res
