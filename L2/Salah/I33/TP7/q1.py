def transpose(M):
    p = len(M)
    n = len(M[0])

    Mt = []
    for i in range(n):
        Mt.append([])
        for j in range(p):
            Mt[i].append(M[j][i])

    return Mt

def test_transpose():
    assert transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]
