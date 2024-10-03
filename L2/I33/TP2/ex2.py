def int_to_ens(t):
    k = 0
    tab = []
    while t > 0:
        if t & 1 == 1:
            tab += [k]
        t >>= 1
        k += 1
    return tab

print(int_to_ens(804))

