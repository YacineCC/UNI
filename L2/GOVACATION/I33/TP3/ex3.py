def decompose(n):
	decomp = []
	i = 2
	while i <= n:
		
		if n % i == 0:
			decomp += [i]
			while n % i == 0:
				n = n // i
		
		i += 1
	return decomp

print(decompose(99999876400))
			
