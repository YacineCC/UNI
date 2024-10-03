from pocketnoobj import *

ch = input("saisir une chaine de caracteres :")
i = 0
while i < len(ch) :
	if ch[i].isalpha():
		print(ch[i],": caractere")
	elif ch[i].isdigit():
		print(ch[i],": chiffre")
	else :
		print(ch[i],": special")
	i += 1
