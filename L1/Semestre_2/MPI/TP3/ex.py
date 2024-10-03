import random as r
def factorielle(n):
	fact = 1
	for i in range(1,n+1):
		fact = fact * i
	return fact

def factorielleRec(n):
	if n == 0:
		return 1
	fact = n*factorielleRec(n-1)
	return fact


def binomialfake(n,p):
	if n < p:
		return("undef")
	else:
		return (factorielle(n)//(factorielle(n-p)*factorielle(p)))

def Triangle(n):
	tab = []
	for i in range(n + 1):
		tab += [(n + 1)*[0]]
	return tab
	
def TrianglePascalVierge(n):
	tab = Triangle(n)
	for i in range(len(tab)):
			j = 0
			while j <= i:
				tab[i][j] = 1
				j += 1 
	return tab
def JoliePascalprint(T):
	for i in T:
		for j in i:
		
			if j != 0:
				print(j,end=" ")
		print("\n",end="")
			

def TrianglePascal(n):
	tab = TrianglePascalVierge(n) 
	i = 2
	
	while i < len(tab):
		j = 1
		while j <= (n):
			
			tab[i][j] = (tab[i-1][j] + tab[i-1][j-1])
			j += 1
		
		i += 1
	return tab

T =TrianglePascal(13)
JoliePascalprint(T)

def LignePascal(T,n):
	tab = T
	ligne = []
	for i in tab[n]:
		if i != 0:
			ligne += [i]
		
	return ligne
print(LignePascal(T,5))

print(binomialfake(5,1))

def VraiBinomial(n,p):
	tab = LignePascal(T,n)
	return(tab[p])
print(VraiBinomial(5,1))



def phoque(n):
	tab = []
	if n == 0:
		return []
		
	elif n == 1:
		A = ['.']
		return A
	elif n == 2:
		A = ['..']
		B = ['-']
		return A + B
	else:
		A = ['.' + x for x in phoque(n-1)]
		B = ['-' + x for x in phoque(n-2)]
		return A + B

for i in range(8):
	print(phoque(i))











"""def phoque(n):
	tab = []
	if n == 1 :
		tab += ["."]
		return tab
	for i in range(n):
		
			if r.randrange(2) == 0:
				
	A = phoque(n-1)
	B = phoque(n-2)
	tab += ['.'+ x for x in A] + ['-' + x for x in B]
	A = tab
	B = A
	return tab
print(phoque(2))"""
		


		
	

