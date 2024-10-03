def swap(T,a,b):
	tp = T[a]
	T[a] = T[b]
	T[b] = tp

def bbr(T):
	
	tab = []
	B = 0
	R = len(T) - 1
	W = 0
	while W <= R:
		if T[W] == "white":
			W += 1
		elif T[W] == "red":
			swap(T,W,R)
			tab += [(W,R)]
			R -= 1
		else:
			swap(T,W,B)
			tab += [(W,B)]
			B += 1
			W += 1
	
	return tab
print(bbr(['white','white','red','blue','blue','red','white']))   
   
def fusionner(T1,T2):
	i,j,k = 0,0,0
	n = len(T1)
	m = len(T2)
	T3 = [0] * (n+m)
	comp = 0
	
	while i < n and j < m:
		if T1[i] < T2[j]:
			T3[k] = T1[i]
			i += 1
		else:
			T3[k] = T2[j]
			j += 1
		k += 1
		comp += 1
	if i < n :
		while i < n:
			T3[k] = T1[i]
			i,k = i+1, k+1
	
	else:
		
		while j < m:
			T3[k] = T2[j]
			j,k = j+1, k+1
	
	return T3,comp
print(fusionner([1,4,6,8,10],[2,3,9,11]))

print(fusionner([41, 44, 50, 54],[49, 49, 65, 92]))



def fusion_partielle(T,a,b):
	T1 = T[:a]
	T2 = T[a:b]
	T[:b],comp = fusionner(T1,T2)
	return T,comp
	
"""def fusion_partielle(T,a,b):
	return fusionner(T[:a],T[a:b])"""

T = [2,4,5,3,6,8,5,4,2,7]
a = 3
b = 6
print(fusion_partielle(T,a,b))
print(fusion_partielle([31, 78, 76, 39, 34, 42, 62, 7, 42, 2], 2, 3))

def tri_insertion(T):
	comp = 0
	i = 1 
	while i < len(T):
		j = i
		while j > 0 and T[j] < T[j-1]:
			
			swap(T,j,j-1)
			comp += 1
			j -= 1
		comp += 1
		i += 1 
		
	
	return T,comp
	
def tri_partiel(T,a,b):
	test = T[a:b] 
	T[a:b],comp = tri_insertion(test)
	return T,comp

T = [2,4,5,3,6,8,5,4,2,7]
print(tri_partiel(T,2,8))
print(tri_partiel([32, 79, 11, 39, 94, 57, 23, 36, 37, 34], 6, 7))
print(tri_partiel([18, 78, 89, 8, 73, 93, 91, 15, 78, 60, 29, 38, 4, 25, 97, 86, 53, 53, 73, 5], 2, 7))	

def tri_morceau(T,m):
	i = min(m,len(T))
	cpt = tri_partiel(T,0,i)[1]
	while i < len(T):
		j = min(i+m,len(T))
		cpt += tri_partiel(T,i,j)[1]
		cpt += fusion_partielle(T,i,j)[1]
		i = j 
		
	return cpt
print(tri_morceau([4,5,6,7,8,23,22,11,5,0,4,9,7],4))

def diff(ch1,ch2):
	i = 0
	Continuer = True
	while Continuer and i < len(ch1) and i < len(ch2):
		if ch1[i] == ch2[i]:
			i += 1
			Continuer = True
		else:
			Continuer = False
	if i >= len(ch1) or i >= len(ch2):
		return -1
	else:
		return i

def swap(T,a,b):
	tp = T[a]
	T[a] = T[b]
	T[b] = tp
	
def tri_alien(T,m):
    dicoAlien = {}
    for i in range(len(m)):
        dicoAlien[m[i]] = i
    i = 0
    while i < len(T):
        imin = i
        j = i + 1

        while j < len(T):
            b = diff(T[j],T[imin])
        
            if(b>=0):
                if dicoAlien[T[j][b]] < dicoAlien[T[imin][b]]:
                    imin = j
            else :
                if(len(T[j]) < len(T[imin])):
                    imin = j
            j += 1
        swap(L,i,imin)
        i += 1
    return T

L = ['#!', '@!@', '!!^^!', '@#!!^', '!']
A =  '@!#^'
L = ['///*././.*/*', '*./....*./*./**/.*', '*/*****./.**/...*', '//*.*/*././', '//*../*.**/*/*', '*././/.*..///*../*', '.*..*/*.**', './/.//**../*.', '*./*/*.***', './/../****', '/.*.//**/**..///..', '/*..*//', '.*/****.*', '../', '../*.*.//./', '.../', '//*///*.*/////*.*', './**.**', '....', '*/.**.*', './.*//*.*./', '**///.**/*/*./****', '..///.**.*.*/*.', '//*.././////.////./', './//./***', './**//./*./*..', '**../*/.*', '//./**/', './//*.**/*//', '././/////.///.///']
A = '/*.'
test =  ['///*././.*/*', '//*///*.*/////*.*', '//*.*/*././', '//*../*.**/*/*', '//*.././////.////./', '//./**/', '/*..*//', '/.*.//**/**..///..', '*/*****./.**/...*', '*/.**.*', '**///.**/*/*./****', '**../*/.*', '*./*/*.***', '*././/.*..///*../*', '*./....*./*./**/.*', './//*.**/*//', './//./***', './/.//**../*.', './/../****', './**//./*./*..', './**.**', '././/////.///.///', './.*//*.*./', '.*/****.*', '.*..*/*.**', '../', '..///.**.*.*/*.', '../*.*.//./', '.../', '....']
print(test == tri_alien(L,A))
