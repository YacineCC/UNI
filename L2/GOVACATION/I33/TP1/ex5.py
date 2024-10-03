def recherche(L,S,p):
	T = []	
	i = 0
	while i < len(L) and p+i < len(L):
		
		k = i
		som = 0
		while k <= (p+i):
			som += L[k]
			k += 1
		
		if som >= S:
			T += [i]
		
		i += 1
	
	
	return T
			 
