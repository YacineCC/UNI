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

def vigenere_chiffre(clair,k):
	Dicodoci = dicodoci()
		
	dico = Dicodoci[0]
	doci = Dicodoci[1]
	
	clair = lisse(clair)
	chiffre = ""
	
	i = 0
	while(i < len(clair)):
		
		tmp = dico[clair[i]] + dico[k[i%len(k)]]
		chiffre += doci[tmp % 26]
			
		
		i += 1
	
	return chiffre

def vigenere_dechiffre(cryptogramme,k):
	Dicodoci = dicodoci()
		
	dico = Dicodoci[0]
	doci = Dicodoci[1]
	
	clair = ""
	
	i = 0
	
	while(i < len(cryptogramme)):
		tmp = dico[cryptogramme[i]] - dico[k[i%len(k)]] 
		clair += doci[tmp % 26]
		i += 1
	
	return clair

def vigenere(texte,k,mode):
	
	Dicodoci = dicodoci()
		
	dico = Dicodoci[0]
	doci = Dicodoci[1]
	
	texte = lisse(texte)
	resultat = ""
	
	i = 0
	
	while(i < len(texte)):
		tmp = dico[texte[i]] + mode * dico[k[i%len(k)]] 
		resultat += doci[tmp % 26]
		i += 1
	
	return resultat


def trigrammes(texte):
	
	i = 0
	L = []
	
	while(i < len(texte) -2):
		ch = ""
		for k in range(3):
			ch += texte[i+k]
		
		L += [ch]
		i += 1
	return L






"""
clair = "Bonjour à tous"
k = "anneau"

print(vigenere_chiffre(clair,k))
"""
"""
cryptogramme = "bbanoorngsum"
cle = "anneau"

print(vigenere_dechiffre(cryptogramme,cle))
"""
"""
clair = "Bonjour à tous"
cryptogramme = "bbanoorngsum"
cle = "anneau"

print(vigenere(clair,cle,1))
print(vigenere(cryptogramme,cle,-1))
"""


