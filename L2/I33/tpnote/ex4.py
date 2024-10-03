def decompose(n):
    i = 2
    tab = []
    k = 0
    while n > 1:

        if n % i == 0:
            exp = 0
            while n % i == 0:

                n =  n / i
                exp += 1
            tab += [[i,exp]]
        i += 1
    return tab

print(decompose(99999876400))




