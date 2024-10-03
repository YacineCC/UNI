def multbyalpha(b,f):
    deg = len(bin(f)[2:])-1
    y = b<<1
    if (y&(1<<deg))!=0:
        y = y ^ f

    return y

print(multbyalpha(4,13))
