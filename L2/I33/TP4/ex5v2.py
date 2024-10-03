def is_irreductible(P,p):

    pol = 0
    i = 1
    j = 0
    while i <= len(P) and (P[-i]*j)%p == 0 :

        j = 0
        while j < p :
        
            pol += (P[-i] * j) % p
            j += 1
        
        i += 1
        print(i)
    return i == len(P)+1 


print(is_irreductible([2, 18, 1],19))
