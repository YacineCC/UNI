def euclide_e(a,n):
    
    u = 1
    v = 0
    u1 = 0
    v1 = 1

    while n != 0:

        q = a // n
        r = a % n
        tmpu = u
        tmpv = v

        u = u1
        v = v1
        u1 = tmpu - q*u1
        v1 = tmpv - q*v1
        
        a = n
        n = r

    return [u,v,a]

print(euclide_e(54,39))


