def hammingweight(n):
	poids = 0
	
	while n > 0:
		
		if n&1:
			poids += 1
		
		n = n >> 1
	
	return poids


print(hammingweight(25))
print(hammingweight(24))
n = 25 & 24
print(hammingweight(24))
