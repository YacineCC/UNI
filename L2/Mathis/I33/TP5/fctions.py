def multbyalpha(b,f):
    result = b << 1
    if len(bin(result)[2:]) >= len(bin(f)[2:]):
        result = result ^ f

    return result


def multiplie(b,c,f):
    s = 0
    aux = b
    while c != 0:
        if (c & 1) != 0:
            s = s ^ aux
        aux = multbyalpha(aux, f)
        c = c >> 1
    return s


def multiplication(b,c,f):
    s = 0
    aux = b
    while c != 0:
        if (c & 1) != 0:
            s = s ^ aux
        aux = multbyalpha(aux, f)
        c = c >> 1
    return s
