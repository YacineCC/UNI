from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 

im = Image.open("cachalot.jpeg")
m3d = np.array(im) # matrice 3D de l'image
m2d = np.sum(m3d,axis=2) # matrice 2D en niveau de gris

out = np.array([])
#m2d = m2d.flatten()

largeur = 418
hauteur = 120
image_tout = []
image_vertical = []
immage_horizontal = []
poids = 1
seuil = max(m2d.flatten())//10
for i in range(1, m2d.shape[0]-1):
    tmp_tout = []
    tmp_vertical = []
    tmp_horizontal = []
    
    for j in range(1, m2d.shape[1]-1):
        voisins_tout = m2d[i][j+1] + m2d[i][j-1] + m2d[i+1][j+1] + m2d[i+1][j-1] + m2d[i-1][j+1] + m2d[i-1][j-1] + m2d[i+1][j] + m2d[i-1][j]
        voisins_vertical = m2d[i][j+1] + m2d[i][j-1]
        voisins_horizontal =  m2d[i+1][j] + m2d[i-1][j]

        val_tout = (m2d[i][j] - (poids * voisins_tout / 8))
        val_vertical = (m2d[i][j] - (poids * voisins_vertical / 2))
        val_horizontal = (m2d[i][j] - (poids * voisins_horizontal / 2))
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
        
    image_tout.append(tmp_tout)
    image_vertical.append(tmp_vertical)
    immage_horizontal.append(tmp_horizontal)


#m2d = m2d.reshape(120, 418)
plt.subplot(4,1,1)
plt.imshow(m3d)
plt.subplot(4,1,2)
plt.imshow(image_tout, cmap="gray")
plt.subplot(4,1,3)
plt.imshow(image_vertical, cmap="gray")
plt.subplot(4,1,4)
plt.imshow(immage_horizontal, cmap="gray")
plt.show()
