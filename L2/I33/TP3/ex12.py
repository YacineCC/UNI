def is_sym_mult(x,y):

    T = [0,0]

    T[0] = x[0] * y[0]
    T[1] = x[1] * y[1]

    return T[0] == T[1]
