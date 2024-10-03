def pgcd(a,b):

    while b != 0:

        a,b = b,a%b

    return a


def generateurs(n):
    tab = []
    i = 1
    while i < n:

        if pgcd(i,n) == 1:

            tab += [i]
        i += 1
    return tab


print(generateurs(6))
