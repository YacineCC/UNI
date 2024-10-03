def hammingweight2(n):
	i = 0
	
	while n > 0:
		
		n = n & (n-1)
		print(n)
		
		i += 1
	
	return i


print(hammingweight2(25))
