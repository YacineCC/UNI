def ListerVariables(expression):
	tab = []			#Initialisation tableau
	for s in expression:
		if  97 <= ord(s) <= 122 and not(s in tab): #Parcours le tableau et comparer les lettres de l'alphabet avec la fonction ord 
			tab.append(s) 	
	return tab
expression = "!(p + q) * (!p + r) + (p * q)"
test = ListerVariables(expression) #La liste des variables de l'expression d'exemple
print(test)

def DicoVariables(liste):
	i = 0			#Dictionnaire où les clefs sont les variables de "ListerVariable" et leurs valeurs sont des entiers de 0 à n variables, en fonctions de leurs positions dans l'alphabet
	dico = {}
	for s in test:
		dico[s] = i
		i += 1
	return dico
print(DicoVariables(test))
DicoVariables = DicoVariables(test)

def Int2Bin(entier,n):
	binaire = bin(entier)[2:] # Transforme un entier de base 10 en binaire
	if len(binaire) < n:
		binaire = (n-len(binaire))*'0' + binaire # On ajoute des "0" où il manque, par exemple 5 en binaire "101" codé sur 5 bits manquera 2 zeros 00101
	
	return binaire
print(Int2Bin(5,5))

def Bin2Bool(bits):
	tup = tuple()
	for i in bits:
		if i == "0":
			tup += (False,)
		else:
			tup += (True,)
	return tup	
print(Bin2Bool(Int2Bin(1,3)))	


vecteur = Bin2Bool(Int2Bin(1,3)) # Donne des valeurs booleenes bits à bits d'un nombre binaire


	
def Math2Python(expression,vecteur,dicovar):
	dicoOP = {}
	dicoOP["!"] = "not " #Dictionnaire d'opérateurs
	dicoOP["+"] = "or"
	dicoOP["*"] = "and"

	expr = ""
	for s in expression:
		if s in test:
			s = vecteur[dicovar[s]] #On parcours l'expression, si on tombe sur une variable ou un operateur, on le transforme en sa valeure de vérité en prenant sa valeur du dictionnaire (0,1,2,3,... dans le cas de la variable) et prenant l'indice correspondant dans le tuple vecteur
		elif s in dicoOP:
			s = dicoOP[s] 
		expr += str(s)
	
	return expr

print(Math2Python(expression,vecteur,DicoVariables))
expr = Math2Python(expression,vecteur,DicoVariables)

def TableVerite(expression,dicovar):
	L = []
	for i in range(0,2**len(test)): # on parcours les entiers de 0 à 2 ** nombre de variables
		vecteur = Bin2Bool(Int2Bin(i,3)) # le vecteur est le tuple de booleens du nombre i en binaire
		if eval((Math2Python(expression,vecteur,DicoVariables))) == True:
			L.append(1) # On evalue l'expression convertie avec la fonction Math2Python et on ajoute au tableau L 1 si true 0 sinon
		else:
			L.append(0)
	return L
print(TableVerite(expression,DicoVariables))
table = TableVerite(expression,DicoVariables)

def affichage(variables,table):
	for s in variables:
		print (s + " |"," " * 2,end = "",sep = "") # On print les variables en les séparants d'espaces et de barres
		
	
	print("\n"+"―"*(len(variables) * 4 )+"―"+"\n",end="") # On met une barre en bas pour faire jolie, avec le caractere sepaciale "―" en le multipliant par le nombre de variables + les espaces et la barre "|"
	for i in range(2**len(variables)):
		val = Bin2Bool(Int2Bin(i,3)) # On parcours les entiers de 0 à 2** nombre de variables puis on les convertis en binaire
		for s in val: # Dans le vecteur binaire on transforme les 0 en F et 1 en V puis on les sépares avec des barres, le but est d'énumerer les vecteurs pour la partie gauche de la table de verité
			if s == 0:
				s = "F"
			else:
				s = "V"
			print(s + " |",end="")	
		if table[i] == 0:
			print(" F") # La partie droite de la table de verité
		else:
			print(" V")
affichage(test,table)

def FND(TDV,listevar):			# ON regarde où l'expression est vraie et on regarde la valeurs des variables e, mettant "barre" quand la variable est 0
	FND = ""
	for i in range(len(TDV)): # On compte le nombre de valeurs de la table de verité
		if TDV[i]: # Si la valeur dans la table est True ( = 1 )
			vecteur = Bin2Bool(Int2Bin(i,3)) # On transorme sa position dans la table en vecteur booleen à partir de son nombre binaire
			for j in range(len(vecteur)):
				if vecteur[j]: 		# On parcours le vecteur, si la valeur est True on ajoute à la chaine de caracteres FND la variable correspondante grace à l'indice j, par ex dans le tuple vecteur(0,1,0,1) l'indice 2 qui vaut 0 on prend la lettre de la liste de variable qui correspond à l'indice 2 et vu que vecteur[2] == 0 on prendra la lettre de la liste variable avec la barre au dessus.
					FND += listevar[j]
				else:
					FND +=listevar[j]+"\u0304" # Si faux on met "barre" avec \u0304
			
			FND +=" + "
	print("\nFND : \n"+FND[:-2]) # pour enlever le "+" en trop à la fin
	
FND(table,test)

def FNC(TDV,listevar): # Duale avec FND
	FNC = ""
	for i in range(len(TDV)):
		if not TDV[i] :
			vecteur = Bin2Bool(Int2Bin(i,3))
			FNC += "("
			for j in range(len(vecteur)):
				
				if not vecteur[j]:
					FNC += listevar[j] +  "+"
				
				else:
					FNC +=listevar[j]+"\u0304" + "+"
			FNC = FNC[:-1] # pour enlever des caracteres en trop
			FNC += ") * " 
	print("\nFNC : \n"+FNC[:-2])

FNC(table,test)
			


	
