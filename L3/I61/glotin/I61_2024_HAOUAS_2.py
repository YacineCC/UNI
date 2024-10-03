import numpy as np
import math
import pandas as pd 
import matplotlib.pyplot as plt
from PIL import Image
CONST = 0.45

def get_rdm_hline(seuil=CONST):
    res = np.zeros((8, 8), dtype=int)
    for row in range(3,5):
        for col in range(8):
            res[row, col] = np.random.rand() > seuil

    return res

def get_rdm_vline(seuil=CONST):
    
    return get_rdm_hline(seuil).transpose()


def get_rdm_o1line(seuil=CONST):
    res = np.zeros((8, 8), dtype=int)

    res[0, 0] = np.random.rand() > seuil
    for diag in range(7):
        res[diag + 1, diag] = np.random.rand() > seuil
        res[diag, diag + 1] = np.random.rand() > seuil
        res[diag + 1, diag + 1] = np.random.rand() > seuil
    return res


def get_rdm_o2line(seuil=CONST):
    res = np.zeros((8, 8), dtype=int)

    res[7, 0] = np.random.rand() > seuil
    for diag in range(7):
        res[7 - diag - 1, diag] = np.random.rand() > seuil
        res[7 - diag, diag + 1] = np.random.rand() > seuil
        res[7 - diag - 1, diag + 1] = np.random.rand() > seuil
    return res



def get_rdm_centre(seuil=CONST):
    res = np.zeros((8, 8), dtype=int)
    liste = [[3, 3], [4, 3], [3, 4], [4, 4]]
    for centre in liste:
        res[centre[0], centre[1]] = np.random.rand() > seuil
  
    return res


def get_rdm_corner(seuil=CONST):
    res = np.zeros((8, 8), dtype=int)
    liste = [[0, 0], [1, 0], [0, 1], [1, 1], [7, 0], [6, 0], [7, 1], [6, 1], [0, 6], [1, 6], [0, 7], [1, 7], [7, 6], [6, 6], [7, 7], [6, 7]]
    for corner in liste:
        
        res[corner[0], corner[1]] = np.random.rand() >= seuil
    
    return res


def entropie(PX):
    res = 0
    for x in PX:
        if x > 0:
            res -= x * math.log2(x)
    return res

def infomut(PXY):
    ePXY = entropie(PXY.np.flatten())
    PX = np.sum(PXY, 0)
    PY = np.sum(PXY, 1)
    ePX = entropie(PX)
    ePY = entropie(PY)
    return ePXY - ePX - ePY

def dkl(B, C):
    res = 0
    for i in range(len(B)):
        if B[i] > 0 and C[i] > 0:
            res -= B[i] * math.log2(B[i]/C[i])
    return res

def H_croise(B, C):
    res = 0
    for i in range(len(B)):
        if B[i] > 0 and C[i] > 0:
            res -= B[i] * math.log2(C[i])
    return res


def gen_hline():

    data = []
    for i in range(100):
        data.append(get_rdm_hline())
    #np.savetxt("hline.csv", data, fmt='%d', delimiter=',')
    DF = pd.DataFrame(data)
    DF.to_csv("hline.csv")
    return data
        
def gen_vline():

    data = []
    for i in range(100):
        data.append(get_rdm_vline())
    np.savetxt("vline.csv", data, fmt='%d', delimiter=',')
    return data

def gen_o1line():

    data = []
    for i in range(100):
        data.append(get_rdm_o1line())
    np.savetxt("o1line.csv", data, fmt='%d', delimiter=',')

    return data


def gen_o2line():

    data = []
    for i in range(100):
        data.append(get_rdm_o2line())
    np.savetxt("o2line.csv", data, fmt='%d', delimiter=',')
    return data

def gen_centre():

    data = []
    for i in range(100):
        data.append(get_rdm_centre())
    np.savetxt("centre.csv", data, fmt='%d', delimiter=',')

    return data

def gen_corner():

    data = []
    for i in range(100):
        data.append(get_rdm_corner())
    np.savetxt("corner.csv", data, fmt='%d', delimiter=',')

    return data


def lire(filename):
    np.loadtxt(filename, delimiter=',')

        

def moyenne(LM): #liste de matrices

    res = np.zeros((8,8 ), dtype=float)

    for x in LM:
        res += x
    
    res = res / len(LM)
    return res

def moyenne_all():
    liste_moyennes = [moyenne(gen_hline()), moyenne(gen_vline()),
                      moyenne(gen_o1line()), moyenne(gen_o2line()),
                      moyenne(gen_centre()), moyenne(gen_corner())]

    return liste_moyennes

def normalise(M):

    return M.flatten()/M.sum()

def normalise_all():
    lm = moyenne_all()
    liste_norma = []
    for m in lm:
        liste_norma.append(normalise(m))
    return liste_norma


def H_croise_all():

    ln = normalise_all()

    res = np.zeros((6, 6), dtype=float)
    for i in range(len(ln)):
        for j in range(len(ln)):
            res[i, j] = (H_croise(ln[i], ln[j]))
    
    plt.imshow(res)
    plt.show() #pour afficher les images
    plt.savefig('matrice_des_H_croise.png')
    return res


print(H_croise_all())

