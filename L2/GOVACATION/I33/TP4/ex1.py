def eval_poly(P,b):
	i = 2
	s = P[-1]
	while i <= len(P):
		
		s = s * b
		s += P[-i]
		
		
		
		
		i += 1
	
	return s

print(eval_poly([3, 2, 5, 0, 3, 3, 3, 1],2))
