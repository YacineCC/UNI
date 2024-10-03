from math import log,floor
def bit(n,i):
	return ((n>>(i))&1)
print(bit(4,2))

def set_bit(x,i,val):
	if val:
		return((x|(1<<i)))
		
	else:
		return((x&(~(1<<i))))
print(set_bit(19,0,0))

def pop_count(x):
	longueur = floor(log(x,2))+1
	compteur = 0
	for i in range(longueur):
		if ((x>>i)&1):
			compteur += 1
	return compteur
print(pop_count(19))

def expo_gd(x,k):
	L = []
	i = floor(log(k,2))
	r = 1
	while i >= 0:
		
		r = r*r
		L += [r]
		if bit(k,i):
			r = r*x
			L += [r]
		i = i - 1
	return L
print(expo_gd(3,5))

def expo_dg(x,k):
	r = 1 
	L = [1]
	p = x
	i = 0
	while i <= floor(log(k,2)) :
		if p not in L:
			L += [p]	
		if bit(k,i):
			
			r = r*p
			if r not in L:
				L += [r]
		p = p*p
		i += 1	
	return L 
print(expo_dg(2,13))

	
def fibo(n):
	F0 = 0
	F1 = 1
	for i in range(n):
		F2 = F0 + F1
		F0 = F1
		F1 = F2
	return F0
print(fibo(1))
	
"""def matmult(m1,m2):
	MF = []
	x = 0
	y = 0
	for i in m1[x]:
		for j in m2[y]:
			for s in 
			MF[x][y] = [i*j]
			y += 1"""
			 
		
def matmult(m1,m2):
	m = []
	
	for i in range(len(m1)):
		ligne = []
		for j in range(len(m2[0])):
			element = 0
			for k in range(len(m1[0])):
				element = element + m1[i][k] * m2[k][j]
			ligne.append(element)
		m.append(ligne)
	return m
M1 = [[1,2],[3,4]]
M2 = [[5,6],[7,8]]

print(matmult(M1,M2))
	
def matcarre(m):
	return matmult(m,m)
print(matcarre([[1,1]]))	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
