def som_div_propres(n):
	if n == 1:
	    return 0
	i = 2
	som = 1
	while i < (n**0.5) + 1:
		
		if n % i == 0:
			som += i
			if i != n/i:
			    som += n/i
		
		i += 1
	
	return som
