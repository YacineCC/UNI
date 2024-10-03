def euler_phi(n):
	if n == 0 or n == 1:
		return 1
	phi = 2
	
	i = 2
	
	while i < n - 1:
		
		a = i
		b = n
		while b != 0:
			
			a,b = b, a % b
		
		if a == 1:
			phi += 1
		
		i += 1
	
	return phi

print(euler_phi(89))
		
		
		
		
