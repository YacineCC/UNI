def norme(M):
	maxi = 0
	i = 0
	while i < len(M[0]):
		som = 0
		j = 0
		while j < len(M):
			
			som += abs(M[j][i])
			j += 1
		
		if maxi < som:
			maxi = som
		i += 1
	return maxi
