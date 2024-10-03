
def egcd(a,n):
    
    
    
    u,v1 = 1,1
    u1,v = 0,0

    while(n>0):
        q = a//n

        u,v,u1,v1 = u1,v1,u-(q*u1),v-(q*v1)

        a,n = n, a%n

    return [a,u,v]

def enumere_keys(n):
    res = []
    i = 2
    while(i < n):
        
        test = egcd(i,n)
        # On regarde si i et n sont premiers entre eux pour tous les i
        if(test[0] == 1):
            #creation de toutes les clefs possibles
            for j in range(n):
                res += [[i,j,n]]

        i += 1
    return res

print(enumere_keys(26))
print(len(enumere_keys(26)))
