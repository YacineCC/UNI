def minimum(L):
	i = 1
	mini = L[0]
	while i < len(L):
		
		if L[i] < mini:
			mini = L[i]
		i += 1
	
	
	return mini 
		
		
