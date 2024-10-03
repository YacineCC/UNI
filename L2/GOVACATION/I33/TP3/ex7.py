def ord(a,n):
	
	x = a
	y = n
	
	while y != 0:
		x,y = y, x % y
	
	return n/x

print(ord(5,10))
