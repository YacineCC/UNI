def eval_poly_F2(P,b):

    pol = P[-1]

    i = len(P)-2

    while i >= 0:
        pol = pol & b
        pol = pol ^ P[i]
        i -= 1
    return pol
print(eval_poly_F2([1, 0, 1, 1, 0, 1],0))
