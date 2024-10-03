def somme(L,M):
    
    x = L[0] * M[1] + M[0] * L[1]
    y = L[1] * M[1]
    if x % y == 0:
        return x / y
    else:
    	
    	a = x
    	b = y
    	
    	while b != 0:
    		a,b = b, a % b
    	x = x / a
    	y = y / a
    	return [x,y]
