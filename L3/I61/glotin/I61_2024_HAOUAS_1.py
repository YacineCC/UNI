import numpy as np
import math
import pickle
import matplotlib.pyplot as plt
from PIL import Image
SEUIL = 0.35
EPSILON = 0.00001
TIRAGES = 10000
CLASSES = {'Coins' : 0, 'AntiDiagonale' : 1, 'Diagonale' : 2,
            'Centre' : 3, 'Verticale' : 4, 'Horizontale': 5}


def get_rdm_hline(seuil=SEUIL):
    res = np.zeros((8, 8), dtype=int)
    res = res + EPSILON
    for row in range(3,5):
        for col in range(8):
            if np.random.rand() > seuil:
                res[row, col] = 1

    return res

def get_rdm_vline(seuil=SEUIL):
    
    return get_rdm_hline(seuil).transpose()


def get_rdm_o1line(seuil=SEUIL):
    res = np.zeros((8, 8), dtype=int)
    res = res + EPSILON

    res[0, 0] = np.random.rand() > seuil
    for diag in range(7):
        res[diag + 1, diag] = np.random.rand() > seuil
        res[diag, diag + 1] = np.random.rand() > seuil
        res[diag + 1, diag + 1] = np.random.rand() > seuil
    return res


def get_rdm_o2line(seuil=SEUIL):
    res = np.zeros((8, 8), dtype=int)
    res = res + EPSILON

    res[7, 0] = np.random.rand() > seuil
    for diag in range(7):
        res[7 - diag - 1, diag] = np.random.rand() > seuil
        res[7 - diag, diag + 1] = np.random.rand() > seuil
        res[7 - diag - 1, diag + 1] = np.random.rand() > seuil
    return res



def get_rdm_centre(seuil=SEUIL):
    res = np.zeros((8, 8), dtype=int)
    res = res + EPSILON
    liste = [[3, 3], [4, 3], [3, 4], [4, 4]]
    for centre in liste:
        res[centre[0], centre[1]] = np.random.rand() > seuil
  
    return res


def get_rdm_corner(seuil=SEUIL):
    res = np.zeros((8, 8), dtype=int)
    res = res + EPSILON
    liste = [[0, 0], [1, 0], [0, 1], [1, 1], [7, 0], [6, 0], [7, 1], [6, 1], [0, 6], [1, 6], [0, 7], [1, 7], [7, 6], [6, 6], [7, 7], [6, 7]]
    for corner in liste:
        
        res[corner[0], corner[1]] = np.random.rand() >= seuil
    
    return res





def entropie(PX):
    res = 0
    PX = PX.flatten()
    for x in PX:
        
        res -= x * math.log2(x)
    return res

def infomut(PXY):
    ePXY = entropie(PXY.np.flatten())
    PX = np.sum(PXY, 0)
    PY = np.sum(PXY, 1)
    ePX = entropie(PX)
    ePY = entropie(PY)
    return ePXY - ePX - ePY

# def dkl(B, C):
#     res = 0
#     for i in range(len(B)):
       
#         res -= B[i] * math.log2(B[i]/C[i])
#     return res



def H_croise(B, C):
    res = 0
    C = C.flatten()
    B = B.flatten()
    for i in range(len(B)):
        
        res -= B[i] * math.log2(C[i])
    return res

def dkl(p, q):

    return H_croise(p, q) - entropie(p)

def gen_hline():
    filename = "hlines.txt"
    file = open(filename, 'wb')
    data = []
    for i in range(TIRAGES):
        data.append(get_rdm_hline())
    pickle.dump(data, file)

    file.close()

    return data
        
def gen_vline():
    filename = "vlines.txt"
    file = open(filename, 'wb')
    data = []
    for i in range(TIRAGES):
        data.append(get_rdm_vline())
    pickle.dump(data, file)

    file.close()
    return data

def gen_o1line():
    filename = "o1lines.txt"
    file = open(filename, 'wb')
    data = []
    for i in range(TIRAGES):
        data.append(get_rdm_o1line())
    pickle.dump(data, file)

    file.close()
    return data


def gen_o2line():
    filename = "o2lines.txt"
    file = open(filename, 'wb')
    data = []
    for i in range(TIRAGES):
        data.append(get_rdm_o2line())
    pickle.dump(data, file)
    file.close()
    return data

def gen_centre():
    filename = "centre.txt"
    file = open(filename, 'wb')
    data = []
    for i in range(TIRAGES):
        data.append(get_rdm_centre())
    pickle.dump(data, file)
    file.close()
    return data

def gen_corner():
    filename = "corner.txt"
    file = open(filename, 'wb')
    data = []
    for i in range(TIRAGES):
        data.append(get_rdm_corner())
    pickle.dump(data, file)
    file.close()
    return data


def lire(filename):
    file = open(filename, 'rb')
    test = pickle.load(file)
    for x in test : 
        print(x)
        

def moyenne(LM): # Retourne la moyenne d'apparition des pixels

    res = np.full((8, 8), EPSILON,dtype=float)

    for x in LM:
        res += x
    
    res = res / len(LM)
    return res

def moyenne_all(): # Retourne un tableau avec les moyennes pour chaque
                # classe toujours dans
                # l'odre habituel [coins, antidiag, diag, centre, verticale, horizontale]
    liste_moyennes = [moyenne(gen_corner()), moyenne(gen_o2line()),
                      moyenne(gen_o1line()), moyenne(gen_centre()),
                      moyenne(gen_vline()), moyenne(gen_hline())]

    return liste_moyennes

def normalise(M):

    return M/M.sum()

def normalise_all():    # Retourne la pdf des 6 classes
    lm = moyenne_all()
    liste_norma = []
    for m in lm:
        liste_norma.append(normalise(m))
    return liste_norma


def H_croise_all(): # Retourne la matrice des entropies croisées par couples de classes.

    ln = normalise_all()

    res = np.zeros((6, 6),dtype=float)
    for i in range(len(ln)):
        for j in range(len(ln)):
            res[i, j] = ((H_croise(ln[i], ln[j])+ H_croise(ln[j], ln[i]))/2)
    
    fig, ax = plt.subplots()

    pos = ax.matshow(res)
    
    ax.set_xticks(range(len(res)))
    ax.set_yticks(range(len(res)))
    ax.set_xticklabels(["Coins", "AntiDiagonale", "Diagonale", "Centre", "Verticale", "Horizontale"])
    ax.set_yticklabels(["Coins", "AntiDiagonale", "Diagonale", "Centre", "Verticale", "Horizontale"])
    fig.colorbar(pos, ax=ax)


    plt.savefig('matrice_des_H_croise.png')
    plt.show() #pour afficher les images
    

    return res


# Dictionnaire de fonctions (toujours dans l'odre habituel) pour faciliter l'implementation dans le code.
FCLASSES = {0 : gen_corner, 1 : gen_o2line, 2 : gen_o1line,
            3 : gen_centre, 4 : gen_vline, 5: gen_hline} 


# Retourne si le notre système trouve bien l'appartenance d'une image à sa classe.
def arg(T, forme_img, pdf): 
    T = T + EPSILON
    T = normalise(T)
    
    res = []
    for i in pdf:
        res.append((H_croise(T, i) + H_croise(i, T)))
    if min(res) == res[forme_img]: #ARGMIN
         return True
    else:
         return False

def bruitage(M, db): # Prend une image et la retourne bruitée.
    n = 64/(10**(db/10))
    L = np.arange(0, 64, 1, dtype=int)
    np.random.shuffle(L)
    
    for i in range(int(n)):
        
        if M[L[i]//8,L[i]%8] > EPSILON:
            M[L[i]//8,L[i]%8] = EPSILON

        elif M[L[i]//8,L[i]%8] == EPSILON:
             M[L[i]//8,L[i]%8] = 1
    return M


def bruitage_32px(M, db, top_px): # La version avec seulement les 32 pixels les plus pertinents.

    n = 64/(10**(db/10))
    L = np.arange(0, 64, 1, dtype=int)
    np.random.shuffle(L)
    
    for i in range(int(n)):
        if  (L[i]//8,L[i]%8) in top_px:
            if M[L[i]//8,L[i]%8] > EPSILON:
                M[L[i]//8,L[i]%8] = EPSILON

            elif M[L[i]//8,L[i]%8] == EPSILON:
                M[L[i]//8,L[i]%8] = 1
    return M     




def courbe(classe : int, pdf): # Donne l'image (l'accuracy) pour chaque x, 



    x = [0, 1, 2, 3, 4, 5, 6, 8, 16, '+inf']
    y = []
    
    for db in x: 
        data = FCLASSES[classe]()
        score = 0
        for d in data :    
            test = d
            if db != '+inf':
                test = bruitage(d, db)
            if arg(test, classe, pdf):
                score += 1
        y += [(score/TIRAGES)*100]
    return y


def courbe_32px(classe: int, pdf, tp): # La version avec seulement les 32 pixels les plus pertinents.


    x = [0, 1, 2, 3, 4, 5, 6, 8, 16, '+inf']
    y = []
    
    for db in x: 
        data = FCLASSES[classe]()
        score = 0
        for d in data :    
            test = d
            if db != '+inf':
                test = bruitage_32px(d, db, tp)
            if arg(test, classe, pdf):
                score += 1
        y += [(score/TIRAGES)*100]
    return y


def dessine_courbe(): # Dessine les courbes avec matplotlib.
    x = [0, 1, 2, 3, 4, 5, 6, 8, 16, '+inf']
    xticks = ['0', '1', '2', '3', '4', '5', '6', '8', '16', '+inf']

    y = []
    pdf = normalise_all()
    fig, ax = plt.subplots()
    for c in CLASSES:
        y = courbe(CLASSES[c], pdf)
        print(c)
        print(y)
        
        ax.plot(x, y, label=c)

    

    #plt.xlim([0, 17])
    plt.ylim([0, 100+1])
    plt.xticks(xticks)
    plt.yticks(np.arange(0, 100+1, 20))

    plt.ylabel('% Accuracy')
    plt.xlabel('DB (RSB)')
    
    plt.legend()
    plt.savefig('Courbe_Scores.png')

    plt.show()

def dessine_courbe_32px(): # La version avec seulement les 32 pixels les plus pertinents.
    x = [0, 1, 2, 3, 4, 5, 6, 8, 16, '+inf']
    xticks = ['0', '1', '2', '3', '4', '5', '6', '8', '16', '+inf']

    y = []
    pdf = normalise_all()
    tp = get_top_pixels_indices(Matrice_DKL())
    fig, ax = plt.subplots()
    for c in CLASSES:
        y = courbe_32px(CLASSES[c], pdf, tp)
        print(c)
        print(y)
        
        ax.plot(x, y, label=c)

    

    #plt.xlim([0, 17])
    plt.ylim([0, 100+1])
    plt.xticks(xticks)
    plt.yticks(np.arange(0, 100+1, 20))

    plt.ylabel('% Accuracy')
    plt.xlabel('DB (RSB)')
    
    plt.legend()
    plt.savefig('Courbe_Scores.png')

    plt.show()




def Matrice_DKL(): # Retourne la matrice des moyennes des divergences de Kullback-Leibler
    ln = normalise_all()

    res = np.zeros((8, 8),dtype=float)
    for px_i in range(8):
        for px_j in range(8):
            som = 0
            for classe_A in range(6):
                
                for classe_B in range(6):
                    pjA = ln[classe_A][px_i][px_j] # Probabilité dans la classe A du pixel [i,j]
                    pjB = ln[classe_B][px_i][px_j] # Probabilité dans la classe B du pixel [i,j]
                    som += pjA * math.log2(pjA / pjB) + (1 - pjA) * math.log2((1 - pjA) / (1 - pjB))
                    #som += dkl(Aj, Bj)
            moy = som / 36
            #res[i, j] = dkl(ln[i], ln[j])
            res[px_i, px_j] = moy
    fig, ax = plt.subplots()

    return res


def get_top_pixels_indices(DIV): # Avoir les indices des 32 pixels pertinents.
    # Convertir la matrice DIV en une liste de tuples (valeur, (i, j))
    indices = [(i, j) for i in range(8) for j in range(8)]

    # Trier les indices par valeur en ordre décroissant
    sorted_indices = sorted(indices, key=lambda x: DIV[x[0], x[1]], reverse=True)

    # Récupérer les indices des 32 pixels avec les plus grandes valeurs
    top_pixels_indices = sorted_indices[:32]

    return top_pixels_indices





def adjust_matrix(matrix, top_pixels_indices):
    # Créer une copie de la matrice originale pour éviter les modifications non désirées
    adjusted_matrix = matrix.copy()

    # Parcourir les indices des 32 pixels avec les plus grandes valeurs
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Vérifier si l'indice (i, j) est dans top_pixels_indices
            if (i, j) not in top_pixels_indices:
                # Si l'indice n'est pas dans top_pixels_indices, supprimer la valeur du pixel
                adjusted_matrix[i, j] = 1
            

    return adjusted_matrix

DIV = Matrice_DKL()
TP = get_top_pixels_indices(DIV)
top_pixels_indices = get_top_pixels_indices(DIV)
plt.matshow(DIV)#adjust_matrix(DIV, TP))
plt.colorbar()
plt.show()

dessine_courbe_32px()
dessine_courbe()
