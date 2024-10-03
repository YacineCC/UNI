#Q1

def eval_poly(P,b):
	d = len(P)-1
	res = P[d]
	while d > 0:
		res *= b 
		res += P[d-1]
		d -= 1
	return res 
  

#Q2

def eval_poly(P,b,p):
	d = len(P)-1
	res = P[d]
	while d > 0:
		res *= b 
		res += P[d-1]
		d -= 1
	return res%p

#Q3
def eval_poly_F2(P,b):
	d = len(P)-1
	res = P[d]
	while d > 0:
		res *= b 
		res += P[d-1]
		d -= 1
	return res%2
	
#Q4

def eval_poly_F2(P,b):
    l = []
    while P > 0 :
        l +=[(P&1),]
        P = P >> 1
    res = l[0]
    i = 1
    while i < len(l) :
        res += l[i]*b
        i += 1
    return res % 2

#Q5

def is_irreducible(P,p):
    boool = True 
    for n in range(p*p*p) :
        boool = boool and (eval_poly(P,n,p) != 0)
    return boool
    
#Q6
def is_primitif(P):
    k = (1<<(len(P)-1))-1
    l = decompose(k)
    alpha = 2
    est_primitif = True
    i = 0
    while est_primitif and i < len(l) :
        g = alpha
        j = 1
        while j < k//l[i]  :
            g = multiplie(g,alpha,P)
            j += 1
        est_primitif = (g!=1)
        i += 1
    return est_primitif
    
#Q7

def hammingweight(n):
    cpt = 0
    while n != 0 :
        if n & 1 :
            cpt += 1
        n = n >> 1
    return cpt
    
#Q8

def hammingweight2(n):
    i=0
    while n != 0 :
        i += 1
        n = n&(n-1)
    return i
    

