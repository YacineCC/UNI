# Q11

def tri_bulle(L):
    d = len(L)
    while d > 0:
        for i in range(d - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
        d -= 1
    return L

# Q12

def tri(L):
    for i in range(len(L) - 1):
        imin = i
        for j in range(i + 1, len(L)):
            if L[j] < L[imin]:
                imin = j
        L[i], L[imin] = L[imin], L[i]
    return L

# Q13

def partition(L):
    L = L.copy()
    d1, d2, d3 = 0, 0, len(L) - 1
    while d2 <= d3:
        if 3 <= L[d2] <= 6:
            d2 += 1
        elif L[d2] > 6:
            L[d2], L[d3] = L[d3], L[d2]
            d3 -= 1
        else:
            L[d1], L[d2] = L[d2], L[d1]
            d1 += 1
            d2 += 1
    return L

# Q14

def puissance(x, y, n):
    result = 1
    while y > 0:
        if y & 1:
            result = result*x % n
        x = x*x % n
        y = y // 2
    return result % n