import soundfile as sf
import scipy.io.wavfile as wave
#import panda as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import os

#os.chdir(os.path.dirname(__file__)))

sig, r = sf.read("ONECAT_20200114_152058_174.wav")

indice1 = r * 56
indice2 = r * 57
data1 = sig[indice1:indice2]



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

