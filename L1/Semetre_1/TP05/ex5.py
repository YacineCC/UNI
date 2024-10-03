from math import *

def factorielle(n):
	if n == 0:
		return 1
	else :
		i = 1
		fact = 1
		while i <= n:
			fact *= i
			i += 1
		return fact
	
def puissance(x,n):
	pui = x**n
	return pui
	
def serie_exp(x,n):
	seri = 0
	i = 0
	while i <= n:
		seri += (x**i) / factorielle(i)
		i += 1
	return seri
	
x = float(input("Flotant : "))
p = int(input("Précision : "))
continuer = True
o = 0
while continuer:
	if abs(serie_exp(x,o) - exp(x)) >= 10**-p:
		o += 1
	else :
		continuer = False
print(o)
		
	
