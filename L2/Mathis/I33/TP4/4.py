def eval_poly_F2(P, b):
    result = P & 1
    P = P >> 1

    # On travaille dans F2 donc les degrés n'ont aucune importance (sauf x^0)
    while P != 0:
        result = result ^ ((P & 1) & b)
        P = P >> 1
    return result

print(eval_poly_F2(5, 1))
print(eval_poly_F2(5, 0))
