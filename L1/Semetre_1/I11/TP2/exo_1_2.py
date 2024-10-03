n1 = float(input("\nPremière note : "))
n2 = float(input("Deuxième note : "))
n3 = float(input("Troisème note : "))

	
moyenne = (n1+n2+n3) / 3

if moyenne >= 10:
	if (n1 or n2 or n3)<10 :
		print("\nsemestre validé par compensation")
	else :
		print("\nsemestre validé")
else : 
	print("\nsession rattrapage")



