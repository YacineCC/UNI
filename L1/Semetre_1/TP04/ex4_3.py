tab = ['abc','sus','abcd','lol']
nb = int(input("Longeur de la chaine ? "))
i = 0
newtab = []
indices = []
while i < len(tab):

	if len(tab[i]) == nb:
		newtab += [tab[i]]
		
		indices += [i]
	i+=1
print(newtab,indices)
		
