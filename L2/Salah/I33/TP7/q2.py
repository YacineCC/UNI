from random import randrange


def gentrianginf(n, t):
    m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i >= j:
                m[i][j] = randrange(0, t)
    return m


def gensym(n, t):
    m = gentrianginf(n, t)
    for i in range(n):
        for j in range(i+1, n):
            m[i][j] = m[j][i]
    return m


print(str(gensym(4, 10)).replace("],", "]\n"))
