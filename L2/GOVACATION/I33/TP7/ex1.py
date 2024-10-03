def transpose(M):
	
	tab = []
	
	i = 0
	
	while i < len(M[0]):
		
		j = 0
		tmp = []
		while j < len(M):
			tmp += [M[j][i]]
			
			
			j += 1
		tab += [tmp] 
		i += 1
	return tab
		



print(transpose([[1,2,3],[4,5,6]]))
