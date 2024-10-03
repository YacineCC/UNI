ch = input("Saisir chaîne : ")
i = 0
bop = ''
while i < len(ch) :
	if ch[i] != ' ':
		bop += ch[i]	
	i += 1	
print(bop)
