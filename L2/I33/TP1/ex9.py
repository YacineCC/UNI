def minimum_posi(L):
    mini = 0
    tab = []
    k = 0
    for i in L:

        if i < L[mini] :
            mini = k
            tab = [k]
        elif(i == L[mini]):
            tab += [k]
        
        k += 1
        
    return tab
print(minimum_posi([2,2,5,7,2]))
print(minimum_posi([3,2,5,7,2]))

