def partition(L):
	
	d1 = 0
	d2 = len(L) - 1
	i = 0
	
	
	while i < d2:
		
		if L[i] < 3:
			
			L[i], L[d1] = L[d1], L[i]	
			d1 += 1
			i += 1
		
		elif L[i] > 6:
			
			L[i], L[d2] = L[d2], L[i]
			d2 -= 1
		
		else:
			
			i += 1
	
	return L
