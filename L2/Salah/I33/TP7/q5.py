def matvec(M, V):
    p = len(M)
    n = len(V)

    result = []

    for i in range(p):
        val = 0
        for j in range(n):
            val += V[j]*M[i][j]
        result.append(val)
    return result

def test_matvec():
    assert matvec([[2, 1, 2], [2, 1, 2], [2, 1, 0]],[1,0,2]) == [6, 6, 2]
