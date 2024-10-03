n = float(input("Alors on a eu quoi comme note?\n"))
if n >= 10:
	print("Bon c'est bon tu passe en L2")
	
	if n >= 12 and n <14:
		print("\nMention assez bien")
	
	elif n >= 14 and n <16:
		print("\nMention bien")
	
	elif n>= 16 :
		print("\nMention très bien")

else :
	print("Dommage")
