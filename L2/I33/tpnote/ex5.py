def symetrique(f):
    g = [0,0]
    g[0] = f[0]
    g[1] = f[1]


    a = (f[0] * g[0])
    b = f[0] * g[1] + f[1]

    T = [a,b]
    ad = b - f[1]
    ac = a

    x = -ad/ac - f[1]
    return[x,-b]

print(symetrique([5,8]))
