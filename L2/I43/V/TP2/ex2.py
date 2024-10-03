def egcd(a,n):
    x = n
    u = 1
    v = 0

    u1 = 0
    v1 = 1

    while n > 0:

        q = a // n
        a,n = n,a % n

        u,u1 = u1, u - (q*u1)
        v,v1 = v1, v - (q*v1)


    return [a,u,v]

def enumere_keys(n):
    res = []
    i = 2
    while(i < n):
        
        test = egcd(i,n)
        # On regarde si i et n sont premiers entre eux pour tous les i
        if(test[0] == 1):
            #creation de toutes les clefs possibles
            for j in range(n):
                res += [[i,j,n]]

        i += 1
    return res

#fonction qui "lisse" la chaine de caracteres, càd qui y enleve la ponctuation, les accents et met toutes les lettres en minuscule
def lisse(texte):
    
    dico = {}
    dico["é"] = "e"
    dico["è"] = "e"
    dico["ê"] = "e"
    dico["ë"] = "e"
    dico["à"] = "a"
    dico["â"] = "a"
    dico["ä"] = "a"
    dico["ô"] = "o"
    dico["ö"] = "o"
    dico["ï"] = "i"
    dico["î"] = "i"
    dico["ç"] = "c"
    dico["!"] = ""
    dico["."] = ""
    dico["?"] = ""
    dico[","] = ""
    dico[";"] = ""
    dico[":"] = ""
    dico[" "] = ""
    dico["'"] = ""
    dico["\n"] = ""

    texte = texte.lower()
    texte_final = ""
    i = 0
    while(i < len(texte)):
        #si la lettre fait parti du dictionnaire on la remplace
        if(texte[i] in dico.keys()):
            texte_final += dico[texte[i]]
        #sinon on ne fait rien
        else:
            texte_final += texte[i]

        i += 1
    return texte_final

def dechiffre(cryptogramme,k,n):
    #k[2] contient l'inverse modulo n de k[0]

    clair = ""
    #creation des deux dictionnaires l'un associant des nombres à des lettres et l'autre des lettres à des nombres
    #cette methode est necessaire lorsque l'alphabet contient des caracteres spéciaux
    dico = {}
    for z in range(ord('a'),ord('z')+1):
        dico[chr(z)] = z - 97

    doci = {}
    for j in range(ord('a'),ord('z')+1):
        doci[j - 97] =  chr(j)
    #quand l'alphabet contient des caracteres spéciaux il faut les inclure dans le dictionnaire   
    """
    dico[','] = 26
    dico["'"] = 27
    dico['.'] = 28
    doci[26] = ','
    doci[27] = "'"
    doci[28] = '.'
    """
    i = 0
    while(i < len(cryptogramme)):

        if(cryptogramme[i] != " "):
            #on applique la transformation de dechiffrement
            test = ((dico[cryptogramme[i]] - k[1]) * k[2]) % n
            clair += doci[test] 

        i += 1
    return clair


def resolution_affine(bigramme):
                
    dico = {}   
                
    for i in range(ord('a'), ord('z') + 1): 
        dico[chr(i)] = i - 97
                
                
    dico[' '] = 26
    dico['\''] = 27
    dico['.'] = 28
    
    #implementation python de la résolution du systeme d'equation
    #on soustrait la premiere ligne a la deuxieme pour isole mu puis on multiplie par l'inverse modulaire
    u = ((dico[bigramme[1]] - dico[bigramme[0]])*egcd(14,29)[1])%29
    #il n'y a plus qu'a finir l'equation
    v = (dico[bigramme[0]] - 4*u) % 29
    return [u,v]

def analyse_freq(cryptogramme):
    cryptogramme1 = lisse(cryptogramme)
    #initialisation d'un dictionnaire ou 0 est associe a toutes les lettres de notre alphabet 
    freq = {}
    for i in range(ord('a'),ord('z')+1):
        freq[chr(i)] = 0
    freq[','] = 0
    freq["'"] = 0
    freq['.'] = 0
    i = 0
    #recherche de la lettre qui apparait le plus de fois et son nombre d'occurence
    maxi1 = 0
    lettremax1 = '' 
    while(i < len(cryptogramme1)):
        freq[cryptogramme1[i]] += 1
        if(freq[cryptogramme1[i]] > maxi1):
            lettremax1 = cryptogramme1[i]
            maxi1 = freq[cryptogramme1[i]]
        i += 1
    #on remet les compteurs a 0 pour la recherche de la lettre suivante de la lettre max la plus frequente
    for i in range(ord('a'),ord('z')+1):
        freq[chr(i)] = 0
    freq[','] = 0
    freq["'"] = 0
    freq['.'] = 0
    i = 0
    maxi2 = 0
    lettremax2 = ''
    while(i < len(cryptogramme1)-1):

        if(cryptogramme1[i] == lettremax1):
            freq[cryptogramme1[i+1]] += 1
            if(freq[cryptogramme1[i+1]] > maxi2):
                maxi2 = freq[cryptogramme1[i+1]]
                lettremax2 = cryptogramme1[i+1]
        i += 1

    pourcentage1 = round(((maxi1/len(cryptogramme1)) *100),2)
    pourcentage2 = round((maxi2/maxi1 *100),2)

    return [lettremax1, maxi1, str(pourcentage1)+'%', lettremax2, maxi2, str(pourcentage2)+'%']

 #analyse de frequence plus basique qui associe a chaque lettre sa frequence d'apparition dans un texte
def analyse_freq2(cryptogramme):
    cryptogramme1 = lisse(cryptogramme)
    freq = {}
    for i in range(ord('a'),ord('z')+1):
        freq[chr(i)] = 0
    #freq[','] = 0
    #freq["'"] = 0
    #freq['.'] = 0
    i = 0
    while(i < len(cryptogramme1)):
        freq[cryptogramme[i]] += 1
        i += 1

    for j in freq.keys():
        
        freq[j] =   round(((freq[j]/len(cryptogramme1)) *100),2)
 

    return freq
def brute_force(fic,n,eps):
    
    dico = {}
    dico['a'] = 8.15
    dico['b'] = 0.97
    dico['c'] = 3.15
    dico['d'] = 3.73
    dico['e'] = 17.39
    dico['f'] = 1.12
    dico['g'] = 0.97
    dico['h'] = 0.85
    dico['i'] = 7.31
    dico['j'] = 0.45
    dico['k'] = 0.02
    dico['l'] = 5.69
    dico['m'] = 2.87
    dico['n'] = 7.12
    dico['o'] = 5.28
    dico['p'] = 2.8
    dico['q'] = 1.21
    dico['r'] = 6.64
    dico['s'] = 8.14
    dico['t'] = 7.22
    dico['u'] = 6.38
    dico['v'] = 1.64
    dico['w'] = 0.03
    dico['x'] = 0.41
    dico['y'] = 0.28
    dico['z'] = 0.15

    cryptogramme = ""

    nomfic = fic
    # ouverture du fichier en mode lecture
    fic = open(nomfic,'r')
    #on parcourt les lignes du fichier
    for ligne in fic:
        # pour chaque ligne on parcourt les caracteres de la ligne
        for car in ligne:
            if car != "\n": 
                cryptogramme += car
    # ne pas oublier de fermer les fichiers
    fic.close()

    cryptogramme = lisse(cryptogramme)
    #creation d'un gros tableau avec toutes les clefs possibles
    big = enumere_keys(29)
    for cle in big:
        #on place l'inverse modulaire dans k[2]
        cle[2] = egcd(cle[0],n)[1]
        test = dechiffre(cryptogramme,cle,n)
        freq = analyse_freq2(test)
        bol = True
        for j in freq.keys():
            #pour toutes les lettres on regarde si elles passent le seuil de tolerence
            if(freq[j] > dico[j] + eps or freq[j] < dico[j] - eps):
                   
                bol = False
        #si oui on affiche le texte dechiffre supose juste
        if bol:
            print(test)
            print()

brute_force("crypto1.txt",26,5)
brute_force("crypto2.txt",26,5)
brute_force("crypto3.txt",26,5)
brute_force("crypto4.txt",26,5)
brute_force("crypto5.txt",26,5)
