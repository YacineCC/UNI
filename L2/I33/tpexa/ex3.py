def echelon(A,p):
	

   	
	i = 0
	
	while i < len(A)-1:
		k = i
		
		
		while k < len(A[0]) and A[k][i] == 0:
			
			k += 1
		
		if k > i:
			tmp = A[k]
			A[k] = A[i]
			A[i] = tmp
			
		z = i + 1
		while z < len(A[0]):
			q = 0
			tmp = A[k][i]
			while(q < len(A)):
				A[k][q] = (A[i][i] * A[k][q] - tmp * A[i][q])%p
				q += 1
			z += 1
		i += 1

		
	return A

print(echelon([[7, 4, 8, 6, 6, 7, 3, 2], [1, 8, 3, 12, 12, 1, 6, 4], [10, 0, 6, 10, 0, 1, 9, 7], [3, 9, 7, 6, 11, 2, 2, 10], [4, 8, 4, 10, 5, 2, 8, 10]],13))

print(echelon([[0], [12], [21], [18], [4]],23))
