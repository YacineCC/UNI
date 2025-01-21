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

# eta arbitraire
eta = 1/300

# Initialisation des poids aléatoires, on a ici 3 neurones et 4 entrées avec un biais pour chaque neurone.
poids = np.array([rd.randint(-100, 100) / 100 for i in range(15)])
poids = poids.reshape(3, 5)





# Normalisation des données
for i in range(len(entrees[0])):
	entrees[:,i] /= max(entrees[:,i])

# Moitié des données pour l'apprentissage, l'autre moitié pour le test
# Mélange des données
idx = np.arange(len(entrees))
np.random.shuffle(idx)
entrees = entrees[idx,:]

# Affecation des listes d'apprentissage et de test on fait moitié moitié
learning_data = entrees[:len(entrees)//2]
test_data = entrees[len(entrees)//2:]

# Attention à ne pas oublier de shuffler les sorties de la même manière que les entrées
sorties = sorties[idx,:]



tab_test = []

tab = []
# Pour chaque étape
for etapes in range(200):
	erreur = 0
	erreur_test = 0

	# Pour chaque exemple d'apprentissage
	for p in range(len(learning_data)):
		
		# Pour chaque neurone j
		for j in range(len(sp)):
			value = 0
			# Calcul de la somme pondérée
			for i in range(len(learning_data[0])):
			 
				value += poids[j][i]  * learning_data[p][i]

			# Fonction d'activation
			if value < 0:
				value = 0
			else:
				value = 1

			# Calcul de l'erreur
			erreur += (sorties[p][j] - value)**2

			# Pour chaque entrée
			for i in range(len(learning_data[0])):
				# Mise à jour des poids
				poids[j,i] += eta * (sorties[p][j] - value) * learning_data[p][i]
			
			# Mise à jour du biais
			poids[j, -1] += -(eta * (sorties[p][j] - value))


	# Le méthode pour tester est identique à l'apprentissage on ne modifie juste pas les poids.
	# Pour chaque exemple de test
	for p in range(len(test_data)):
		# Pour chaque neurone j
		for j in range(len(sp)):
			value_test = 0
			# Calcul de la somme pondérée
			for i in range(len(test_data[0])):
			
				value_test += poids[j][i]  * test_data[p][i]

			# Fonction d'activation
			if value_test < 0:
				value_test = 0
			else:
				value_test =1

			# Calcul de l'erreur
			erreur_test += (sorties[p][j] - value_test)**2

			# Note : pas de mise à jour des poids ici



	# Ajout de l'erreur à la liste
	tab.append(erreur/len(learning_data)*100)
	tab_test.append(erreur/len(test_data)*100)


# Affichage des erreurs pour l'apprentissage et le test
plt.plot(tab)
plt.savefig("apprentissage.png")



plt.show()

plt.plot(tab_test)
plt.savefig("test.png")
plt.show()



