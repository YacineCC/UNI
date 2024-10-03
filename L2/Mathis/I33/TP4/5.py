def is_irreducible(P,p):
    result = True
    i = 0
    while i < p and result:
        result = bool(eval_poly(P, i, p))
        i += 1
    return result


def eval_poly(P, b, p):
    result = 0
    for i in range(-1, -len(P), -1):
        result += P[i]
        result *= b
    return (result + P[i - 1]) % p
