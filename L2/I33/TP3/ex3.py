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

print(decompose(99999876400))

