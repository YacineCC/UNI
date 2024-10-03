def is_symetrique(M):
    n = len(M)
    result = n == len(M[0])

    i = 0
    while result and i < n:
        j = 0
        while result and j < n:
            result = result and M[i][j] == M[j][i]
            j += 1
        i += 1

    return result

def test_is_symetrique():
    assert is_symetrique([[1,2,3],[2,4,6],[3,6,7]])
