def matmat(A,B):
    
    res = []
    for i in range(len(A)):
    	tmp = []
    	for j in range(len(B[0])):
    		som = 0
    		
    		for k in range(len(A[0])):
    			som += A[i][k]*B[k][j]
    		tmp += [som]
    	res += [tmp]
    return res
   

print(matmat([[1, 1, 2], [1, 0, 2]],[[1, 2, 0, 1], [1, 1, 1, 0], [0, 2, 2, 1]]))
