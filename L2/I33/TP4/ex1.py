def eval_poly(P,b):

    i = 2
    pol = P[-1]

    while i <= len(P):

        pol *= b
        pol += P[-i]
        i += 1

    return pol

print(eval_poly([4,5,3],2))

