def sommefibo(j):
	if (j == 0) or (j == 1):
		return 0
	F0 = 0
	F1 = 1
	som = 1
	i = 2
	while i < j:
		
		F2 = F0 + F1
		F0 = F1
		F1 = F2
		som += F2
		i += 1
	
	return som
