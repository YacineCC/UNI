def int_to_ens(t):
	A = []
	i = 0
	while t > 0:
		
		if t & 1:
			A += [i]
		t >>= 1
		i += 1
	return A

t = 804
print(int_to_ens(t))
		
		
