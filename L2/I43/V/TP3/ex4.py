def egcd(a,n):
	u = 1
	v = 0
	
	u1 = 0
	v1 = 1

	while(n>0):
		q = a//n
		a,n = n,a%n
		
		u,u1 = u1, u - (q*u1)
		v,v1 = v1, v - (q*v1)

	return [a,u,v]

def pgcd(a,n):
	
	while n != 0:
		a,n = n,a%n
	return a

#remplace les accents, la ponctuation et la casse d'un texte
def lisse(texte):
	dico = {}
	dico["é"] = "e"
	dico["è"] = "e"
	dico["ê"] = "e"
	dico["ë"] = "e"
	dico["à"] = "a"
	dico["â"] = "a"
	dico["ä"] = "a"
	dico["ô"] = "o"
	dico["ö"] = "o"
	dico["ï"] = "i"
	dico["î"] = "i"
	dico["ç"] = "c"
	dico["!"] = ""
	dico["."] = ""
	dico["?"] = ""
	dico[","] = ""
	dico[";"] = ""
	dico[":"] = ""
	dico[" "] = ""
	
	texte = texte.lower()
	texte_final = ""
	i = 0
	while(i < len(texte)):
		if(texte[i] in dico.keys()):
			texte_final += dico[texte[i]]
		else:
			texte_final += texte[i]
		
		i += 1
	return texte_final


def vignere_chiffre(clair,k):
	clair = lisse(clair)
	dico = {}
	doci = {}
    #creation des deux dictionnaire a:0 b:1 ... et 0:a 1:b ...
	for i in range(ord('a'), ord('z') + 1):
		dico[chr(i)] = i - 97
		doci[i -97] = chr(i)
	
	lcle = len(k)
	chiffre = ""	
	i = 0
    #dechiffrement avec l'indice i mod la longueur de la cle
	while(i < len(clair)):
		chiffre += doci[(dico[clair[i]] + dico[k[i%lcle]]) %26]
		i += 1
	return chiffre

def vignere_dechiffre(cryptogramme,k):
	dico = {}
	doci = {}
	for i in range(ord('a'), ord('z') + 1):
		dico[chr(i)] = i - 97
		doci[i -97] = chr(i)
	
	lcle = len(k)
	clair = ""
	
	i = 0
	while(i < len(cryptogramme)):
		clair += doci[(dico[cryptogramme[i]] - dico[k[i%lcle]])%26]
		i += 1
	return clair

	
def vignere(texte,k,mode):
	dico = {}
	doci = {}
	for i in range(ord('a'), ord('z') + 1):
		dico[chr(i)] = i - 97
		doci[i -97] = chr(i)
	
	lcle = len(k)
	clair = ""
	
	i = 0
	while(i < len(texte)):
		clair += doci[(dico[texte[i]] + mode*dico[k[i%lcle]])%26]
		i += 1
	return clair

#retourne un tableau avec tous les trigrammes glissants possibles
def trigrammes(texte):
	big = []
	i = 0
	while(i < len(texte)-2):
		ch = ""
		for k in range (3):
			ch += texte[i+k]
		big += [ch]
		i += 1
	return big

#cherche le trigramme le plus frequent du cryptogramme
def freqtri(texte):
	big = trigrammes(texte)
	freq = {}
	for i in range(len(big)):
		freq[big[i]] = 0

	freqtrimaxi = freq[big[0]]
	trimaxi = big[0]

	for j in range(len(big)):
		if(big[j] in freq.keys()):
			freq[big[j]] += 1
			if freq[big[j]] > freqtrimaxi:
				freqtrimaxi = freq[big[j]]
				trimaxi = big[j]
				
	return trimaxi,freqtrimaxi

#retourne un tableau avec toutes les distances entre les occurences du trigramme maximal
def distfreqtrimax(texte):
	tab = []
	trimaxi = freqtri(texte)[0]
	big = trigrammes(texte)
	i = 0
	k = 0
    #on cherche d'abord la premiere occurence du trigramme maximal
	while(big[i] != trimaxi):
		i += 1
	#puis on incremente k et on le rentre dans le tab de sorti et on remet k a 0
	while(i < len(big)):
		if(big[i] == trimaxi):
			tab += [k]
			k = 0
		k += 1
		i += 1
	
	return tab
#retourne la longueur de la cle
def lencle(texte):
	
	tab = distfreqtrimax(texte)
	
	i = 1
	pgcdi = tab[0]
	n = len(tab)
    #on fait le pgcd de tous les elements du tableau
	while(i < n):
		pgcdi = pgcd(tab[i],pgcdi)
		i += 1
	return pgcdi

#retourne un tableau avec toutes les sous chaines en fonction de la longueur de la cle
def sous_chaines(texte):
	lcle = lencle(texte)
	tab = []
	k = 0
	while k < lcle:
			ch = ""
			for i in range(0,len(texte)-lcle,lcle):
				ch += texte[i+k]
				
			tab += [ch]
			k += 1
	return tab

#renvoi la lettre avec la frequence maximale d'un texte
def lettre_max(texte):
	freq = {}
	for i in range(ord('a'),ord('z')+1):
		freq[chr(i)] = 0
	
	lettremaxi = ''
	nbmaxi = 0
	i = 0
	while(i < len(texte)):
		freq[texte[i]] += 1
		if freq[texte[i]] > nbmaxi:
			nbmaxi = freq[texte[i]]
			lettremaxi = texte[i]
		i += 1	
	
	return lettremaxi

# lmsc : lettre max sous chaine, renvoi un tableau avec la lettre de frequence maximale de chaques sous chaines
def lmsc(texte):
	sc = sous_chaines(texte)
	tab = []
	for j in sc:
		tab += [lettre_max(j)]
	return tab

#renvoi la cle avec la transformation de cesar en supposant que la lettre la plus frequence est code par la lettre e
def key_finder(texte):
	tab = lmsc(texte)
	ch = "" 
	for j in tab:
		ch += chr((ord(j)-4))
	return ch

#cryptogramme = "tcqhrxwwfqiunrhigcuwzsaumzrpwfuhwyirgmrsvkvovmmbefwkfvwtqqblyirfmbigababwmexgwtzrpmzxpguahqbqpywusawjmrndbsyomyialqbqlabiakipyhygiqazsqhtgmdmmdrqaqvqwtivtcqvrkasawqdtbmzzhlqxiflawqlnrmpatsqhtgmqgvbruczivexcewizgrhifglkgpvwzsrwxayelibgvizwymqbbvxtvnkmgchzpialtshuaqrficsshzusakvchvamrfdmabwygidmmrryqqrqjiwrqbzsfuwbihzeegawbftcqhrnqsagzmmrfbbbvbqbgwabbxaeieawbfsmdhhkkczpmpifeifvqaeeakjchvaapruwazhlqwesvrbqvqyekaoavkmvgwyirgqdiqwxzhvygissqfrgmbphkyirsmzwrjlscoceprewhdxmqwghifgrcfmywahgrcfehlwiegmzshkqzrvbqragcgvomexywamzewxiqwvcgumnifgqbqhkaqzmvwpdbusavmbbwzqfrkwwagmoszhzsagzqigvmhehkaqcjqgdxmhmiwtszrbcyricsildqrblzsydvsyrjqquhmzqblasghvqbcjmgflwzwdmmjvymzsgjmqnsiomgwiqbpugrvicsedmolnfosedxmvgsoseqwemqwmgrwvawfwvhvpmzxfwbehhduzrdmhelodezemehhygmagcgedxbiydmopkicyravggdvfpvexcewizgrvmgchbuxfewhftcugbexcfhvfrblzsydvsyr"

cryptogramme = "tcqhrxwwfqiunrhigcuwzsaumzrpwfuhwyirgmrsvkvovmmbefwkfvwtqqblyirfmbigababwmexgwtzrpmzxpguahqbqpywusawjmrndbsyomyialqbqlabiakipyhygiqazsqhtgmdmmdrqaqvqwtivtcqvrkasawqdtbmzzhlqxiflawqlnrmpatsqhtgmqgvbruczivexcewizgrhifglkgpvwzsrwxayelibgvizwymqbbvxtvnkmgchzpialtshuaqrficsshzusakvchvamrfdmabwygidmmrryqqrqjiwrqbzsfuwbihzeegawbftcqhrnqsagzmmrfbbbvbqbgwabbxaeieawbfsmdhhkkczpmpifeifvqaeeakjchvaapruwazhlqwesvrbqvqyekaoavkmvgwyirgqdiqwxzhvygissqfrgmbphkyirsmzwrjlscoceprewhdxmqwghifgrcfmywahgrcfehlwiegmzshkqzrvbqragcgvomexywamzewxiqwvcgumnifgqbqhkaqzmvwpdbusavmbbwzqfrkwwagmoszhzsagzqigvmhehkaqcjqgdxmhmiwtszrbcyricsildqrblzsydvsyrjqquhmzqblasghvqbcjmgflwzwdmmjvymzsgjmqnsiomgwiqbpugrvicsedmolnfosedxmvgsoseqwemqwmgrwvawfwvhvpmzxfwbehhduzrdmhelodezemehhygmagcgedxbiydmopkicyravggdvfpvexcewizgrvmgchbuxfewhftcugbexcfhvfrblzsydvsyr"

print((trigrammes(cryptogramme)))
print(freqtri(cryptogramme))
print(distfreqtrimax(cryptogramme))
print(lencle(cryptogramme))
print(sous_chaines(cryptogramme))
print(lmsc(cryptogramme))
k = key_finder(cryptogramme)
print(k)
print(vignere_dechiffre(cryptogramme,k))
