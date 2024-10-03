def partition(L):
    d1 = 0
    i = 0
    n = len(L)
    d2 = n - 1
    while i < d2:
        if L[i] < 3:

            tmp = L[d1]
            L[d1] = L[i]
            L[i] = tmp
            d1 += 1
            i += 1

        elif L[i] > 6:

            tmp = L[d2]
            L[d2] = L[i]
            L[i] = tmp
            d2 -= 1
        else:
            i += 1
    return L

print(partition([3, 6, 6, 4, 6, 5, 5, 6, 3, 4, 5, 5, 5, 5, 5, 5, 5]))
print(partition([1, 1, 0, 4, 3, 4, 3, 5, 6, 7, 7, 8, 7, 7, 8, 8]))
