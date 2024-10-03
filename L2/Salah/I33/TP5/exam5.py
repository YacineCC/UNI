def multbyalpha(b ,f ) :
	m = len(bin(f)) - 3
	y = b << 1
	if ( y & (1 << m) != 0 ) :
		y = y ^ f
	return y 
	


def multiplication(b ,c ,f ) :
	s = 0 
	aux = c 
	while b != 0 :
		if (b & 1) != 0 :
			s = s ^ aux
		aux = multbyalpha(aux ,f)
		b = b >> 1
	return s 


def table_log(P) :
	d = len(bin(P)) - 3
	L = [-1 ,0 ,1 ] + [0] *((1<<d)-3)
	tmp = 2
	exp = 2
	tmp = multbyalpha(tmp,P) 
	while tmp != 1 :
		L[tmp] = exp
		tmp = multbyalpha(tmp,P) 
		exp += 1
	return L
	

def table_alpha(P) :
	d = len(bin(P)) - 3
	L = [1 ,2 ] + [0] *((1<<d)-3)
	tmp = 2
	exp = 2
	tmp = multbyalpha(tmp,P) 
	while tmp != 1 :
		L[exp] = tmp
		tmp = multbyalpha(tmp,P) 
		exp += 1
	return L


def multiplie(x,y,P):
    d = len(bin(P)) - 3
    if x==0 or y==0 :
        return 0
    e = (log_table[x] + log_table[y]) % ((1 << d) - 1)
    return alpha_table[e]
    
    
    
def evalue(Q,y,P):
    m = len(Q)
    res = Q[-1]
    for i in range(-2,-m-1,-1) :
        res = multiplie(res,y,P) ^ Q[i]
    return res
    
    

def sous_groupe_gen(b,f):
    res = b 
    L = []
    while res != 1 :
        L+= [res,] 
        res = multiplication(b,res,f)
    L += [1,]
    return L
    


def ordre(b,f):
    return len(sous_groupe_gen(b,f))



def symetrique_mul(x,P):
    d = len(bin(P)) - 3
    deg = (1<<d) - log_table[x] -1
    return alpha_table[deg]
    
    
def is_sym_mul(b,c,f):
    return multiplication(b,c,f) == 1
