ch = input("Entrez une chaine de caracteres : ")

i = 0
j = -1
if len(ch) % 2 == 0 :
	while i < len(ch) // 2 :
		print(ch[i] + ch[j]) 
		j -= 1
		i += 1
else :
	while i < len(ch) // 2+1 :
		if j > -(len(ch) // 2 + 1) :	
			print(ch[i] + ch[j])	
			i += 1
			j -= 1
		else :
			print(ch[i])	
			i += 1
			j -= 1

			
	
