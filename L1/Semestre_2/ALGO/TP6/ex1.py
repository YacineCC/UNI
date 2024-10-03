import random as rd
import matplotlib.pyplot as plt
from math import sin
def Swap(T,i,j):
	aux = T[i]
	T[i] = T[j]
	T[j] = aux



def tri_bulle(T):
	d = (len(T)-1)
	echange = True
	while echange:
		i = 0
		echange = False
		while i < d:
			if T[i] > T[i+1]:
				Swap(T,i,i+1)
				echange = True
			i += 1
		d -= 1
	return T

def alea(n):
	tab =[]
	for i in range(n):
		tab += [rd.randrange(1,2*n+1)]
	return tab


def gen_tableau(n):
	return(tri_bulle(alea(n)))

def recherche_binaire(T,x):
	comp,g,d = 0,0,len(T)-1
	while g <= d:
		m = (g+d)//2
		if T[m] < x:
			comp += 1
			g = m+1
		elif T[m] > x:
			comp += 2
			d = m-1
		else:
			comp += 2
			return m,comp
	return -1,comp
T = gen_tableau(50)

def recherche_ternaire(T,tup):
	comp,g,d = 0,0,len(T)-1
	
	while g <= d:
		tupe = (tup[0],tup[1],tup[2])
		cont = (0,0,0)
		m1,m2 = (2*g+d)//3,(g+2*d)//3
		
		if  T[m1] == tup[0] :
			cont[0] += 1
		elif T[m2] == tup[0]:
			cont [0] += 1
		
		elif T[m1] > x:
			comp += 3
			d = m1-1
		elif T[m2] > x:
			comp += 4
			g = m1+1
			d = m2-1
		else:
			comp += 5
			g = m2+1
	return -1,comp
			

def complexite_binaire(T):
	somme = 0
	for x in T:
		somme += recherche_binaire(T,x)[1]
	return somme/len(T)


def complexite_ternaire(T):
	somme = 0
	for x in T:
		somme += recherche_ternaire(T,x)[1]
	return somme/len(T)


abscisse = [x for x in range(1,5001,10)]
moy_bin = []
moy_tern = []
for n in abscisse:
	tab = gen_tableau(n)
	moy_bin += [complexite_binaire(tab)]
	moy_tern += [complexite_ternaire(tab)]

plt.plot(abscisse,moy_bin,label="Binaire")
plt.plot(abscisse,moy_tern,label="TERNaire")
plt.legend()
plt.show()
		
def recherche_zero(a,b,prec):
	debut,fin = a,b
	m = debut + (fin - debut) / 2
	while fin - debut > prec:
		if sin(debut) * sin(m)
