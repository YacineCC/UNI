def SQandMontg(a, b, p, phi):
     c = phi % p
     aphi = (a * phi) % p
     while b:
         if b & 1:
             c = montg(c, aphi, p, phi)
         aphi = montg(aphi, aphi, p, phi)
         b = b >> 1
     return montg(c, 1, p, phi)

def SQandMult(a, b, p):
     c = 1
     while b:
         if b & 1:
             c = (c * a) % p
         a = (a * a) % p
         b = b >> 1
     return c


def montg(a, b, p, phi):
         c = a * b
         q = (c * pow(p, -1, phi)) % phi
         c_prime = (c - q * p) // phi
         if c_prime < 0:
             c_prime = c_prime + p
         return c_prime

