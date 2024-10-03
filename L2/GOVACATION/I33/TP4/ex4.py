def eval_poly_F2(P,b):
    pol = P & 1
    P >>= 1
    while P > 0:

        while P & 1:
            pol = pol ^ b
            P >>= 1
        P >>= 1

    return pol
