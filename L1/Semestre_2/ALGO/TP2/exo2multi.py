def decomp(n):
	tab = []
	k = str(n)
	for i in k:
		tab += [int(i)]
	return tab
		



def tableau(T):
	i = 1
	tab = []
	while i <= len(T):
		tab += [T[-i]]
		i += 1
	return tab
n1 = int(input('n1 : '))
n2 = int(input('n2 : '))
nb1 =(tableau(decomp(n1)))
nb2 =(tableau(decomp(n2)))

def multiplication(n1,n2):
	n = len(n1)
	j = 0
	RES = [0]*2*len(n1)
	while j < n:
		i,r = 0,0
		while i < n:
			p = RES[i+j] + n1[j]*n2[i] +r
			RES[i+j] = p % 10
			r = p // 10
			i += 1
		RES[i+j] = r
		j += 1
	RES[i+j-1] = r
	
		
	return RES

