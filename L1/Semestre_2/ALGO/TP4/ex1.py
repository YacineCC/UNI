import matplotlib.pyplot as plt
import random as rd
abscisse = []
for i in range(50,551,50):
	abscisse += [i]

carre = []
for i in range(len(abscisse)):
	carre += [abscisse[i]**2]

cube = []
for i in range(len(abscisse)):
	cube += [abscisse[i]**3]

"""courbe_carre, = plt.plot(abscisse, carre, label='x^2')
courbe_cube, = plt.plot(abscisse, cube, label='x^3')
plt.legend(handles=[courbe_carre, courbe_cube])
plt.show()"""

def rand_table(n,a,b):
	T = []
	for i in range(n):
		T += [rd.randrange(a,b+1)]
	return T
print(rand_table(5,1,3))

def swap(T,a,b):
	tp = T[a]
	T[a] = T[b]
	T[b] = tp
	return T
def tri_insertion(T):
	comp = 0
	i = 1 
	while i <= len(T):
		j = 1
		comp += 1
		while j < len(T) and T[j] < T[j-1]:
			
			swap(T,j,j-1)
			comp += 1
			j += 1
		i += 1 
		
	
	return T,comp
print(tri_insertion(rand_table(9,1,9)))

def tri_bulle(T):
	comp = 0
	i = 0
	while i <= len(T):
		j = 0
		comp += 1
		while j < len(T)-1:
			if T[j] > T[j+1]:
				swap(T,j,j+1)
				comp += 1
			j += 1
		i += 1
	return T,comp
print(tri_bulle(rand_table(9,1,9)))

def mini(T,debut):
	mini = debut
	for i in range(debut,len(T)):
		if T[i] < T[mini]:
			mini = i
	return mini

def tri_selection(T):
	comp = 0
	i = 0
	while i < len(T):
		mun = mini(T,i)
		comp += len(T) - i
		swap(T,i,mun)
		i += 1
	return T,comp
print(tri_selection(rand_table(9,1,9)))
			

def compare_tris(T):
	t = tuple()
	t += (tri_insertion(T)[1],tri_bulle(T)[1],tri_selection(T)[1])
	return t
	
T = rand_table(50,1,50)


def moy():
	tab = []
	for j in range(50,551,50):
		som = 0
		moyI = 0
		moyB = 0
		moyS = 0
		for i in range(100):
		
			tp = compare_tris(rand_table(j,1,j))
			moyI += tp[0]
			moyB += tp[1]
			moyS += tp[2]
		tab += [[moyI/100, moyB/100, moyS/100]]

	return tab

print(moy())
ordo = moy()
moyI,moyB,moyS = [],[],[]
for y in ordo:
	moyI.append(y[0])
	moyB.append(y[1])
	moyS.append(y[2])
	

courbe_insertion, = plt.plot(abscisse, moyI, label='insertion')
courbe_bulle, = plt.plot(abscisse, moyB, label='bulle')
courbe_selection, = plt.plot(abscisse, moyS, label='selection')
plt.legend(handles=[courbe_insertion, courbe_bulle, courbe_selection])
plt.show()
	
