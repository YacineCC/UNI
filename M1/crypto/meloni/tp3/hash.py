from sympy import factorint
from Crypto.Hash import SHA256
from cesar import sort_indice
from random import randint

def hash_1(input_string):
    return sum(ord(char) for char in input_string)

def hash_2 ( input_string ):
    h = [15 ,87 ,48 ,65]
    for char in input_string :
        tmp = h . pop ()+ ord ( char )
        h . insert (0 , tmp % 100)
    return ' '. join ( map ( str , h ))

def hash_3 ( input_string ):
    p = 637478271281448807312372970443159127031
    R = 346647589564164759049672764997687712320
    h = 0
    for char in input_string :
        h = ( h + ord ( char ))* R % p
    return h

def SHEE(message, difficulte):
    h = SHA256.new()
    nonce = 0
    message1 = message + str(nonce)
    h.update(bytes(message1, "UTF8"))
    while int(h.hexdigest(), 16) >= 2**(256-difficulte):
        nonce += 1
        h = SHA256.new()
        message1 = message + str(nonce)
        h.update(bytes(message1, "UTF-8"))
    print(int(h.hexdigest(), 16))
    return nonce

def collision_bourrin():
    tab_hash = []
    trouve = False
    i = 0
    while not trouve:
        h = SHA256.new()
        h.update(bytes(str(i), "UTF-8"))
        tab_hash += [int(h.hexdigest(), 16) % 2**40]
        indices = recherche_double(tab_hash)
        if indices:
            trouve = True
        i += 1
    return indices

def collision_bourrin_trie():
    tab_hash = []
    i = 0
    while i < 2**22:
        h = SHA256.new()
        h.update(bytes(str(i), "UTF-8"))
        tab_hash += [int(h.hexdigest(), 16) % 2**40]
        i += 1
    print("triage")
    tab_indice_trie = sort_indice(tab_hash)
    print("recherche")
    indices = recherche_double_trie(tab_hash, tab_indice_trie)
    return indices

def encode_neuil(neuil):
    n = SHA256.new()
    n.update(str(neuil).encode())
    return int(n.hexdigest(), 16)

def collision_non_neuil():
    dico = {}
    mod = 1 << 40
    cpt = 0
    while True:
        x = randint(0, mod)
        y = encode_neuil(x) % mod

        if y in dico:
            if x != dico[y]:
                print(x, dico[y], y, cpt, (encode_neuil(x) % mod) == (encode_neuil(dico[y]) %mod))
                break
        else:
            dico[y] = x

        cpt += 1
        


def recherche_double(tab):
    """recherche un doublon dans tab est rencoie leur indice"""
    i = 0
    while i < len(tab) - 1:
        j = i + 1
        while j < len(tab):
            if tab[j] == tab[i]:
                print("hash", tab[i], tab[j])
                print("indice", i, j)
                return i, j
            j += 1
        i += 1
    return None

def recherche_double_trie(tab, tab_indice):
    i = 0
    while i < len(tab) - 1:
        j = i + 1
        if tab[tab_indice[i]] == tab[tab_indice[j]]:
            return tab_indice[i], tab_indice[j]
        i = j 
    return None


if __name__ == "__main__":
    # res = SHEE("hash precedent: 00766536a5ad7d4e9644378a23c07a4c4a2ee15b048dad770e601a488ab35666 difficulte: 8 Ceci est un bloc a valider.  La difficulte de validation est de 12 cette fois.", 12)
    # print(res)
    #print(collision_bourrin_trie())
    collision_non_neuil()
