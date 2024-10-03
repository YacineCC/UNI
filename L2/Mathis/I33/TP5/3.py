from fctions import multbyalpha


def table_log(P):
    lim = 1 << (len(bin(P)[2:]) - 1)
    result = [-1] * (lim)
    tmp = 1

    y = 0
    while y < lim - 1:
        result[tmp] = y
        tmp = multbyalpha(tmp, P)
        y += 1

    return result


print(table_log(13))
