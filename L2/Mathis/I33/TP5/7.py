from fctions import multiplication


def sous_groupe_gen(b,f):
    # on va calculer les puissances de b
    result = [b]
    cpy_b = b
    while b != 1:
        b = multiplication(b, cpy_b, f)
        result.append(b)

    return result

def ordre(b,f):
    return len(sous_groupe_gen(b,f))


print(sous_groupe_gen(2, 39))
print(ordre(2, 39))
