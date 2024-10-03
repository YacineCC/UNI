def poids(n):
	i = 0
	while n > 0:
		
		if n&1:
			i += 1
		
		n >>= 1
	return i

		



def prod_mat_vec_F2(M,V):
	s = 0
	for i in M:
		print(s)
		s = s ^ (i ^ V)
	
	return s
print(prod_mat_vec_F2([9,15,5],7))
		

