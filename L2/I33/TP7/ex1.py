def transpose(M):
	res = []
	i = 0
	while i < len(M[0]):	
		tmp = []
		for l in M:	
			tmp += [l[i]]
		res += [tmp]
		i += 1
	return res

M = [[7, 1, 8, 0], [4, 7, 4, 8], [7, 1, 2, 3], [0, 5, 7, 7], [3, 0, 4, 1], [0, 7, 7, 8]]
print(transpose(M))
