import soundfile as sf
import scipy.io.wavfile as wave
#import panda as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import os
import sys

#os.chdir(os.path.dirname(__file__)))

sig, r = sf.read("ONECAT_20200114_152058_174.wav")

indice1 = r * 56
indice2 = r * 57
data1 = sig[indice1:indice2]
data_tout = sig



tk = []
diff = np.zeros(len(data1))
for i in range(1, len(data1) - 1):
    diff[i] = data1[i+1]-data1[i]

peak = np.argmax(diff)
peak_vector_1 = diff[peak-500:peak+500]
TK_corr_1 = scipy.signal.correlate(peak_vector_1, peak_vector_1)
peak_vector_2 = diff[peak-200:peak+200]
TK_corr_2 = scipy.signal.correlate(peak_vector_2, peak_vector_2)
corr_2_resample = scipy.signal.resample(TK_corr_2, len(TK_corr_2)//10)
#TK_corr = scipy.signal.correlate(diff, diff)




diff_tout = np.zeros(len(data_tout))
for i in range(1, len(data_tout) - 1):
    diff_tout[i] = data_tout[i+1]-data_tout[i]

matrice = []
entropies = []
for start in range(0, len(diff_tout), 512):
    interval = diff_tout[start : start + 1024]
    auto_corr = scipy.signal.correlate(interval, interval)
    auto_corr = auto_corr[len(auto_corr)//2:len(auto_corr)//2 + len(auto_corr)//20]
    #auto_corr = auto_corr[0 : len(interval)//2]
    resamp_auto_corr = auto_corr #scipy.signal.resample(auto_corr, 32)
    z = np.array(resamp_auto_corr) - min(resamp_auto_corr) + 1e-100#sys.float_info.epsilon
    p = z / sum(z)
    H = scipy.stats.entropy(p) 
    entropies.append(H)
    matrice.append(resamp_auto_corr)

#np.savetxt("matrice.txt", matrice)
#cumsum_H = np.cumsum(entropies)

entropies = np.array(entropies)
idx_mode_1 = np.where(entropies < 4.42)
idx_mode_2 = np.where(entropies > 4.42)
matrice = np.array(matrice)
mode_1 = matrice[idx_mode_1[:10]]
mode_2 = matrice[idx_mode_2[:10]]



#mode_1 = sum(mode_1) // len(mode_1)
#mode_2 = sum(mode_2) // len(mode_2)
plt.plot(mode_1)
plt.plot(mode_2)



plt.hist(entropies, 1000)#int(len(entropies) ** 0.5))
#histo = scipy.ndimage.histogram(entropies, np.min(entropies), np.max(entropies), int(len(entropies) ** 0.5))
#histo = plt.hist()
#plt.plot(histo)
#print(histo)
#print(entropies)
#matrice = np.array(matrice)
#print(matrice.shape)
fig = plt.figure(figsize=(20, 5))
ax1 = fig.add_subplot(221)
ax1.plot(data1)
ax2 = fig.add_subplot(222)
ax2.plot(diff*5000)
#ax3 = fig.add_subplot(223)
#ax3.plot(TK_corr_1)
ax4 = fig.add_subplot(223)
ax4.plot(TK_corr_2)
ax5 = fig.add_subplot(224)
ax5.plot(corr_2_resample)


plt.show()

