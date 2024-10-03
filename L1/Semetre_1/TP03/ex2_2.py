from pocketnoobj import *

ch = input("saisir une chaine de caracteres :")
i = 0
test = False
ite = 0
while i < len(ch) :
	if ch[i] == " ":
		test = True
		ite += 1
	i += 1

if test : 
	print("\nLa chaîne contient",ite,"espaces\n")
else :
	print("\nLa chaîne ne contient pas espace\n")
