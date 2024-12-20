import soundfile as sf
import scipy.io.wavfile as wave
#import panda as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import os
import sys
import scipy.cluster.vq as vq
from sklearn.manifold import TSNE

#os.chdir(os.path.dirname(__file__))
out_images = os.path.join(os.path.dirname(__file__), "out/images")
out_data = os.path.join(os.path.dirname(__file__), "out/data")

def entropie(p):
    return -sum(p * np.log2(p))

def matrice_entropies():
    sig, r = sf.read("ONECAT_20200114_152058_174.wav")

    data = sig#[::2]
    diff = np.zeros(len(data))
    for i in range(1, len(data) - 1):
        diff[i] = data[i+1]-data[i]


    matrice = []
    entropies = []

    pas = 640
    for start in range(0, len(diff)-pas, pas):
        interval = diff[start : start + pas * 2]

        auto_corr = scipy.signal.correlate(interval, interval)
        # Symétrie de l'auto-corrélation donc on prend la moitié et garder le 1/20ème après.
        resamp_auto_corr = auto_corr[len(auto_corr)//2:len(auto_corr)//2 + len(auto_corr)//20]
        resamp_auto_corr = scipy.signal.resample(resamp_auto_corr, 10)

        z = resamp_auto_corr - min(resamp_auto_corr) + 1e-100 #sys.float_info.epsilon
        p = z / sum(z)
        #H = scipy.stats.entropy(p)
        H = entropie(p)



        entropies.append(H)
        matrice.append(p)


    np.save(os.path.join(out_data, "matrice"), matrice)
    np.save(os.path.join(out_data, "entropies"), entropies)

    
    return matrice, entropies

#matrice, entropies = matrice_entropies()



matrice = np.load(os.path.join(out_data, "matrice.npy"))
entropies = np.load(os.path.join(out_data, "entropies.npy"))
fig = plt.figure(figsize=(20, 20))

hist = fig.add_subplot(224)

hist.hist(entropies, 150, color='orange')
hist.set_title("Histogramme des entropies (resample)")
hist.set_xlabel("Entropie")
hist.set_ylabel("Fréquence")
plt.show()


entropies = np.array(entropies)
seuil = 2.4
idx_faible_entropie = np.where(entropies < seuil)
idx_forte_entropie = np.where(entropies > seuil)

matrice = np.array(matrice)
mode_1 = matrice[idx_faible_entropie]
mode_2 = matrice[idx_forte_entropie]

print("Mode 1: ", mode_1.shape)
print("Mode 2: ", mode_2.shape)


tsne = TSNE(n_components=2, random_state=0, perplexity=30, max_iter=1000)
mode_1_2d = tsne.fit_transform(mode_1)

codebook,distorsion = scipy.cluster.vq.kmeans(mode_1_2d,2)
labels, _ = scipy.cluster.vq.vq(mode_1_2d, codebook)
plt.scatter(mode_1_2d[:,0], mode_1_2d[:,1],c=labels)

plt.scatter(codebook[:,0], codebook[:,1],c='r')

plt.savefig(os.path.join(out_images, "clustering.png") )
plt.show()

plt.hist2d(mode_1_2d[:,0], mode_1_2d[:, 1])

plt.savefig(os.path.join(out_images, "heatmap.png"))
plt.show()

fig = plt.figure(figsize=(20, 20))



entropie_faible_plot = fig.add_subplot(221)
moy_1 = 0
for i in range(10):
    #entropie_faible_plot.plot(mode_1[i], 'r')
    moy_1 += mode_1[i]
moy_1 = moy_1 / 10
entropie_faible_plot.plot(moy_1, 'r')
entropie_faible_plot.set_title("Moyenne entropie faible")

entropie_forte_plot = fig.add_subplot(222)
moy_2 = 0
for i in range(10):
    #entropie_forte_plot.plot(mode_2[i], 'b')
    moy_2 += mode_2[i]
moy_2 = moy_2 / 10
entropie_forte_plot.plot(moy_2, 'b')
entropie_forte_plot.set_title("Moyenne entropie forte")


comparaison_plot = fig.add_subplot(223)
comparaison_plot.plot(moy_1, 'r')
comparaison_plot.plot(moy_2, 'b')

comparaison_plot.set_title("Comparaison des moyennes")



hist = fig.add_subplot(224)

hist.hist(entropies, 150, color='orange')
hist.set_title("Histogramme des entropies (resample)")
hist.set_xlabel("Entropie")
hist.set_ylabel("Fréquence")


plt.savefig(os.path.join(out_images, "signal_1sur2_resample.png"))

plt.show()


"""
#Partie du code Shawn Pélerin et Florian Audouard

NbCluster = 6
fig, axs = plt.subplots(NbCluster, 1, figsize=(15, 10))
for i in range(NbCluster) :
	ilab = np.where(labels == i)[0]
	#print(ilab4)
	lab = weak_entropie[ilab]
	entropielab = [entropie(l) for l in lab]
	axs[i].hist(entropielab,range=(1.3,2.1), bins=50)
plt.show()


#On garde le 2 : label 2 = couleur gris bleu
ilab2 = np.where(labels == 5)[0]
lab2d = weak_entropie_2d[ilab2]
lab2 = weak_entropie[ilab2]
plt.plot(lab2d[:,0],lab2d[:,1],'.')
plt.show()

tsne = TSNE(n_components=2, random_state=0, perplexity=30, max_iter=1000)
tsnelab2 = tsne.fit_transform(lab2)
codebook, _ = scipy.cluster.vq.kmeans(tsnelab2, 3)
labels, _ = scipy.cluster.vq.vq(tsnelab2, codebook)

plot_scatter_hist2d(
	tsnelab2,
	labels,
	codebook,
	len(weak_entropie[0]),
	f"Cluster points label 2",
)

plt.show()
"""

