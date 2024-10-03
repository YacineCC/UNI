import matplotlib.pyplot as plt
from math import pi,cos,sin
abscisse = []
abscisse_trigo = []
for i in range(10):
	abscisse += [i]


carre = []
for i in range(len(abscisse)):
	carre += [abscisse[i]**2]

cube = []
for i in range(len(abscisse)):
	cube += [abscisse[i]**3]

def intervalle(a,b,inc):
	L = []
	i = a
	while i <= b:
		L += [i]
		i += inc 
		i = round(i,len(str(inc)))
		
	return L
def valeur_sin(t):
	T = []
	for i in t:
		T += [sin(i)]
	return T
def valeur_cos(t):
	T = []
	for i in t:
		T += [cos(i)]
	return T
print(intervalle(0,1,0.2))
print(valeur_sin(intervalle(-2*pi,2*pi,0.1)))
print(valeur_cos(intervalle(-2*pi,2*pi,0.1)))
valeur_sinu = valeur_sin(abscisse_trigo)


plt.plot(intervalle(-2*pi,2*pi,0.1),valeur_sin(intervalle(-2*pi,2*pi,0.1)),intervalle(-2*pi,2*pi,0.1),valeur_cos(intervalle(-2*pi,2*pi,0.1)))
plt.show()

