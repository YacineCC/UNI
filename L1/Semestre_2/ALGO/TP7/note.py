from pilefile import *

def swap(T,a,b):
    tp = T[a]
    T[a] = T[b]
    T[b] = tp
    
def nb2pairs(T):
	tabPairs = []
	for tab in T:
		pairs = 0
		for s in tab:
			if s % 2 == 0:
				pairs += 1
		tabPairs += [pairs]
	return tabPairs
	
def Tri(M):	
	
	tableau = nb2pairs(M)
	i = 1 
	while i < len(tableau):
		j = i
		while j > 0 and tableau[j] < tableau[j-1]:
			
			swap(tableau,j,j-1)
			swap(M,j,j-1)
			
			j -= 1
		
		i += 1 
		
	return M


M =[[74, 36, 42, 29], [30, 3, 79, 72], [39, 57, 15, 38], [93, 31, 34, 97], [96, 49, 6, 12], [56, 35, 61, 91], [3, 37, 10, 39], [6, 67, 62, 99]]

#print(nb2pairs(M))

#print(Tri(M))


def Norme1(tup):
	maxi = abs(tup[0])
	
	if abs(tup[1]) > maxi:
		maxi = abs(tup[1])
	return maxi


def Ranger(L):
	g = 0
	m = 0
	d = len(L) - 1

	while m <= d:
	
		if Norme1(L[m]) == 1:
			m += 1
			
			
		elif Norme1(L[m]) < 1:
			swap(L,m,d)
			
			d -= 1
			
			
			
		elif Norme1(L[m]) > 1:
			
			swap(L,m,g)
			m += 1
			g += 1
	return L
			
			
	
L = [ (0,1) , (-1,2), (1,1), (0.5, 0), ( -1,0), (0,0) ]

"""def parcours_diagonal(M):
    
    
    			
    	if nb0 > max0:
    		max0= nb0
 
     	
    return max0 


M = [[1,0,3,1,0],[2,4,7,2,0],[0,1,2,0,1],[0,0,5,0,1],[2,0,1,2,1]]

print(parcours_diagonal(M))"""



def chaine_ab(n):
	L = ['aab','aba','baa','bab']
	P = pile_init()
	i = 0
	j = 0
	while j < (2*n)-1:
		i = 0
		while i < len(L):
			if (L[j][-1] != 'b') or (L[i][0] != 'b'):
				empiler(P,L[j]+L[i])
			i += 1
			
		j += 1
	print(P)

chaine_ab(1)
		
		
		
		
		
		
		
		
		
		
		
		
