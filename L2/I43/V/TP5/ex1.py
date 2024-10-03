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

print(decoupe("test",4)[0])
