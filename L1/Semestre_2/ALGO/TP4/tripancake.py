def swap(T,a,b):
	tp = T[a]
	T[a] = T[b]
	T[b] = tp
	return T
def retourner(T,i):
	n = len(T) - 1
	while n >= i:
		swap(T,i,n)
		i += 1
		n -= 1

def maxi(T,i):
	maxi = i
	while i < len(T):
		if T[maxi] < T[i]:
			maxi = i
		i += 1
	return maxi
print(maxi([4 ,3 ,5 ,2 ,1 ,6],0))

def tri_pancake(T):
	tab = []
	k = 0
	while k < len(T)-1:
		
		tab += [maxi(T,k)]
		retourner(T,maxi(T,k))
		retourner(T, k)
		
		tab += [k]
		print(T)
	
		
		
				
		k += 1
	
	return  tab
print(tri_pancake([4,3,5,2,1,6]))
	
"""f = open('dico-fr.txt')
dico = []
for mot in f:
	dico += [mot[:-1]]
print(dico)
f.close()"""
