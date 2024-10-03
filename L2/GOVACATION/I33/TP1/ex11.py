def tri_bulle(L):
	n = len(L) - 1
	permute = True
	while permute:
	    permute = False
	    i = n
	    while 1 <= i:
	        if L[i-1] > L[i]:
	            L[i-1],L[i] = L[i], L[i-1]
	            permute = True
	        i -= 1
		
		
	return L
