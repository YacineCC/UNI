from pocketnoobj import *
ch = input("Entrez une chaine de caracteres : ")
i = 0
nb = ''
al = ''
while i < len(ch):
	if isdigit(ch[i]):
		while i < len(ch) and isdigit(ch[i]) :
			nb += ch[i]
			i+=1 
		nb += ' '
		
	elif isalpha(ch[i]):
		while i < len(ch) and isalpha(ch[i]) :
			al += ch[i]
			i+=1
		al += ' '
			
	
	else :
		i+= 1
	
	
print("Nombres presents :", nb)
print("Mots presents :", al)
		
		
