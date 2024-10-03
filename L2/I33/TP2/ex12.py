def inverse(a,p):
    x = p
    u = 1
    v = 0
    u1 = 0
    v1 = 1

    while p != 0:

        q = a // p
        r = a % p
        tmpu = u
        tmpv = v

        u = u1
        v = v1
        u1 = tmpu - q*u1
        v1 = tmpv - q*v1

        a = p
        p = r

    return u % x

print(inverse(678,1423))
