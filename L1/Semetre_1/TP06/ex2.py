import random as r

c1,c2,c3,c4,c5,c6 = 0,0,0,0,0,0
for i in range(1,10001):
	a = r.randrange(1,7)
	if a == 1:
		c1 += 1
	elif a == 2:
		c2 += 1
	elif a == 3:
		c3 += 1
	elif a == 4:
		c4 += 1
	elif a == 5:
		c5 += 1
	elif a == 6:
		c6 += 1
print ("nb de 1 : ",c1,"nb de 2 : ",c2,"nb de 3 : ",c3,"nb de 4 : ",c4,"nb de 5 : ",c5,"nb de 6 : ",c6)
