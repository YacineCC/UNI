def inverse(a,p):
    x = p
    u,v,u1,v1 = 1,0,0,1

    while p != 0:
        q = a//p

        a,u,v,p,u1,v1 = p,u1,v1,a-q*p,u-q*u1,v-q*v1

    if u < 0:
        return x+u
    return u

print(inverse(221,783))
 
