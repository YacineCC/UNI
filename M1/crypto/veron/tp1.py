from random import *

def pgcd(a, b):

    while b != 0:
        tmp = a
        a = b
        b = tmp % b

    return a


def euclide_e(a, n):

    u1 = 1
    v1 = 0

    u2 = 0
    v2 = 1

    while(n != 0):
        print(n)
        r = a % n
        q = a // n

        tmp_u2 = u2
        tmp_v2 = v2

        u2 = u1 - q * u2
        v2 = v1 - q * v2 

        u1 = tmp_u2
        v1 = tmp_v2

        a = n
        n = r


    return (u1, v1, a)

def inverse(a,p):
    u1 = 1
    v1 = 0

    u2 = 0
    v2 = 1
    n = p
    while(p != 0):

        r = a % p
        q = a // p

        tmp_u2 = u2
        tmp_v2 = v2

        u2 = u1 - q * u2
        v2 = v1 - q * v2

        u1 = tmp_u2
        v1 = tmp_v2

        a = p
        p = r


    return u1 % n

def euler_phi(n):

    phi = 0
    i = 1
    while i <= n:
        b = n
        a = i
        while b != 0:
            tmp = a 
            a = b 
            b = tmp % b 
        if a == 1:
            phi += 1

        i += 1
    return phi

def ord(a,n):
    
    b = n
    x = a 
    while b != 0:
        tmp = a 
        a = b 
        b = tmp % b
        
    return n// a
   

def generateurs(n):

    gens = []

    i = 1
    while i <= n:
        if pgcd(i, n) == 1:
            gens.append(i)
        i +=1
    return gens

def sous_groupe_gen_add(a, n):
    s_groupe = []
    x = a
    while x != 0:
        s_groupe.append(x)
        x = (x + a) % n
    s_groupe.append(0)
    return s_groupe

def sous_groupe_gen_mult(a, n):
    s_groupe = []
    x = a
    while x != 1:
        s_groupe.append(x)
        x = (x * a) % n
    s_groupe.append(1)
    return s_groupe


def ord(a, p):

    i = 1
    mini = p-1 
    while i < p**0.5:
        if (p-1) % i == 0:
            if pow(a, i, p) == 1:
                return i
            
            elif pow(a, (p-1) // i, p) == 1 and ((p-1) // i) < mini: 
                mini = (p-1) // i
        i += 1

    return mini


def GSG(p):

    test = randrange(2, p-2)

    while pow(test, (p-1) // 2, p) == 1 or  pow(test, (p-1) // (p-1), p) == 1:
        test = randrange(2, p-2)
    return test

def decompose(n):
    x = n
    decomp = []
    puissance = 0
        
    while x % 2 == 0:
        x = x // 2
        puissance += 1
    if puissance > 0:
        decomp.append([2, puissance])
    i = 3
    while x > 1:
        puissance = 0
        while x % i == 0:
            x = x // i
            puissance += 1
        if puissance > 0:
            decomp.append([i, puissance])
        i += 2
    return decomp
print(decompose(59242))


def generateurs_mult(p):
    
    dec = decompose(p-1)
    
    gens = []
    for i in range(1, p):
        flag = True
        for facteurs in dec:
            if pow(i, (p-1) // facteurs, p) == 1:
                flag = False
        if flag:
            gens.append(i)

    return gens


