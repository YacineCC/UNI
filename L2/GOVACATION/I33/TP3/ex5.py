from random import randrange

def generateur(p):
	g = randrange(2,p-1)
	formule = pow(g,((p-1)//2),p) 
	while formule == 1:
		g = randrange(2,p-1)
		formule = pow(g,((p-1)//2),p)
	
	return g

print(generateur(89))
	
