def ens_to_int(A):
	
	t = 0
	
	for k in A:
		t = t | 1 << k
		
	
	return t
	
A = [2,5,8,9]

print(ens_to_int(A))
