# Q1
def somme_pair(L):
    return sum(x for x in L if x % 2 == 0)


def test_somme_pair():
    L = [3, 2, 5, 7, 4, 1]
    assert somme_pair(L) == 6

# Q2


def somme_ind_pair(L):
    somme = 0
    i = 0
    while i < len(L):
        somme += L[i]
        i += 2
    return somme


def test_somme_ind_pair():
    L = [3, 2, 5, 7, 4, 1]
    assert somme_ind_pair(L) == 12

# Q3


def somme(L, M):
    l, m = L.copy(), M.copy()
    denominateur = ppcm(l[1], m[1])

    l[0] = l[0] * int(denominateur/l[1])
    l[1] = denominateur

    m[0] = m[0] * int(denominateur/m[1])
    m[1] = denominateur

    l[0] += m[0]

    p = pgcd(l[0], l[1])
    l[0] = l[0] // p
    l[1] = l[1] // p

    result = l[0]/l[1]
    if result.is_integer():
        return int(result)
    else:
        return l


def pgcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def ppcm(x, y):
    return int(x*y/pgcd(x, y))


def test_somme():
    assert somme([1, 2], [1, 2]) == 1
    assert somme([1, 2], [1, 4]) == [3, 4]
    assert somme([14, 11], [14, 22]) == [21, 11]

# Q4


def sommefibo(j):
    l_fibo = [0, 1, 1]
    s = 0
    i = 0
    while i < j:
        s += l_fibo[0]

        l_fibo[0] = l_fibo[1]
        l_fibo[1] = l_fibo[2]
        l_fibo[2] = l_fibo[0] + l_fibo[1]

        i += 1
    return s


def test_sommefibo():
    assert sommefibo(5) == 7
    assert sommefibo(6) == 12

# Q5


def recherche(L, S, p):
    result = []
    k = 0
    while p + k < len(L):
        i = k
        somme = 0
        while i <= p + k:
            somme += L[i]
            i += 1
        if somme >= S:
            result.append(k)
        k += 1
    return result


def test_recherche():
    data = (
        ([38, 52, 79, 91, 73, 60, 85, 27, 73, 48, 71, 43, 24, 64, 41, 47, 1, 90, 24,
         18, 29, 97, 30, 30, 51, 72, 78, 69, 0, 9, 31, 5, 76, 84, 64, 1, 17], 515, 7),
        ([33, 16, 18, 36, 41, 96, 62, 31, 3, 59, 69, 91,
         75, 51, 67, 99, 21, 80, 67, 30, 78], 355, 5),
        ([18, 24, 42, 41, 65, 21, 54, 40, 91, 42, 46, 43, 59, 58, 58, 52, 4, 80, 16, 30, 14,
         41, 79, 23, 77, 29, 56, 52, 49, 84, 81, 34, 18, 33, 98, 99, 70, 93, 18], 417, 7),
        ([91, 88, 10, 75, 18, 75, 90, 29, 49, 38, 74, 73, 40, 70, 33,
         9, 9, 54, 66, 34, 35, 13, 63, 64, 11, 0, 21, 1, 19], 593, 5),
        ([10, 62, 87, 78, 34, 48, 34, 19, 56, 50, 16, 21,
         17, 26, 47, 61, 54, 13, 69, 36, 41], 409, 8),
        ([2, 40, 2, 35, 22, 92, 43, 80, 5, 56, 33, 61, 44, 88, 24, 14, 90, 21,
         66, 88, 50, 12, 49, 18, 48, 40, 19, 40, 47, 88, 25, 48, 9, 85], 484, 15),
        ([45, 50, 78, 8, 43, 78, 22, 96, 31, 14, 72, 1,
         99, 62, 82, 68, 87, 72, 82, 37, 21, 35], 342, 5),
        ([95, 37, 18, 22, 29, 41, 83, 55, 48, 96, 87, 89, 35, 11, 97, 58,
         71, 44, 84, 94, 87, 86, 79, 64, 81, 96, 48, 81, 94], 559, 9),
        ([41, 46, 64, 24, 86, 23, 54, 68, 42, 65, 66, 77,
         35, 44, 24, 74, 26, 62, 6, 35, 14, 21], 598, 9),
        ([97, 98, 1, 40, 70, 35, 2, 26, 53, 52, 37, 76, 32, 88, 39, 24, 4, 89, 19, 84,
         72, 83, 85, 38, 39, 44, 52, 41, 57, 64, 32, 10, 65, 16, 64, 98, 91, 93], 539, 8),
    )

    result = (
        [1, 2, 3],
        [9, 10, 11, 12, 13, 14, 15],
        [6, 7, 8, 22, 23, 24, 27, 28, 29, 30, 31],
        [],
        [0, 1, 2],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        [10, 11, 12, 13, 14, 15],
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        [],
        [17],
    )

    for d, r in zip(data, result):
        assert recherche(*d) == r
