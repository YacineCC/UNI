def matmat(A, B):
    p = len(A)
    k = len(B)
    n = len(B[0])

    result = []
    for i in range(p):
        result.append([])
        for j in range(n):
            result[i].append(0)

            for u in range(k):
                result[i][j] += A[i][u]*B[u][j]
    return result


def test_matmat():
    assert matmat(
        [[1, 1, 2], [1, 0, 2]],
        [[1, 2, 0, 1], [1, 1, 1, 0], [0, 2, 2, 1]]
    ) == [[2, 7, 5, 3], [1, 6, 4, 3]]
