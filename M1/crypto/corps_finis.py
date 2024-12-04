def multbyalpha(b, f):
    z = b << 1
    if( z & (1<<(len(bin(f)) - 3))) != 0:
        z = z ^ f

    return z

#print(multbyalpha(10, 11))


def multiplication(b, c, f):
    s = 0
    aux = c
    while b !=0 :
        if (b & 1) != 0: s = s ^ aux
        aux = multbyalpha(aux)
        b = b >> 1
    return s

def table_log(P):
    L = [0] * (1<<(len(bin(P)) - 3))
    L[0] = -1

    i = 0
    alpha = 1

    while i < len(L)-1:
        
        L[alpha] = i
        alpha = multbyalpha(alpha, P)

        i += 1
    return L

def table_alpha(P):
    L = [0] *( (1<<(len(bin(P)) - 3)) - 1)
    L[0] = 1

    i = 0
    alpha = 1

    while i < len(L):
        
        L[i] = alpha
        alpha = multbyalpha(alpha, P)

        i += 1
    return L


def multiplie(x,y,P):
    if x == 0 or y == 0:
        return 0

    else:
        t_a = table_alpha(P)
        t_l = table_log(P)

        i = t_l[x]
        j = t_l[y]

        deg = len(bin(P)) - 3
        exposant =  (i + j) % ((1 << deg)-1)

        return t_a[exposant]

def symetrique_mul(x, P):
    t_a = table_alpha(P)
    t_l = table_log(P)

    
    i = t_l[x]
    return t_a[-i]


def evalue(Q, y, P):
    ev = 0
    i = len(Q) - 1
    alpha_i = 1
    while i >= 0:
        ev = ev ^ (multiplie(multiplie(Q[i],y , P), alpha_i,P))
        
        i -= 1
        alpha_i = multiplie(alpha_i, alpha_i, P)
    return ev


print(evalue([4, 3, 6], 2, 13))
