def multbyalpha(b,f):
    deg = len(bin(f)[2:])-1
    y = b<<1
    if (y&(1<<deg))!=0:
        y = y ^ f

    return y


def table_log(P):
    deg = len(bin(P)[2:])-1
    i = 0
    ok = 1 << deg
    L = [0] * ok
    L[0] = -1
    alpha = 1
    while i < ok-1:
        L[alpha] = i
        alpha = multbyalpha(alpha,P)
        i += 1

    return L

def table_alpha(P):
    deg = len(bin(P)[2:])-1
    ok = 1 << deg
    i = 0
    L = [0] * (ok-1)
    alpha = 1
    while i < ok-1:
        L[i] = alpha
        alpha = multbyalpha(alpha,P)
        i+= 1
    return L

"""
def multiplie(x,y,P):
    if x == 0 or y == 0:
        return 0
    c = (log_table[x] + log_table[y]) % (len(log_table)-1)
    
    return alpha_table[c]
"""

def eval_poly(P,b):
    i = len(P) - 1
    z = P[i]
    while i > 0:
        z *=  b
        z += P[i-1]

        i -= 1
    return z


def evalue(Q,y,P):
    i = len(Q)-1
    z = Q[i]

    while i > 0:

        z = multiplie(z,y,P)
        z = z ^ Q[i-1]

        i -= 1
    return z

print(evalue([4,3,6],2,13))

