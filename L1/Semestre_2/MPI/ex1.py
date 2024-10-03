def Lecture(nomfichier):
	fichier = open(nomfichier,"r")
	liste = fichier.readlines()
	G = {}
	X = set()
	Y = set()
	
	for s in liste:
		couple = s.rstrip().split(">")
		if couple[0] and couple[1]:
			
			if not couple[0] in G.keys():
				G[couple[0]] = set(couple[1])
			else:
				G[couple[0]] = G[couple[0]] | set(couple[1])
		if couple[0]:	
			X.add(couple[0])
		if couple[1]:
			Y.add(couple[1])
	return (X,G,Y)
	

C = Lecture("correspondance.txt")

def Affiche(c):
	print("X = ",str(c[0]).replace("'",''))
	print("G = ",str(c[1]).replace("'",''))
	print("Y = ",str(c[2]).replace("'",''),end='\n\n')

Affiche(C)

def Reciproque(C):
	X = C[2]
	Y = C[0]
	G = {}
	for s in C[1].keys():
		for j in C[1][s]:
			if not j in G.keys():
				G[j] = set(s)
			else:
				G[j] = G[j] | set(s)
		
	return (X,G,Y)
Crep = Reciproque(Lecture("correspondance.txt"))
Affiche(Crep)

def ImageDirect(C,A):
	G = set()
	for s in C[0]:
		if s in A:
			G = G | C[1][s]
	return G
print(ImageDirect(C,{"a"}))



def ImageReciproque(C,A):
	DEEZ = set()
	for s in C[2]:
		if s in A:
			DEEZ = DEEZ | Reciproque(C)[1][s]
	return DEEZ
print(ImageReciproque(C,{'2', '1'}))


def Composer(g,f):
	X = g[0]
	Y = f[2]
	G = dict()
	
	for s in f[1]:
		G[s] = ImageDirect(g,f[1][s]) 
	return (X,G,Y)


print(Composer(Crep,C))

def EstFonction(C):
	for s in C[1].keys():
		if len(C[1][s]) > 1:
			return False
		else:
			return True
	
print(EstFonction(C))


def EstApplication(C):
	
	if EstFonction(C) and len(C[0]) == len(C[1]):
		return True
	return False

print(EstApplication(C))


def EstInjection(C):
	if EstApplication(C) and EstFonction(Crep):
		return True
	return False
print(EstInjection(C))
def EstSurjection(C):
	if EstApplication(C):
		for s in C[0]:
			if s not in C[1].keys():
				return False 
		return True
	return False

print(EstSurjection(C))



























