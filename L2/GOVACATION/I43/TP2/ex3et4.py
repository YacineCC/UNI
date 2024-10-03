def egcd(x,y):
	n = x
	u = 1
	v = 0
	
	u1 = 0
	v1 = 1
	
	
	while(y > 1):
		
		q = x // y
		x,y = y,x % y
		
		u1,u = u-(q*u1),u1
		v1,v = v-(q*v1),v1
		
	return([y,u1%n,v1%n])
	
def dicodoci(): #renvoi une liste avec deux dictionnaires le premier qui associe une lettre a un nombre (a:0 b:1)
				#et le deuxieme sa reciproque
	dico = {}
	doci = {}
	for i in range(ord('a'), ord('z')+1):
		dico[chr(i)] = i - 97
		doci[i-97] = chr(i)
	
	#dico[' '] = 26 #a mettre en commentaire en fonction de l exercice
	dico[','] = 26
	dico["'"] = 27
	dico['.'] = 28
	#doci[26] = ' '
	doci[26] = ','
	doci[27] = "'"
	doci[28] = '.'
	return[dico,doci]

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
def dechiffre(cryptogramme, k):
	Dicodoci = dicodoci()
		
	dico = Dicodoci[0]
	dico[','] = 26 #a mettre en commentaire en fonction de l exercice
	dico["'"] = 27
	dico["."] = 28
	doci = Dicodoci[1]
	doci[','] = 26 #a mettre en commentaire en fonction de l exercice
	doci["'"] = 27
	doci["."] = 28
	
	
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
	dico[','] = 0 #a mettre en commentaire en fonction de l exercice
	dico["'"] = 0
	dico["."] = 0
	
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
	dico[','] = 0 #a mettre en commentaire en fonction de l exercice
	dico["'"] = 0
	dico["."] = 0
	
	while(i < len(cryptogramme) ):
		
		if(cryptogramme[i] == lettremaxiA):
			
			dico[cryptogramme[i+1]] += 1
			if(dico[cryptogramme[i+1]] > nbB):
				nbB = dico[cryptogramme[i+1]]
				lettremaxiB = cryptogramme[i+1]
		i += 1
	
	frequenceA = str(round((nbA/len(cryptogramme))*100,2))+'%'
	frequenceB = str(round((nbB/nbA)*100,2))+'%'
	
	
	return [lettremaxiA,nbA,frequenceA,lettremaxiB,nbB,frequenceB]


def resolution_affine(bigramme):
	
	Dicodoci = dicodoci()
	dico = Dicodoci[0]
	doci = Dicodoci[1]
	
	x = dico[bigramme[0]]
	y = dico[bigramme[1]]
	
	mu = ((y-x)*egcd(29,14)[2])%29
	l = (x-4*mu)%29
	
	return[mu,l]



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


def cryptanalyse(fic):
	
	cryptogramme = file2str(fic)
	
	freq = analyse_freq(cryptogramme)
	
	bigramme = freq[0] + freq[3]
	
	bigramme = resolution_affine(bigramme)
	
	mu = bigramme[0]
	l = bigramme[1]
	inv = egcd(29,mu)[2]
	cle = [mu,l,inv]
	clair = dechiffre(cryptogramme,cle)
	return clair,cle
	
def chiffre(clair, k):
		clair = lisse(clair)
		chiffre = ""
		Dicodoci = dicodoci()
		
		dico = Dicodoci[0]
		doci = Dicodoci[1]
		
		
		i = 0
		while(i < len(clair)):
			if(clair[i] != ' '):
				tmp = dico[clair[i]]
				tmp = tmp * k[0]
				tmp = tmp + k[1]
				tmp = tmp % len(dico)
				
				chiffre += doci[tmp]
			else:
				chiffre += ' '
			i = i + 1
		
		return chiffre


clair = cryptanalyse("crypto6.txt")[0]
cle = cryptanalyse("crypto6.txt")[1]


print(chiffre(clair,cle))
	
#print(cryptanalyse("crypto6.txt"))
