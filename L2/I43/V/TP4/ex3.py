def make_log_table_Z29():
	L = [0]*29	
	L[0] = -1
	i = 2
	j = 1 
	while((i)%29 != 1):
		L[(i)%29] = j
		j += 1
		i = i<<1
	return L

def inverse_Z29(x):
	
	L = make_log_table_Z29()
	return (1<<28-L[x])%29


def mat_id(n):
	return[[1 if i == j else 0 for j in range(n)] for i in range(n)]

def print_mat(mat):

	for i in mat:
		print(i,"\n")
		
def mat_inverse_Z29(mat):
    n = len(mat)
    Mid = mat_id(n)



    for j in range(n):

        k = j
        while(mat[k][j] == 0):
            k += 1

        if(k != j):
            mat[j],mat[k] = mat[k],mat[j]
            Mid[j],Mid[k] = Mid[k],Mid[j]

        inv = inverse_Z29(mat[j][j]%29)
        for x in range(n):
            mat[j][x] = mat[j][x] * inv %29
            Mid[j][x] = Mid[j][x] * inv %29
        for x in range(n):


            for y in range(j+1,n):
                ancre = mat[y][j] 
                for z in range(n):
                    mat[y][z] = (mat[y][z] - ancre*mat[j][z]) %29

                    Mid[y][z] = (Mid[y][z] - ancre*Mid[j][z]) %29
    
    i = n-1
    
    z = 0
    while(i >= 0): #digonal/pivot
        j = i-1
        
        while(j >= 0): #ligne
            coef = mat[j][i]
            for z in range(n): # colonne
                    mat[j][z] = (mat[j][z] - coef*mat[i][z]) %29

                    Mid[j][z] = (Mid[j][z] - coef*Mid[i][z]) %29
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
            som = (som + (Vec[j]* Mat[j][i])) % 29
            j += 1
        Res += [som]
        i += 1
    return Res

def translate(Vec):
    ch = ""
    dico = {}
    for i in range(ord('a'),ord('z')+1):
        dico[chr(i)] = ord(chr(i)) - 97
    
    dico['{'] = 26
    dico['}'] = 27
    dico['|'] = 26

    doci = {}
    for x in range(ord('a'),ord('z')+1):
        doci[ord(chr(x)) - 97] = chr(x)
    doci[26] = '{'
    doci[27] = '}'
    doci[28] = '|'
    for j in Vec:
        ch += doci[j]
    return ch

#Vec = [6,0,20,18,18]
#M = ([[8,24,7,9,25],[18,9,10,3,5],[13,6,13,2,5],[14,19,24,9,25],[22,4,15,11,26]])
Vec = [0,7,25,21,11]
M = [[2,7,22,9,25],[11,14,9,13,7],[13,7,1,2,5],[3,26,8,9,25],[22,4,3,12,26]]


print()
M = mat_inverse_Z29(M)
Vec = Prod_Vec_Mat(Vec,M)
print(Vec)

print(translate(Vec))
