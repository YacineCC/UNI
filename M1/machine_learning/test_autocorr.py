import soundfile as sf
import scipy.io.wavfile as wave
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import os
import sys


sig, r = sf.read("ONECAT_20200114_152058_174.wav")

indice1 = r * 56
indice2 = r * 57
data1 = sig[indice1:indice2]


diff = np.zeros(len(data1))
for i in range(1, len(data1) - 1):
    diff[i] = data1[i+1]-data1[i]

peak = np.argmax(diff)
peak_vector_1 = diff[peak-500:peak+500]
TK_corr_1 = scipy.signal.correlate(peak_vector_1, peak_vector_1)
peak_vector_2 = diff[peak-200:peak+200]
TK_corr_2 = scipy.signal.correlate(peak_vector_2, peak_vector_2)
corr_2_resample = scipy.signal.resample(TK_corr_2, len(TK_corr_2)//10)
TK_corr = scipy.signal.correlate(diff, diff)

fig = plt.figure(figsize=(20, 20))
ax1 = fig.add_subplot(321)
ax1.set_title("Signal")
ax1.plot(data1)

ax2 = fig.add_subplot(322)
ax2.plot(diff*5000)
ax2.set_title("Diff (x5000) seconde 56 à 57")

ax3 = fig.add_subplot(323)
ax3.plot(TK_corr_1)
ax3.set_title("Auto_Correlation décalage +-500 seconde 56 à 57")

ax4 = fig.add_subplot(324)
ax4.plot(TK_corr_2)
ax4.set_title("Auto_Correlation décalage +-200 seconde 56 à 57")

ax5 = fig.add_subplot(325)
ax5.plot(corr_2_resample)
ax5.set_title("Auto_Correlation décalage +-200 resample seconde 56 à 57")

ax6 = fig.add_subplot(326)
ax6.plot(TK_corr)
ax6.set_title("Auto_Correlation sur tout le signal")

plt.savefig("ex_autocorr")

plt.show()