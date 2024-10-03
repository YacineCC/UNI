def eval_poly_F2(P,b):
	s = P[-1]
	i = len(P)-2
	while i >= 0:
		
		
		s = s & b
		s = s  ^ P[i]
		i -= 1
		
		
	
	return s
