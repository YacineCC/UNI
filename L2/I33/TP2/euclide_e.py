def euclide_e(a,n):
    
    u,v,u1,v1 = 1,0,0,1

    while n != 0:
        q = a//n

        a,u,v,n,u1,v1 = n,u1,v1,a-q*n,u-q*u1,v-q*v1

    if a < 0:
        return [-a,-u,-v]
    return [a,u,v]
 
print(euclide_e(54,39))



