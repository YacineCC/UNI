def multbyalpha(b,f):
    deg = len(bin(f)[2:])-1
    y = b<<1
    if (y&(1<<deg))!=0:
        y = y ^ f

    return y

def multiplication(b,c,f):
    S = 0
    aux = c
    while b!= 0:
        if(b&1)!=0:
                S = S ^ aux
            aux = multbyalpha(aux,f)
            a = a>>1
    return S
