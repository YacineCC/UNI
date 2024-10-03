def puissance(x,y,n):
    z = 1
    while y > 0:

        if y & 1:

            z = ((z % n) * (x % n)) % n

        x = ((x% n) * (x % n)) % n

        y >>= 1
    return z

print(puissance(5,7,7))
