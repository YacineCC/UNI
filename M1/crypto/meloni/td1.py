import numpy as np
from math import gcd

def chiffrer(m, k):
    
    m = m.lower()
    c = ""
    for l in m:
        c += chr(((ord(l) - ord('a') + k) % 26) + ord('a'))

    return c

#print(chiffrer('cryptographie', 3))
#for i in range(25):
#    print(chiffrer('PELCGNANYLFRPYNFFVDHR', i))


freq_french = np.array([7.636, 0.901, 3.260, 3.669, 14.715, 1.066, 0.866, 0.737, 7.529, 0.613, 0.074, 5.456, 2.968, 7.095, 5.796, 2.521, 1.362, 6.693, 7.948, 7.244, 6.311, 1.838, 0.049, 0.427, 0.128, 0.326]) / 100

def analyse_freq(m):
    m = m.lower()
    occurences = np.zeros(26)
    occurences_doubles = {}

    for i, l in enumerate(m) :
        occurences[ord(l) - ord('a')]+= 1
        if ((m[i], m[i-1]) not in occurences_doubles.keys()):

            occurences_doubles[(m[i], m[i-1])] = 1
        else :
            occurences_doubles[(m[i], m[i-1])] += 1


    for k in occurences_doubles:
        occurences_doubles[k] /= len(occurences_doubles)
    
    
    return occurences / len(m), dict(sorted(occurences_doubles.items(), key=lambda item : item[1], reverse= True)) 



def coincidence(m) :
    
    #return sum((occurences * (occurences - 1)) / (len(m) * (len(m) - 1)))
    freq_text = analyse_freq(m)[0]
    return sum(freq_french * freq_text) 
    


#print(coincidence('cryptographie'))
#alphabet = [chr(i) for i in range(65, 91)]
#print(alphabet)


cipher_ex2 = 'AYAOSXNGWOSXORZYAFIHVYHOSXTIXGSKYFSVIGTFNSTYAOBWXYEYTNIOTGWWXOHOTVIYVYNAOTAYWFNHOTVGBYTFGSKVYLGAXDWFOMXGWEIYAOTFYBWOXGITYILWXYWGXYLYNYFSVIGTFNGSFILINYXYFGTGLDNYXVIHHYXYTFNNDNFYBYNAXDWFOMXGWEIQSYNGVGWFYNGSKYKIMYTAYNBOVYXTYNYTBGFIYXYVYNYASXIFYVYAOTHIVYTFIGLIFYVITFYMXIFYYFVGSFEYTFIAIFYVYNVOTTYYNLYAOSXNITALSFVYNGNWYAFNFEYOXIQSYNYFWXGFIQSYNBYFFGTFLGAAYTFNSXLYNGLMOXIFEBYNVYAEIHHXYBYTFNDBYFXIQSYYFGNDBYFXIQSYGITNIQSYNSXLGBINYYTSUXYVYAYNGLMOXIFEBYNUIGVYNOSFILNFYLNQSYWDFEOTYFOWYTNNL'


cipher_ex1 = 'PELCGNANYLFRPYNFFVDHR'

#ics = []
#for i in range(26):
#    tmp = chiffrer(cipher_ex1, i)
#    ic = coincidence(tmp)
#    ics.append([ic, i])

#print(sorted(ics, reverse=True)[:5])
#print(chiffrer(cipher_ex1, max(ics)[1]))


alphabet_dict = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
def dsubstitution(m):
    M = m
    alphabet_dict_rev = {}
    m = m.lower()
    frequences = analyse_freq(m)

    freq = frequences[0]

    freq_double = frequences[1]

    idx_text_dec = np.argsort(freq)[::-1]
    idx_french_dec = np.argsort(freq_french)[::-1]

   
    #for i in range(26):
        #alphabet_dict_rev[chr(idx_text_dec[i] + 97)] = chr(idx_french_dec[i] + 97)


    alphabet_dict_rev['y'] = 'e'
    alphabet_dict_rev['o'] = 'o'
    alphabet_dict_rev['s'] = 'u'
    alphabet_dict_rev['n'] = 's'
    alphabet_dict_rev['i'] = 'i'
    alphabet_dict_rev['h'] = 'f'
    alphabet_dict_rev['v'] = 'd'
    alphabet_dict_rev['t'] = 'n'
    alphabet_dict_rev['k'] = 'x'
    alphabet_dict_rev['b'] = 'm'
    alphabet_dict_rev['e'] = 'h'
    alphabet_dict_rev['d'] = 'p'
    alphabet_dict_rev['l'] = 'l'
    alphabet_dict_rev['m'] = 'g'

    alphabet_dict_rev['f'] = 't'
    #alphabet_dict_rev['n'] = tmp

    #alphabet_dict_rev['v'] = 't'

    alphabet_dict_rev['a'] = 'c'
    alphabet_dict_rev['x'] = 'r'
    alphabet_dict_rev['g'] = 'a'
    alphabet_dict_rev['w'] = 'p'
    alphabet_dict_rev['r'] = 'b'
    alphabet_dict_rev['z'] = 'j'



    
    print(alphabet_dict_rev)

    d = ''
    for i, l in enumerate(m):
        if l in alphabet_dict_rev:
            d += alphabet_dict_rev[l]
        else :
            d += M[i]

    print(freq_double, freq)
    return d, coincidence(d)


#print(dsubstitution(cipher_ex2)) 

#print(analyse_freq(cipher_ex2))

cipher_ex3 = 'NPGJTJHCIFPZKRIPPVGPWVFRUJWVPQGOIESMHQVGXIPETCCWWMWVTXWEMQYTQWCCWTJLFGEMSFIFLRUWISFINFRGXIOPPGEXTPHWXIUDEIPGNLMTAIWEWWTZCYXULTQDMVTSPOEPDGGWYKNMGEVGCIOAPCNIGAETOIUWIVEVGDHKQJGCIPEIUNSPEVCTVGXIPEEWYWADXGXIFPGJTJHCIOPRVXSPZENALCMIVTUWPGQXQGWIESMHQVGOIEPWCCUWTPWEMNTWGNIRPRFLRVNSOXIEZQRZWCYXEPXVPQGELQOITPWKDXGLMPDMCWEPLPADIFPJTPUWPREPWEPUWTIUEYPLZCYXCRIFPGKDMHDYTWIUNLKQJTPQGYXUXSPZENALCMIVTUWPWEPTGYHCYXNPGJTJHCIFPZKRIPPVGLIVPTGCGGAETWIOLNQCTTFWUTIPQVKPHTTGJVEUTWMTUWTERFFNTIULQGELQOIGYHGAYKDGGEXGPTQBYGTPPZJHCIRWYULYEFRGDIEFVKEI'
tab = []
for i in range(len(cipher_ex3)):
    
    patern = cipher_ex3[i:i + 4]
    idx = cipher_ex3.find(patern,i+4)
    if idx != -1:
        print(idx - i, patern)
        if idx - i not in tab :
            tab.append(idx - i)

pgcd = gcd(tab[0], tab[1])
for i in range(2, len(tab)):
    pgcd = gcd(pgcd, tab[i])

print(tab)


decal_0 = cipher_ex3[::3]
decal_1 = cipher_ex3[1::3]
decal_2 = cipher_ex3[2::3]
analyse_0 = analyse_freq(decal_0)[0]
cesar_0 = np.argmax(analyse_0)

analyse_1 = analyse_freq(decal_1)[0]
cesar_1 = np.argmax(analyse_1)

analyse_2 = analyse_freq(decal_2)[0]
cesar_2 = np.argmax(analyse_2)



decal_0 = chiffrer(decal_0,  - (cesar_0 - 4) % 26)
decal_1 = chiffrer(decal_1, - (cesar_1 - 4) % 26)
decal_2 = chiffrer(decal_2, - (cesar_2 - 4) % 26)


dechiffer = ''

i = 0
while i < len(decal_2):
    dechiffer += decal_0[i]
    dechiffer += decal_1[i]
    dechiffer += decal_2[i]
    i += 1

print(dechiffer)

cipher_ex4 = "NOPXNQEKMBPGSZIZPUGKCZRWXPBPUKMHHPWZIMCPKMHRGGFAIXEFMEHGQQATPEGBFRWBFGIOUVBSHTSFJVTNMMFCTSFTXZUKTSYCBSPOPPTZZRTIZIZLDNKHRWFMJVPVNMRRPGQBJWEWMZBGIHGMLTKIRHKFQTBLDNBSZRGPTDLNMTIVRCGGBCAOIWYNSDHIERTLIPVWACQWELBRBPQQCUPSNZSQGHDPLFIKMDYWGRXLPLXUSAVZATCGRXCBVPHQGXCEMMRBKHFGIOUBZSNWTGGMEAFMGHTSCJMWEMMLGGZGXMDTWMZVXFQHWFVXVHNNCDPTWOUTWTGOZIIOELIDCTCJXULTBWBFFSEEMCTXARRUSZHDZIKLSFQINAQDABVGVNSEEZZGKIAZGGODUAIEMGFQBFTVREGMFNNPQPCNONXDYWGDPXTDXADBWFBGWOUBZSYGIDHZPSNTHNVGCJMWELXFBIFMBUPSBVHRTDDTBPSMGDVSIQBMYTNVDEQUDPUXEVMGGFWJUWTSITIFTOBXLPQNCBCTCSGIXMXMEHKJMAMYTXVDLVVACMYRXDOAEVQAIXOBVREGAASQQIVIHVQBZTKPSLQHRFSDTTLNVMFYCHAIIWIMMRHRFARMDSNARRECYEQWAMQCAESCJQAENBFRPRDTTPDXDSYQDBTUPNMXZHUZMQWCIXCLPGGFAICABACARCGGTLQNMZYGZQHOCOLXFBIFMBUPSLWBGFSODCAELMBFQIEEZZGKIAZGGBDCGAGBSGTSBPZEIXTZROSZIKZMIQZRUWZSMAEGLOZOSZIWYPTZZRUCGKMYTIIFNDIESMWAGOOTGRQAIYGTOSQGDDDOCAFUOGKCZRWXPBTSBWWZIMCPKMHRKZQHBTMIWFGCBFSMNOFXFRPRDTYFUGTOAIOSTLPPKWUECAYPBTOGMGGCJMCBEONBIAGBAGUPCXAHYKABAIEAMQCAFSOTBEEGWFZGEGXXPUMLCAPSDACTAECHVNWEPBTOGLIAECYEQWAMMIEQIPJVTNMMFCTSFT"

tab = []
for i in range(len(cipher_ex4)):
    
    patern = cipher_ex4[i:i + 4]
    idx = cipher_ex4.find(patern,i+4)
    if idx != -1:
        print(idx - i, patern)
        if idx - i not in tab :
            tab.append(idx - i)

pgcd = gcd(tab[0], tab[1])
for i in range(2, len(tab)):
    pgcd = gcd(pgcd, tab[i])

print(pgcd)
print(tab)


decal_0 = cipher_ex4[::3]
decal_1 = cipher_ex4[1::3]
decal_2 = cipher_ex4[2::3]
analyse_0 = analyse_freq(decal_0)[0]
cesar_0 = np.argmax(analyse_0)

analyse_1 = analyse_freq(decal_1)[0]
cesar_1 = np.argmax(analyse_1)

analyse_2 = analyse_freq(decal_2)[0]
cesar_2 = np.argmax(analyse_2)



decal_0 = chiffrer(decal_0,  - (cesar_0 - 4) % 26)
decal_1 = chiffrer(decal_1, - (cesar_1 - 4) % 26)
decal_2 = chiffrer(decal_2, - (cesar_2 - 4) % 26)


dechiffer = ''

i = 0
while i < len(decal_2):
    dechiffer += decal_0[i]
    dechiffer += decal_1[i]
    dechiffer += decal_2[i]
    i += 1

#print(dechiffer)