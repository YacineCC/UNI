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

os.chdir(os.path.dirname(__file__))

def matrice_entropies():
    sig, r = sf.read("ONECAT_20200114_152058_174.wav")

    data = sig[::2]
    #diff = np.diff(data)
    diff = np.zeros(len(data))
    for i in range(1, len(data) - 1):
        diff[i] = data[i+1]-data[i]


    matrice = []
    matrice_resample = []
    entropies = []
    entropies_resample = []
    e_faible = []
    pas = 640
    for start in range(0, len(diff)-pas, pas):
        interval = diff[start : start + pas * 2]

        auto_corr = scipy.signal.correlate(interval, interval)
        # Symétrie de l'auto-corrélation donc on prend la moitié et garder le 1/20ème après.
        resamp_auto_corr = auto_corr[len(auto_corr)//2:len(auto_corr)//2 + len(auto_corr)//20]
        resamp_auto_corr = scipy.signal.resample(resamp_auto_corr, 10)

        z_resample = resamp_auto_corr - min(resamp_auto_corr) + 1e-100 #sys.float_info.epsilon
        p_resample = z_resample / sum(z_resample)
        H_resample = scipy.stats.entropy(p_resample) 

        #z = auto_corr - min(auto_corr) + 1e-100 #sys.float_info.epsilon
        #p = z / sum(z)
        #H = scipy.stats.entropy(p)

        #entropies.append(H)
        #matrice.append(p)

        entropies_resample.append(H_resample)
        
        #matrice_resample.append(resamp_auto_corr)
        matrice_resample.append(p_resample)


    np.save("matrice.txt", matrice)
    np.save("entropies.txt", entropies)
    np.save("matrice_resample.txt", matrice_resample)
    np.save("entropies_resample.txt", entropies_resample)
    np.save("e_faible.txt", e_faible)
    
    return matrice, entropies, matrice_resample, entropies_resample, e_faible

#matrice, entropies, matrice_resample, entropies_resample, e_faible = matrice_entropies()



#matrice = np.load("matrice.txt.npy")
#entropies = np.load("entropies.txt.npy")

matrice_resample = np.load("matrice_resample.txt.npy")
entropies_resample = np.load("entropies_resample.txt.npy")


#matrice = np.array(matrice)
#cumsum_H = np.cumsum(entropies)

entropies = np.array(entropies_resample)
idx_faible_entropie = np.where(entropies < 1.6)
idx_forte_entropie = np.where(entropies > 1.6)

matrice = np.array(matrice_resample)
mode_1 = matrice[idx_faible_entropie]
mode_2 = matrice[idx_forte_entropie]

print("Mode 1: ", mode_1.shape)
print("Mode 2: ", mode_2.shape)


# Clustering
#union = np.vstack((mode_1, mode_2))
#union.reshape(-1, 2)
#union = e_faible

tsne = TSNE(n_components=2, random_state=0, perplexity=30, max_iter=1000)
mode_1_2d = tsne.fit_transform(mode_1)

codebook,distorsion = scipy.cluster.vq.kmeans(mode_1_2d,2)
#print(codebook)
labels, _ = scipy.cluster.vq.vq(mode_1_2d, codebook)
plt.scatter(mode_1_2d[:,0], mode_1_2d[:,1],c=labels)

plt.scatter(codebook[:,0], codebook[:,1],c='r')

plt.savefig("clustering.png")
plt.show()

plt.hist2d(mode_1_2d[:,0], mode_1_2d[:, 1])
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

hist.hist(entropies_resample, 200, color='orange')
hist.set_title("Histogramme des entropies (resample)")
hist.set_xlabel("Entropie")
hist.set_ylabel("Fréquence")


plt.savefig("signal_1sur2_resample.png")

plt.show()


