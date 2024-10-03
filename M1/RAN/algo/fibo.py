steps = 0
def fibo_rec(n):
    global steps
    steps += 1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibo_rec(n-2) + fibo_rec(n-1)



def mult_matrix(M1, M2):

    A = M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0]

    B = M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1]

    C = M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0]

    D = M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1]

    
    res = [[A,B], [C, D]]
    return res

def square_matrix(M):
    return mult_matrix(M, M)

identite = [[1,2],[3,4]]


test = [[1,2],[3,4]]




print(mult_matrix(identite, test))
