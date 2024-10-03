import math
sqrt = math.sqrt

a = int(input("Nombre a : "))
b = int(input("Nombre b : "))
c = int(input("Nombre c : "))

discri = b**2-(4*a*c)

if discri < 0:
	print("Pas de solutions.")
elif discri > 0:
	x1 = (-b-sqrt(discri))/(2*a)
	x2 = (-b+sqrt(discri))/(2*a)
	print(x1,x2)
	
else :
	x = -(b/(2*a))
	print(x)


