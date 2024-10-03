def decompose(n):
	decomp = []
	i = 2
	while i <= n:
		
		if n % i == 0:
			decomp += [i]
			while n % i == 0:
				n = n // i
		
		i += 1
	return decomp
	
def generateurs(p):
	divs = decompose(p-1)
	gens = []
	for i in range(2,p):
		gen = True
		
		for k in divs:
			if pow(i,((p-1)//k),p) == 1:
				gen = False
		if gen:
		
			gens += [i]
	
	return gens

print(generateurs(11071))
