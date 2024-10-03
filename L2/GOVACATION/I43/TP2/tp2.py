def egcd(x,y):
	n = x
	
	u = 1
	v = 0
	
	u1 = 0
	v1 = 1
	
	while(y > 1):
		
		q = x // y
		
		u,u1 = u1,u-(q*u1)
		v,v1 = v1,v-(q*v1)
		
		x,y = y,x%y
	
	return[y,u1%n,v1%n]

def lisse(texte):  #enleve la casse et les accents d un string
	
	accents = {}
	
	accents[' '] = '' #a mettre en commentaire en fonction de l exercice
	accents['!'] = ''
	accents['?'] = ''
	#accents["'"] = ''
	#accents[','] = ''
	#accents['.'] = ''
	accents[':'] = ''
	
	accents['à'] = 'a'
	accents['â'] = 'a'
	accents['ä'] = 'a'
	
	accents['é'] = 'e'
	accents['è'] = 'e'
	accents['ê'] = 'e'
	accents['ë'] = 'e'
	
	accents['ô'] = 'o'
	accents['ö'] = 'o'
	
	accents['ï'] = 'i'
	accents['î'] = 'i'
	
	accents['ç'] = 'c'
	 
	
	texte = texte.lower()
	
	resultat = ""
	
	i = 0
	while(i < len(texte)):
		if(texte[i] in accents):
			resultat += accents[texte[i]]
		else:
			resultat += texte[i]
		i += 1
	return resultat

def dicodoci(): #renvoi une liste avec deux dictionnaires le premier qui associe une lettre a un nombre (a:0 b:1)
				#et le deuxieme sa reciproque
	dico = {}
	doci = {}
	for i in range(ord('a'), ord('z')+1):
		dico[chr(i)] = i - 97
		doci[i-97] = chr(i)
	"""
	#dico[' '] = 26 #a mettre en commentaire en fonction de l exercice
	dico[','] = 26
	dico["'"] = 27
	dico['.'] = 28
	#doci[26] = ' '
	doci[26] = ','
	doci[27] = "'"
	doci[28] = '.'
	"""
	return[dico,doci]

def dechiffre(cryptogramme, k):
	Dicodoci = dicodoci()
		
	dico = Dicodoci[0]
	"""
	dico[','] = 26 #a mettre en commentaire en fonction de l exercice
	dico["'"] = 27
	dico["."] = 28
	"""
	doci = Dicodoci[1]
	"""
	doci[','] = 26 #a mettre en commentaire en fonction de l exercice
	doci["'"] = 27
	doci["."] = 28
	"""
	
	
	clair = ""
	i = 0
	while(i < len(cryptogramme)):
		if(cryptogramme[i] != ' '):
			tmp = dico[cryptogramme[i]]
			tmp = tmp - k[1]
			tmp = tmp * k[2]
			tmp = tmp % len(dico)
			clair += doci[tmp]
		else:
			clair += ' '
		i += 1
	return clair


def analyse_freq(cryptogramme):
	cryptogramme = lisse(cryptogramme)
	dico = {}
	for i in range(ord('a'), ord('z')+1): # initialisation d un dictionnaire a:0 b:0 c:0 pour compter le nombre d occurrences des lettres
										  # d'un cryptogramme
		dico[chr(i)] = 0
	#dico[','] = 0 #a mettre en commentaire en fonction de l exercice
	#dico["'"] = 0
	#dico["."] = 0
	
	lettremaxiA = '' #La lettre qui apparait le plus de fois
	lettremaxiB = '' #La lettre qui apparait le plus de fois juste apres maxiA	
	nbA = 0 # nb d occurrences A
	nbB = 0 # nb d occurrences B

	i = 0
	while(i < len(cryptogramme) -1):	#Calcul de la lettre qui apparait le plus de fois
		dico[cryptogramme[i]] += 1
		if(dico[cryptogramme[i]] > nbA):
			nbA = dico[cryptogramme[i]]
			lettremaxiA = cryptogramme[i]
		i += 1
	
	for i in range(ord('a'), ord('z')+1): #Réinitialisation du dico pour tester la lettre qui apparait le plus de fois apres la lettremaxiA
		dico[chr(i)] = 0
	i = 0
	#dico[','] = 0 #a mettre en commentaire en fonction de l exercice
	#dico["'"] = 0
	#dico["."] = 0
	
	while(i < len(cryptogramme) -1):
		
		if(cryptogramme[i] == lettremaxiA):
			
			dico[cryptogramme[i+1]] += 1
			if(dico[cryptogramme[i+1]] > nbB):
				nbB = dico[cryptogramme[i+1]]
				lettremaxiB = cryptogramme[i+1]
		i += 1
	
	frequenceA = str(round((nbA/len(cryptogramme))*100,2))+'%'
	frequenceB = str(round((nbB/nbA)*100,2))+'%'
	
	
	return [lettremaxiA,nbA,frequenceA,lettremaxiB,nbB,frequenceB]


def alt_analyse_freq(cryptogramme):
	
	dico = {}
	for i in range(ord('a'), ord('z')+1):
		dico[chr(i)] = 0
	
	for i in cryptogramme:
		dico[i] += 1
	
	return dico


def enumere_keys(n):
	
	listecle = []
	
	for i in range(1,n):
		
		if(egcd(n,i)[0] == 1):
			tmp = []
			inv = egcd(n,i)[2]
			
			for j in range(1,n):
				tmp += [[i,j,inv]]
			
			listecle += tmp
	return listecle

def file2str(fic):
	
	nomfic = fic
	cryptogramme = ""
	fic = open(nomfic,'r')
	
	for ligne in fic:
		for car in ligne:
			if car != '\n':
				cryptogramme += car
		
	fic.close() 
	
	return cryptogramme

def dicofreq():
	dicofreq = {}
	dicofreq['a'] = 8.15
	dicofreq['b'] = 0.97
	dicofreq['c'] = 3.15
	dicofreq['d'] = 3.73
	dicofreq['e'] = 17.39
	dicofreq['f'] = 1.12
	dicofreq['g'] = 0.97
	dicofreq['h'] = 0.85
	dicofreq['i'] = 7.31
	dicofreq['j'] = 0.45
	dicofreq['k'] = 0.02
	dicofreq['l'] = 5.69
	dicofreq['m'] = 2.87
	dicofreq['n'] = 7.12
	dicofreq['o'] = 5.28
	dicofreq['p'] = 2.80
	dicofreq['q'] = 1.21
	dicofreq['r'] = 6.64
	dicofreq['s'] = 8.14
	dicofreq['t'] = 7.22
	dicofreq['u'] = 6.38
	dicofreq['v'] = 1.64
	dicofreq['w'] = 0.03
	dicofreq['x'] = 0.41
	dicofreq['y'] = 0.28
	dicofreq['z'] = 0.15
	
	return dicofreq

def brute_force(fic,n,eps):
	listecle = enumere_keys(26)
	cryptogramme = file2str(fic)
	Dicofreq = dicofreq()
	
	for i in listecle:
		
		clair = dechiffre(cryptogramme,i)
		freq = alt_analyse_freq(clair)
		
		bonnefreq = True
		i = ord('a')
		while(i <= ord('z') and bonnefreq):
			
			freqlettre = (freq[chr(i)] / len(cryptogramme))*100
									
			if(freqlettre > Dicofreq[chr(i)] + eps or freqlettre < Dicofreq[chr(i)] - eps ):
				bonnefreq = False
			i += 1
			
		if(bonnefreq):
			print(clair)
			print()
			


n = 26
eps = 3

(brute_force("crypto1.txt",n,eps))
(brute_force("crypto2.txt",n,eps))
(brute_force("crypto3.txt",n,eps))
(brute_force("crypto4.txt",n,eps))
(brute_force("crypto5.txt",n,eps))
