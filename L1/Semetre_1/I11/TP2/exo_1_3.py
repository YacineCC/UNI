hc = input("Heure du cours : ")

c = int(hc[0:2])
d = int(hc[3:5])

h = input("Entrez une heure : ")



a = int(h[0:2])
b = int(h[3:5])

if (a or c) > 24:
	print("Error semantique.")
if (b or d) > 59:
	print("Error semantique! ")

else :

	if a == c:
		if b == d :
			print ("Vous êtes à l'heure")
		elif b > d :
			print("Vous êtes en retard")
		else :
			print("Vous êtes en avance")
	elif a > c:
		print("Vous êtes en retard")
	else :
		print("Vous êtes en avance")
		




