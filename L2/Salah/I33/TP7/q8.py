def multbyalpha(b, f):
    y = b << 1
    degree = len(bin(f)) - 3
    if (y >> degree) & 1:
        y = y ^ f
    return y


def multiplie(b, c, f):
    s = 0
    aux = c
    while b != 0:
        if (b & 1) != 0:
            s = s ^ aux
        aux = multbyalpha(aux, f)
        b = b >> 1
    return s


def matmat(A, B, P):
    p = len(A)
    k = len(B)
    n = len(B[0])

    result = []
    for i in range(p):
        result.append([])
        for j in range(n):
            val = 0

            for u in range(k):
                val = val ^ multiplie(A[i][u], B[u][j], P)

            result[i].append(val)

    return result


def test_matmat():
    assert matmat(
        [[14, 8, 9], [0, 4, 12], [12, 10, 12]],
        [[11, 12, 8], [7, 8, 15], [4, 9, 5]],
        19) == [[7, 5, 3], [10, 0, 0], [11, 6, 15]]
