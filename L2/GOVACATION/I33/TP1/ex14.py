def puissance(x,y,n):
	z =1
	x %= n
	while (y > 0):
	    if (y & 1 == 1):
	        z *= x
	        z %= n
	    x = (x * x) % n
	    y >>= 1
	 
	 
	return z
