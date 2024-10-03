def det(A):

    d = 1
    s = 1
    p = 1
    j = 0
    
    n = len(A)
    
    while(j < (n-1)):
        i = j
        
        while((i < n) and A[i][j] == 0):
            i += 1
        if(i >= n):
        	return 0
            
        if(i > j):
        	tmp = A[i]
        	A[i] = A[j]
        	A[j] = tmp
        	s = -s
        d = d * A[j][j]
            
        i = j + 1    
        while i < n:
        	k = 0
        	tmp = A[i][j]
        	while(k < n):
        		A[i][k] = A[j][j] * A[i][k] - tmp * A[j][k]
        		k += 1
        	p = p * A[j][j]
        	i += 1
        j += 1
    d = (d * A[n-1][n-1] * s) / p
    return d

