def minimum_posi(L):
    
    mini = 0
    T = [mini] 
    i = 1
    while i < len(L):
    	
    	if L[i] < L[mini]:
    		
    		mini = i
    		T = [i]
    	elif L[i] == L[mini]:
    		T += [i]
    	i += 1
    
    return T
    	
    	
    	
