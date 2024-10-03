def recherche(L,S,p):
	T = []
	i = 0
	som = 0
	while i <= p:
		som += L[i]
		i += 1
	
	if som >= S:
		T += [0]
	
	k = 1
	
	while (k+p) < len(L):
		
		som = som - L[k-1] + L[k+p]
		if som >= S:
			
			T += [k]
		k += 1
	
	
	return T
		
	
	
