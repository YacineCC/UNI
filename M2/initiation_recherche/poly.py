from sage.all import *
from random import randrange

import numpy as np

def gen_poly_random(n, rho):
	rho = int(rho)
	return [randrange(-rho + 1, rho) for coef in range(n)]

def SQandMult(a, b, p):
     c = 1
     while b:
         if b & 1:
             c = (c * a) % p
         a = (a * a) % p
         b = b >> 1
     return c

def generate_matrix(p, gamma, n):
    B = matrix(ZZ, n)
    B[0, 0] = p
    for i in range(1, n):
        B[i, i] = 1                          
        B[i, 0] = -(gamma ** i)
           
    return B

def find_M(B):
	tmp = np.array(B)
	tmp = tmp[:,0]
	for i,x in enumerate(tmp):
		if x & 1 == 1:
			return ZZ["X"](list(B[i]))

def pmns(p, n):
	#psize = True
	#p = random_prime(psize)
	phi = 1 << 64
	#n = floor(log(p, 2) / 64) + 1
	K = GF(p)
	pol = PolynomialRing(K, "X")
	X = pol("X")
	E = ZZ["X"](f"X^{n} - 2") # X**n-2 # lambda = 2
	XP = SQandMult(X, p, E)
	d, v, u = xgcd((XP - X) % E, E)
	gamma = -d[0]
	B = generate_matrix(p, gamma, n)
	B = B.LLL()
	lambda_ = 2
	if (2 * n * abs(lamdba_) * B.norm(1)) < phi:
		rho = B.norm(1) - 1
	
	M = find_M(B) # Pas besoin du M_inv
	E = ZZ["X"](E)
	new_d, new_u, new_v = xgcd(M, E)
	new_d = int(new_d)
	new_d_inv = pow(new_d, -1, phi)
	M_inv = new_d_inv * new_u % phi

	
	return M, M_inv, rho, phi, E, gamma, "M * M^-1 := ", (M_inv * M % E) % phi 

def mult_mongt(p, n):
	res_pmns = pmns(p, n)
	M = res_pmns[0]
	M_inv = res_pmns[1]
	rho = res_pmns[2]
	phi = res_pmns[3]
	E = res_pmns[4]
	gamma = res_pmns[5]
	print("gamma ", int(gamma))
	gamma = int(gamma)

	A = gen_poly_random(n, rho)
	B = gen_poly_random(n, rho)
	A = ZZ["X"](A)
	B = ZZ["X"](B)

	M = ZZ["X"](M)
	M_inv = ZZ["X"](M_inv)
	E = ZZ["X"](E)
	C = (A * B) % E
	Q = (C * M_inv % E) % phi
	C = ZZ["X"](C)
	Q = ZZ["X"](Q)
	C_prime = (C - (Q * M % E)) / phi
	C_prime = ZZ["X"](C_prime)
	print("C_prime :", C_prime)

	return C_prime(gamma) % p == (A(gamma) * B(gamma) * pow(phi, -1, p)) % p

p = (1 << 255) - 19
n = 5
# 

#print(pmns(p, n))

print(mult_mongt(p, n))