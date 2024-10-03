def print_mat(M):
    
    for i in M:
        print(i)


def mat_mult(A,B):
    C = []
    for i in range(len(A)):
    
        D = []
        for j in range(len(B[0])):
            som = 0
            
            for k in range(len(B)):
                som += A[i][k] * B[k][j]

            D += [som]
        C += [D]


    return C

#M = [[1,2,3],[4,5,6],[7,8,9]]
#print_mat(M)


A = [[1,2,3],[4,5,6]]
B = [[7,8],[9,-1],[-2,-3]]

print(mat_mult(A,B))
