def euclide_e(a,n):
	u = 1
	v = 0
	
	u1 = 0
	v1 = 1
	
	while n > 0:
		
		q = a // n
		a,n = n,a % n
		
		u,u1 = u1, u - (q*u1)
		v,v1 = v1, v - (q*v1)
		
	
	return [u,v,a]

print(euclide_e(54,39))
		
		
