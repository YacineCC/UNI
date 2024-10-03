def f(x):
	return (chr(x + ord('A')))

def g(x):
	return (ord(x) - ord('A'))

def a(k,x):
	return (x + ord(k)) % 26

def e(k,x):
	return f(a(k,g(x)))

def Chiffrer(clair,clef):
	ch = ''
	i = 0
	for car in clair:
		  
		ch += e(f(ord(clef[i % len(clef)])),car)
		i += 1
	return ch
print(Chiffrer('MATHS','TP'))



def Cribler(N):
	tab = [True] * N
	tab[0],tab[1] = False,False
	i = 0
	for bol in tab:
		if tab[i] == True:
			for j in range(i, N, i):
				if j != i:
					tab[j] = False
		i += 1
	
	premier = []
	for idx, s in enumerate(tab):
		if s:
			premier += [idx]
	return premier
	

print(Cribler(25))

def affiche_premier(N):
	i = 1
	for premier in Cribler(N):
		print('P'+str(i),' :', premier)
		i += 1

#var = Cribler(10**6)
#print(var[2017])

def Factoriser(N):
	tup = ()
	test = Cribler(N)
	i = 0
	while i < N ** (1/2):
		Q = N
		while Q % test[i] == 0 :
			Q = Q // test[i]
			tup += (test[i],)
			
		i += 1
	return tup

print(Factoriser(7896))
print(Factoriser(20378))

def AfficheTable(T):
	for ligne in T:
		for x in ligne:
			print(str(x)," ",end='')
		print()

def Table(n,op):
	expr = ''
	table = ()
	for a in range(n):
		ligne = ()
		for b in range(n):
			expr = '(a ' + op + ' b) % n'
			ligne += ((eval(expr)),)
		table += (ligne,)
	return table
		
print()	
AfficheTable(Table(5,'+'))
print()
AfficheTable(Table(5,'*'))



def mod9(N):
	ch = str(N)
	if len(ch) <= 1:
		if N == 9:
			return 0
		else:
			return N
		
	
		
	while len(ch) > 1:
		s = 0
		for c in ch:
			
			s += int(c)
		ch = str(s)
	
	
	
print()
print(mod9(9))
print()
