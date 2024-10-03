a = int(input("Entrez l'entier a : "))
op = input("Choisir l'opérateur : ")
b = int(input("Entrez l'entier b : "))

r = "Le résultat est" 

print("Valeur de a : ",a)
print("Valeur de b : ",b)
print("Choix d’operateur parmi (+,-,*,/) : ",op)
if op == "+":
	print(r,a,op,b,"=",a+b)
	print("Cette expression est de type",type(a+b))
elif op == "-":
	print(r,a,op,b,"=",a-b)
	print("Cette expression est de type",type(a-b))
elif op == "*":
	print(r,a,op,b,"=",a*b)
	print("Cette expression est de type",type(a*b))
elif op == "/":
	print(r,a,op,b,"=",a/b)
	print("Cette expression est de type",type(a/b))
	



