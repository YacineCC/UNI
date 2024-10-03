def tri(L):
	i = 0
	
	while i < len(L):
		
		mini = i
		
		k = i
		
		while k < len(L):
			
			if L[k] < L[mini]:
				
				mini = k
			k += 1
		
		L[mini], L[i] = L[i], L[mini]
		i += 1
	
	return L
