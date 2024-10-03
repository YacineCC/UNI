sussy = [45,32,98,150,401,400,33,133,900]
i = 0
maxi = sussy[0]
deux = sussy[0]
indice1 = i
indice2 = i
while i<len(sussy):
	if deux < sussy[i]:

		deux = sussy[i]
		indice2 = i
		if deux > maxi:
			ham = maxi
			maxi = deux
			deux = ham
			temp = indice1
			indice1 = indice2
			indice2 = temp
		
		
		
	i+=1
print(maxi,indice1,deux,indice2)
	

