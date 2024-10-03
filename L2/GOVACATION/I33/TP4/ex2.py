def eval_poly(P,b,p):
	i = 2
	s = P[-1]
	while i <= len(P):
		
		s = (s * b)%p
		s += P[-i] %p
		
		
		
		
		i += 1
	
	return s
