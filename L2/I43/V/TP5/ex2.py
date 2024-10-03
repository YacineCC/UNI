def make_log_table_Z31():
	L = [0]*31	
	L[0] = -1
	i = 2
	j = 1 
	while((i)%31 != 1):
		L[(i)%31] = j
		j += 1
		i = i<<1
	return L

def inverse_Z31(x):
	
	L = make_log_table_Z31()
	return (1<<30-L[x])%31


def mat_id(n):
	return[[1 if i == j else 0 for j in range(n)] for i in range(n)]

def print_mat(mat):

	for i in mat:
		print(i,"\n")
		
def mat_inverse_Z31(mat):
    n = len(mat)
    Mid = mat_id(n)



    for j in range(n):

        k = j
        while(mat[k][j] == 0):
            k += 1

        if(k != j):
            mat[j],mat[k] = mat[k],mat[j]
            Mid[j],Mid[k] = Mid[k],Mid[j]

        inv = inverse_Z29(mat[j][j]%31)
        for x in range(n):
            mat[j][x] = mat[j][x] * inv %31
            Mid[j][x] = Mid[j][x] * inv %31
        for x in range(n):


            for y in range(j+1,n):
                ancre = mat[y][j] 
                for z in range(n):
                    mat[y][z] = (mat[y][z] - ancre*mat[j][z]) %31

                    Mid[y][z] = (Mid[y][z] - ancre*Mid[j][z]) %31
    
    i = n-1
    
    z = 0
    while(i >= 0): #digonal/pivot
        j = i-1
        
        while(j >= 0): #ligne
            coef = mat[j][i]
            for z in range(n): # colonne
                    mat[j][z] = (mat[j][z] - coef*mat[i][z]) %31

                    Mid[j][z] = (Mid[j][z] - coef*Mid[i][z]) %31
            j -= 1
        i -= 1
    
    
    return Mid

def Prod_Vec_Mat(Vec,Mat):
    Res = []
    i = 0
    while i < len(Vec):
        som = 0
        j = 0
        while j < len(Mat):
            som = (som + (Vec[j]* Mat[j][i])) % 31
            j += 1
        Res += [som]
        i += 1
    return Res

def translate(Vec):
    ch = ""
    dico = {}

    for i in range(ord('a'), ord('z')+1):
        dico[chr(i)] = ord(chr(i))-97

    dico['?'] = 26
    dico[','] = 27
    dico[' '] = 28
    dico["'"] = 29
    dico['.'] = 30

    doci = {}
    for x in range(ord('a'),ord('z')+1):
        doci[ord(chr(x)) - 97] = chr(x)
    doci[26] = '?'
    doci[27] = ','
    doci[28] = ' '
    doci[29] = "'"
    doci[30] = '.'
    for j in Vec:
        ch += doci[j]
    return ch
    
def decoupe(s,n):
    
    dico = {}

    for i in range(ord('a'), ord('z')+1):
        dico[chr(i)] = ord(chr(i))-97

    dico['?'] = 26
    dico[','] = 27
    dico[' '] = 28
    dico["'"] = 29
    dico['.'] = 30
    
    tab = []
    i = 0
    j = 0
    tmp = [" "] * n
    while(i < len(s)):
        if(j >= n):
            j = 0
            tab += [tmp]
            tmp = [" "] * n
        tmp[j] = s[i]
        j += 1
        i += 1
    tab += [tmp]
    
    tabo = []
    tmp = []
    for j in tab:
    	
    	for z in j:
    		
    		tmp += [dico[z]]
    	tabo += [tmp]
    	tmp = []
    return tabo

def Hill_chiffre(s,cle):
	L = decoupe(s,len(cle))
	tab = []
	for i in L:
		tab += [translate(Prod_Vec_Mat(i,cle))]
	return tab

s = "la mer est calme sous le ciel bleu. les oiseaux volent en cercles au dessus. les vagues s'echouent doucement sur le sable."

cle = [[13, 23, 30, 25], [22, 13, 7, 13], [8, 0, 10, 22], [19, 22, 27, 18]]

print(Hill_chiffre(s,cle))

