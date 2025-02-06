import numpy as np

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

    for l in m :
        occurences[ord(l) - ord('a')]+= 1
    
    return occurences / len(m)



def coincidence(m) :
    
    #return sum((occurences * (occurences - 1)) / (len(m) * (len(m) - 1)))
    freq_text = analyse_freq(m)
    return sum(freq_french * freq_text) 
    


print(coincidence('cryptographie'))
alphabet = [chr(i) for i in range(65, 91)]
#print(alphabet)


cipher_ex2 = 'AYAOSXNGWOSXORZYAFIHVYHOSXTIXGSKYFSVIGTFNSTYAOBWXYEYTNIOTGWWXOHOTVIYVYNAOTAYWFNHOTVGBYTFGSKVYLGAXDWFOMXGWEIYAOTFYBWOXGITYILWXYWGXYLYNYFSVIGTFNGSFILINYXYFGTGLDNYXVIHHYXYTFNNDNFYBYNAXDWFOMXGWEIQSYNGVGWFYNGSKYKIMYTAYNBOVYXTYNYTBGFIYXYVYNYASXIFYVYAOTHIVYTFIGLIFYVITFYMXIFYYFVGSFEYTFIAIFYVYNVOTTYYNLYAOSXNITALSFVYNGNWYAFNFEYOXIQSYNYFWXGFIQSYNBYFFGTFLGAAYTFNSXLYNGLMOXIFEBYNVYAEIHHXYBYTFNDBYFXIQSYYFGNDBYFXIQSYGITNIQSYNSXLGBINYYTSUXYVYAYNGLMOXIFEBYNUIGVYNOSFILNFYLNQSYWDFEOTYFOWYTNNL'


cipher_ex1 = 'PELCGNANYLFRPYNFFVDHR'

ics = []
for i in range(26):
    tmp = chiffrer(cipher_ex1, i)
    ic = coincidence(tmp)
    ics.append([ic, i])

print(sorted(ics, reverse=True)[:5])
print(chiffrer(cipher_ex1, max(ics)[1]))


alphabet_dict = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
def dsubstitution(m):
    #alphabet_dict = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
    alphabet_dict_rev = {}
    m = m.lower()
    freq = analyse_freq(m)

    idx_text_dec = np.argsort(freq)[::-1]
    idx_french_dec = np.argsort(freq_french)[::-1]

   
    for i in range(26):
        alphabet_dict_rev[chr(idx_text_dec[i] + 97)] = chr(idx_french_dec[i] + 97)



    tmp = alphabet_dict_rev['f']
    alphabet_dict_rev['f'] = alphabet_dict_rev['n']
    alphabet_dict_rev['n'] = tmp

    tmp = alphabet_dict_rev['i']
    alphabet_dict_rev['i'] = alphabet_dict_rev['n']
    alphabet_dict_rev['n'] = tmp
    print(alphabet_dict_rev)

    d = ''
    for l in m:
        d += alphabet_dict_rev[l]


    return d, coincidence(d)


print(dsubstitution(cipher_ex2)) 
