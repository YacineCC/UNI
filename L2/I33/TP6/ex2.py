def combinaison_lineaire(c,V):
    combi = 0
    for el in V:
        ele = el
           
    while c > 1:
        x = c
        cpt = 0

        while x > 1:
            x >>= 1
            cpt += 1
    
    
        while ele > 0:
            combi ^= (c >> cpt & (ele & 1))
            ele >>= 1

        combi <<= 1
        c >>= 1
    return combi - 1
print(combinaison_lineaire(12,[1,5,3,2]))


            

