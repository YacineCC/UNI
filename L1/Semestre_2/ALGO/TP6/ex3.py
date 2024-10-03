nb = int(input("longeur mot "))
f = open("dico-fr.txt")
r = f.readlines()
liste = []
for i in r:
	if len(i) == nb+1:
		liste += [i[:-1]]


def triche_pendu(lettre,pos, liste):
	tab = []
	for i in liste:
		for p in pos:
			if i[int(p)] == lettre:
				tab += [i]
	return tab

def not_contain(liste,lettre):
	L = []
	for mot in liste:
		if not lettre in mot :	
			L += [mot]
	return L

			
	
	



essai = 0
while essai <= 13:
	a = input("lettre ")
	while True:
		test = input("Lettre dans le mot ? (o ou n): ")
		if test.isalpha():
			break
	if test.upper() == 'O':
		b = input("position (sous la forme indice1 indice2 ...): ").split(' ')

		liste = triche_pendu(a, b, liste)
	else:
		liste = not_contain(liste, a)

		
	print("il reste",len(liste),"mots possibles")
	if len(liste) < 20:
		print(liste)
	essai += 1
	
	
	

