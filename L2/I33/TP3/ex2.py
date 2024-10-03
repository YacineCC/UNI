def sous_groupe_gen_add(a,n):
    tab = [a]
    x = a
    while x  != 0:

        x = x + a
        x = x % n

        tab += [x]
    return tab

print(sous_groupe_gen_add(4,10))


