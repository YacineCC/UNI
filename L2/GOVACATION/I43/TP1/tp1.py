import random

def pgcd(a,b):
	while(b >= 1):
		a,b = b,a%b
	
	return a



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



def gen_cle(n):

	
	mu = random.randint(2,n-1)
	l = random.randint(1,n-1)
	test = egcd(n,mu)
	while(test[0] != 1):
		mu = random.randint(2,n-1)
		test = egcd(n,mu)
	
	return([mu,l,test[2]%n])




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
				tmp = tmp % 26
				
				chiffre += doci[tmp]
			else:
				chiffre += ' '
			i = i + 1
		
		return chiffre
		
		
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

def dechiffrecrypto(cryptogramme):
	Dicodoci = dicodoci()
	dico = Dicodoci[0]
	doci = Dicodoci[1]
	
		
	cryptogramme = lisse(cryptogramme)
	freq = analyse_freq(cryptogramme)
	
	bigramme = freq[0] + freq[3]
	#bigramme = doci[resolution_affine(bigramme)[0]] + doci[resolution_affine(bigramme)[1]]
	mu = resolution_affine(bigramme)[0]
	l = resolution_affine(bigramme)[1]
	invmu = egcd(29,mu)[2]
	
	cle = [mu,l,invmu]
	print(cle)
	clair = dechiffre(cryptogramme,cle)
	return clair
	
	#return cryptogramme,freq,bigramme,cle

cryptogramme =".b,wnf.,nrwfwv..knarfp,mrvypbhmvpv,.d.apapvuw.yfpvhpmb.vrwbpaarvbnarvu.fdpvba.bnfryrvd.wfbd.b.blmufpzz.bnrwfd.hrwsfmfjw.a.b,a.nawbyf.jw.v,t.,d.smv.jwrmmabxpum,d..bh.vx.b,npbbwfnf.vpv,'hpfh.,,.hrzlmvpmbrv.b,,f.byf.jw.zz.v,w,mamb..dpvbapapvuw.yfpvhpmb.t.v.yy.,'.b.b,wvs.fl.hrviwuw.papd.wkm.z.n.fbrvv.dwbmvuwam.fpwnf.b.v,d.axmvdmhp,my'h.jwmbmuvmym.jwxma.b,w,mamb.dpvbd.vrzlf.wb.bnqfpb.btd.nawb'.b.b,.upa.z.v,w,mamb.hrzz.nfrvrzn.fbrvv.anrwfd.bmuv.fapd.wkm.z.n.fbrvv.dwbmvuwam.ftzpmb.bvx.b,npbb.wa.z.v,wvs.fl.rwwvnfrvrz'ma.b,.upa.z.v,w,mamb.dpvbd.bzr,bhrwfpv,b,.abjw.a.b'd.b'h.b'z.b',.b'g.b'yf.bjw..,lm.vdxpw,f.b.vhrf.t.vf.bwz.'a.lmufpzz.a.nawbyf.jw.v,.vyfpvhpmb.b,.b'jwm.b,rzvmnf.b.v,dpvbapapvuw.yfpvhpmb.t.v,pv,jw.arhw,.wfvp,my'ma.b,yphma.d.nf.vdf.nrwfphjwmbaxw,mambp,mrvd.h.n.,m,lmufpzz.'zpmbma.b,ypbhmvpv,d.srmfpjw.anrmv,ma.b,mznrf,pv,dpvbapufpzzpmf..,a.srhplwapmf.d.apapvuw.yfpvhpmb.t"


print(dechiffrecrypto(cryptogramme))

