def puissance(x,y,n):
    """ binaire = []
    a = y
    while a > 0:
        r = a % 2
        binaire += [r] 
        a = a // 2
    """
    i = 0
    z = 1
    b = x
    binaire = bin(y)[2::]
    while i < len(binaire):

        if binaire[i] == 1:
            
            z = ((z%n) * (x%n))%n

        z = ((z%n) * (x%n) * (x%n)) % n
        i += 1
    return z


print(puissance(3,10,6))
