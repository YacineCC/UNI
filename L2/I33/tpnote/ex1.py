def cardinal(t):
    nb = 0
    while t>0:
        if t & 1 == 1:
            nb = nb + 1 
        t >>= 1

        
    return nb
        
def plus_grand_elem(t):
    nb = 0
    while t>0:
        nb = nb + 1 
        t >>= 1
        
        
    return (nb-1)
 
def plus_petit_elem(t):
    nb = 0
    while t>0:
        if t & 1 == 1:
            return nb
        t >>= 1
        nb += 1
        
        
    return (nb)

print(plus_petit_elem(804))
 
