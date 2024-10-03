def decompose(n):
    i = 2
    tab = []
    while n != 1:
        if n % i == 0:
            while n % i == 0:

                n = n // i
            tab += [i]

        i += 1

    return tab

def inversibles(n):
    tab = []
    i = 1
    while i < n:
        x = n
        j = i
        while x != 0:

            j,x = x,j % x
        if j == 1:
            tab += [i]
        i += 1
    return tab

def generateurs(p):
    diviseurs = decompose(p-1)
    res = []
    for i in range(1,p):
        test = True
        for k in diviseurs:
            if pow(i,(p-1)//k,p) == 1:
                test = False
        if test:
            res += [i]



    return res

print(generateurs(10007))
