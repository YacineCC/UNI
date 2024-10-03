def eval_poly(P,b,p):
    
    pol = P[-1]

    i = 2

    while i <= len(P):
        pol %= p
        pol *= b
        pol %= p
        pol += P[-i]
        pol %= p
        i += 1
    return pol

print(eval_poly([4, 3, 0, 1, 2, 0, 1, 4, 1],2,41))

