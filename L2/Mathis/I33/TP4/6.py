def is_primitif(P):
    # En python dans F2^m, alpha est représenté par 2
    alpha = 2
    div = decompose((1 << len(P)) - 1)

    # Pour chaque diviseur premier d on teste alpha ^ (2^m - 1) / d
    i = 0
    tmp = alpha
    while i < len(div) and tmp != 1:
        j = 0
        while j < ((1 << len(P)) - 1) / div[i]:
            tmp = multiplie(tmp, alpha, P)
            j += 1
        i += 1

    return tmp != 1


print(is_primitif([1, 1, 1]))
