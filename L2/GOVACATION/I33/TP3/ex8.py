def pgcd(a,b):
	while b != 0:
		a,b = b, a%b
	
	return a

def is_of_order(a,t,n):
	
	return n/pgcd(a,n) == t

print(is_of_order(5,3,10))
