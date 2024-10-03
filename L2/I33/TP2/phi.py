def euler_phi(n):
    tab = []
    j = 1
    while j < n:
        test = n
        i = j
        while test != 0:
            i,test = test,i % test

        if i == 1:
            tab += [j]

        j += 1
    return tab

print(euler_phi(26))
