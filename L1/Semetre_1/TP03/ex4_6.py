from pocketnoobj import *
ch = input("Entrez une chaine de caracteres : ")
i = 0
nb = 0
al = 0
while i < len(ch):
	if isdigit(ch[i]):
		while i < len(ch) and isdigit(ch[i]) :
			i+=1
		nb += 1 
	
		
	elif isalpha(ch[i]):
		while i < len(ch) and isalpha(ch[i]) :
			i+=1
		al += 1
		
			
	
	else :
		i+= 1
	
	
print("Nombres de nombres :", nb)
print("Mots de mots :", al)
		
		
