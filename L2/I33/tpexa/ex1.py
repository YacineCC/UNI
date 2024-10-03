def multbyalpha(x):
	t = [(x[2]*3)%7,x[0],(x[2]+x[1])%7]
	
	return t
   
print(multbyalpha([1, 2, 3]))
