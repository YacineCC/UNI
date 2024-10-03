def is_irreductible(P,p):
	i = 0
	
	s = P[-1]
	while (s != 0) and (i < p):
		
		s = P[-1]
		j = 2
		
		while (j <= len(P)):
			
			s = (s * i) % p
			s = (s + P[-j]) % p
			j += 1
		
		i += 1
			
			
		
	
	return s != 0
	

print(is_irreductible([0, 21, 1],23))
print(is_irreductible([2, 7, 1],11))
print(is_irreductible([3, 16, 1],17))
