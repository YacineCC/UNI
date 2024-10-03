def sous_groupe_gen_mult(a,n):

    x = a
    tab = [a]
    while x != 1:

        x *= a
        x = x % n

        tab += [x]

    return tab
print(sous_groupe_gen_mult(3,17))
