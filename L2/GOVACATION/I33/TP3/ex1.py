def pgcd(a,b):
	
	while b != 0:
		a,b = b, a%b
	
	return a


def generateurs(n):
	gen = [1]
	i = 2
	while i < n-1:
		if pgcd(i,n) == 1:
			gen += [i]
		i += 1
	
	gen += [n-1]
	
	return gen

print(generateurs(6))
