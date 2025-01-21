import random

def rabin_miller(n, t):

    aux = n - 1
    s = 0

    while aux & 1:
        aux = aux >> 1
        s += 1

    
    a = random.randint(2, n-1)

    for k in range(t):
        a_pow_t = pow(a, aux, n)

        flag = True
        for i in range(1, s):
            if pow(a, 1<<i * aux, n) == n-1:
                flag = False
        
        if a_pow_t != 1 and a_pow_t != n-1 and flag:
            return 0 # n est composé

    return 1 # n est probablement premier avec une probabilité de faux positif bornée par 1/4^t