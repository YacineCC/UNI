def algoshawn(tab, k, e) :
    for i in range(0, len(tab)//k) :
        if tab[i*k] > e :
            for j in range (i*(k-1), i*k) :
                if tab[j] == e :
                    return j
            return -1
    return -1

print(algoshawn([1,2,3,4,5,6,7,8], 4, 4))



