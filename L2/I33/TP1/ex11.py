def tri_bulle(L):
    n = len(L)
    permute = True

    while permute == True:
        permute = False
        j = n - 1
        k = 1
        while j >= k:
            if L[j] < L[j-1]:
                tmp = L[j]
                L[j] = L[j-1]
                L[j-1] = tmp
                permute = True
            j -= 1
        k += 1
    return L



print(tri_bulle([4,2,93,12,13,1,2,3]))



