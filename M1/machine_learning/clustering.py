import soundfile as sf
import scipy.io.wavfile as wave
#import panda as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import os
import sys
import scipy.cluster.vq as vq

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
    pas = 512
    for start in range(0, len(diff)-pas, pas):
        interval = diff[start : start + pas * 2]

        auto_corr = scipy.signal.correlate(interval, interval)
        # Symétrie de l'auto-corrélation donc on prend la moitié et garder le 1/20ème après.
        resamp_auto_corr = auto_corr[len(auto_corr)//2:len(auto_corr)//2 + len(auto_corr)//20]

        z_resample = resamp_auto_corr - min(resamp_auto_corr) + 1e-100 #sys.float_info.epsilon
        p_resample = z_resample / sum(z_resample)
        H_resample = scipy.stats.entropy(p_resample) 

        #z = auto_corr - min(auto_corr) + 1e-100 #sys.float_info.epsilon
        #p = z / sum(z)
        #H = scipy.stats.entropy(p)

        #entropies.append(H)
        #matrice.append(auto_corr)

        entropies_resample.append(H_resample)
        matrice_resample.append(resamp_auto_corr)

    #np.save("matrice.txt", matrice)
    #np.save("entropies.txt", entropies)
    #np.save("matrice_resample.txt", matrice_resample)
    #np.save("entropies_resample.txt", entropies_resample)
    
    return matrice, entropies, matrice_resample, entropies_resample

matrice, entropies, matrice_resample, entropies_resample = matrice_entropies()



#matrice = np.load("matrice.txt.npy")
#entropies = np.load("entropies.txt.npy")
#matrice_resample = np.load("matrice_resample.txt.npy")
#entropies_resample = np.load("entropies_resample.txt.npy")


#matrice = np.array(matrice)
#cumsum_H = np.cumsum(entropies)

entropies = np.array(entropies_resample)
idx_faible_entropie = np.where(entropies < 4.5)
idx_forte_entropie = np.where(entropies > 4.5)

matrice = np.array(matrice_resample)
mode_1 = matrice[idx_faible_entropie]
mode_2 = matrice[idx_forte_entropie]

print("Mode 1: ", mode_1.shape)
print("Mode 2: ", mode_2.shape)


# Clustering
union = mode_1#np.stack((mode_1, mode_2))
union.reshape(-1, 2)
whitened = scipy.cluster.vq.whiten(union)
codebook,distorsion = scipy.cluster.vq.kmeans(whitened,2)
print(codebook)

plt.scatter(whitened[:,0], whitened[:,1])

plt.scatter(codebook[:,0], codebook[:,1],c='r')
plt.show()

labels, _ = scipy.cluster.vq.vq(union, codebook)


fig = plt.figure(figsize=(20, 20))
entropie_faible_plot = fig.add_subplot(221)
for i in range(10):
    entropie_faible_plot.plot(mode_1[i], 'r')
entropie_faible_plot.set_title("Entropie faible")

entropie_forte_plot = fig.add_subplot(222)
for i in range(10):
    entropie_forte_plot.plot(mode_2[i], 'b')
entropie_forte_plot.set_title("Entropie forte")


comparaison_plot = fig.add_subplot(223)
for i in range(10):
    comparaison_plot.plot(mode_1[i], 'r')
    comparaison_plot.plot(mode_2[i], 'b')

comparaison_plot.set_title("Comparaison")



hist = fig.add_subplot(224)

hist.hist(entropies_resample, 1000, color='orange')
hist.set_title("Histogramme des entropies (resample)")
hist.set_xlabel("Entropie")
hist.set_ylabel("Fréquence")


plt.savefig("signal_1sur2_resample.png")

plt.show()


