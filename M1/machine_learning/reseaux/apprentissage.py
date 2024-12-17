import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd
from scipy.cluster.vq import whiten

# lecture de la base de données
df = pd.read_csv("https://raw.githubusercontent.com/allisonhorst/palmerpenguins/c19a904462482430170bfe2c718775ddb7dbb885/inst/extdata/penguins.csv")
df = df.dropna() # pour supprimer les lignes avec des valeurs manquantes
#print(df.head()) # pour afficher les premières lignes

# matrice des entrées (longueur du bec, largueur du bec, longueur des nageoires, poids du corps)
entrees = df[["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]].to_numpy()


# matrice des sorties (manchot Adélie, manchot Papou, manchot à jugulaire)
sp = ["Adelie","Gentoo","Chinstrap"]
sorties = np.zeros([len(df),len(sp)])
for s in range(len(sp)) :
   sorties[:,s] = df.species==sp[s]

eta = 1/300

poids = np.array([rd.randint(-100, 100) / 100 for i in range(15)])
poids = poids.reshape(3, 5)
#print(poids)


learning_data = np.zeros([len(entrees)//2 + 1, 4])
learning_data[: 145//2 + 1] = entrees[: 145//2 + 1]
learning_data[145//2 : 264//2 + 1] = entrees[145//2 : 264//2 + 1]
#learning_data[145//2 : 264//2 + 1] = entrees[145//2 : 264//2 + 1]
learning_data[264//2 : 333//2 + 1] = entrees[264//2 : 333//2 + 1]
learning_data = entrees
test_data = np.zeros([len(entrees)//2, 4])


for i in range(len(learning_data[0])):
	learning_data[:,i] /= max(learning_data[:,i])

idx = np.arange(len(learning_data))
np.random.shuffle(idx)
learning_data = learning_data[idx,:]
print(learning_data)
test_data = learning_data[251:]
learning_data = learning_data[:250]
sorties = sorties[idx,:]


tab_test = []

tab = []
for etapes in range(200):
	erreur = 0
	erreur_test = 0

	for p in range(len(learning_data)):
		
		for j in range(len(sp)):
			value = 0
			for i in range(len(learning_data[0])):
			 
				value += poids[j][i]  * learning_data[p][i]

			if value < 0:
				value = 0
			else:
				value = 1

			erreur += (sorties[p][j] - value)**2
			for i in range(len(learning_data[0])):

				poids[j,i] += eta * (sorties[p][j] - value) * learning_data[p][i]
			
			poids[j, -1] += -(eta * (sorties[p][j] - value))



			for p in range(len(test_data)):
		
				for j in range(len(sp)):
					value_test = 0
					for i in range(len(test_data[0])):
					
						value_test += poids[j][i]  * test_data[p][i]


					if value_test < 0:
						value_test = 0
					else:
						value_test =1

					erreur_test += (sorties[p][j] - value_test)**2
			tab_test.append(erreur/len(test_data)*100)



				
	tab.append(erreur/len(learning_data)*100)
	tab_test.append(erreur/len(test_data)*100)

"""
for etapes in range(200):
	erreur = 0

	for p in range(len(test_data)):
		
		for j in range(len(sp)):
			value = 0
			for i in range(len(test_data[0])):
			 
				value += poids[j][i]  * test_data[p][i]

			if value < 0:
				value = 0
			else:
				value = 1

			erreur += (sorties[p][j] - value)**2
			
			#for i in range(len(learning_data[0])):

			#	poids[j,i] += eta * (sorties[p][j] - value) * learning_data[p][i]
			
			#poids[j, -1] += -(eta * (sorties[p][j] - value))
				
"""
#print(tab[2])
plt.plot(tab)



plt.show()

plt.plot(tab_test)
plt.show()




#print(np.where(df.species == "Gentoo"))
#print(entrees)
#print(learning_data) 