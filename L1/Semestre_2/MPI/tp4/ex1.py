def Lire():
	chaine = input("Permutation = ")
	return tuple([int(x)-1 for x in chaine.split()])



def Ecrire(s):
	for i in s:
		print(i + 1,end=" ")
	print()

def EstPermutaion(s):
	n = len(s)
	for i in s:
		
		if not i in range(n):
			return False
			
	for i in range(n):
		if not i in s:
			return False
			
	return True
			
print(EstPermutaion((2,1,1,3)))

def Inverser(s):
	n = len(s)
	tab = [0] * n
	
	for el in s:
		tab[s[el]] = el
	return tuple(tab)
	
	
def Composer(s,t):
	n = len(s)
	tupl = ()
	for i in range(len(s)):
		tupl += (s[t[i]],)
	return tupl

	
def Orbite(k,s):
	k = k - 1
	tup = ()
	amo = s[k]
	while amo != k:
		tup += (amo,)
		amo = s[amo]
	tup += (amo,)
	return tup

def Signature(s):
	som = 0
	for i in range(len(s)):
		
		som += len(Orbite(i,s))
	sign

Ecrire(Orbite(3,Lire()))


#Ecrire((Composer(Lire(),(Inverser(Lire())))))
		
		
		



					
		
