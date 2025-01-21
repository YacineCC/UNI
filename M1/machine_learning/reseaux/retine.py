from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 

# Ouverture de l'image et transformation en matrice numpy.
im = Image.open("cachalot.jpeg")
m3d = np.array(im) # matrice 3D de l'image
m2d = np.sum(m3d,axis=2) # matrice 2D en niveau de gris
out = np.array([])

# Dimensions de l'image
largeur = 418
hauteur = 120

# Initialisation des matrices de sortie
image_tout = []
image_vertical = []
immage_horizontal = []

# Poids arbitraire
poids = 1
# Seuil arbitraire
seuil = max(m2d.flatten())//10

# Parcours de l'image
for i in range(1, m2d.shape[0]-1):

    # Initialisation des variables temporaires
    tmp_tout = []
    tmp_vertical = []
    tmp_horizontal = []
    
    for j in range(1, m2d.shape[1]-1):
        # Calcul de la somme des valeurs des voisins

        # Pour le contraste entier (voisins tout autour)
        voisins_tout = m2d[i][j+1] + m2d[i][j-1] + m2d[i+1][j+1] + m2d[i+1][j-1] + m2d[i-1][j+1] + m2d[i-1][j-1] + m2d[i+1][j] + m2d[i-1][j]

        # Pour détecter les lignes verticales (voisins d'en haut et d'en bas)
        voisins_vertical = m2d[i][j+1] + m2d[i][j-1]

        # Pour détecter les lignes horizontales (voisins de gauche et de droite)
        voisins_horizontal =  m2d[i+1][j] + m2d[i-1][j]

        # Calcul des valeurs de sortie pour chaque type de contrastes
        val_tout = (m2d[i][j] - (poids * voisins_tout / 8)) # Moyenne des voisins
        val_vertical = (m2d[i][j] - (poids * voisins_vertical / 2))
        val_horizontal = (m2d[i][j] - (poids * voisins_horizontal / 2))

        # Fonction d'activation.
        if val_tout > (seuil):
            tmp_tout.append(255)
        else:
            tmp_tout.append(0)

        if val_vertical > (seuil):
            tmp_vertical.append(255)
        else:
            tmp_vertical.append(0)

        if val_horizontal > (seuil):
            tmp_horizontal.append(255)
        else:
            tmp_horizontal.append(0)
    
    # Ajout des lignes dans les matrices de sortie
    image_tout.append(tmp_tout)
    image_vertical.append(tmp_vertical)
    immage_horizontal.append(tmp_horizontal)



# Affichage des images
plt.subplot(4,1,1)
plt.imshow(m3d)

plt.subplot(4,1,2)
plt.savefig("contraste.jpeg")
plt.imshow(image_tout, cmap="gray")

plt.subplot(4,1,3)
plt.savefig("vertical.jpeg")
plt.imshow(image_vertical, cmap="gray")

plt.subplot(4,1,4)
plt.imshow(immage_horizontal, cmap="gray")
plt.savefig("horizontal.jpeg")
plt.show()
