def inverse(a,p):
	y = p
	u = 1
	v = 0
	
	u1 = 0
	v1 = 1
	
	while p > 0:
		
		q = a // p
		a,p = p,a % p
		
		u,u1 = u1, u - (q*u1)
		v,v1 = v1, v - (q*v1)
		

	return u % y

print(inverse(1128,1619))
		
