def tri(L):
    n = len(L)
    i = 0
    while i < n :
        mini = i
        j = i
        while j < n:
            if L[j] < L[mini]:
                mini = j
            j += 1
        tmp = L[i]
        L[i] = L[mini]
        L[mini] = tmp
        i += 1
    return L

print(tri([13,78,1,9,2,3,5,4]))
