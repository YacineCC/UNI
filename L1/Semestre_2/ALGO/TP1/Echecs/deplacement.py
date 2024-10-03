#
# Fichier à compléter: deplacement.py
#
# Chaque fonction doit renvoyer la liste des indices (col,lig) des
# cases sur lesquelles la pièce en question peut aller.
#

def cases_fou(col,lig):
	
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un fou positionné sur la case (col, lig)

    Ex: fou en (2,3) 
    - - - - - - - - - -
    |           x     |
    | x       x       |
    |   x   x         |
    |     F           |
    |   x   x         |
    | x       x       |
    |           x     |
    |             x   |
    - - - - - - - - - -

    """
    L = []
    i = col + 1
    j = lig + 1
   
    n = 8
    while i < n and j < n:
    	L += [(i,j)]
    	i += 1
    	j += 1
    	
    i = col - 1 
    j = lig - 1
    while i >= 0 and j >= 0:
    	L += [(i,j)]
    	i -= 1
    	j -= 1
    	
    i = col - 1 
    j = lig + 1
    while i >= 0 and j < n:
    	L += [(i,j)]
    	i -= 1
    	j += 1
    i = col + 1 
    j = lig - 1
    while i < n and j >= 0:
    	L += [(i,j)]
    	i += 1
    	j -= 1
    return L
def cases_tour(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer une tour positionnée sur la case (col, lig)

    Ex: tour en (5,3)
    - - - - - - - - - -
    |           x     |
    |           x     |
    |           x     |
    | x x x x x T x x |
    |           x     |
    |           x     |
    |           x     |
    |           x     |
    - - - - - - - - - -

    """
    L = []
    i = col 
    j = lig + 1
    n = 8
    
    while i < n and j < n:
    	L += [(i,j)]
    	j += 1
    	
    i = col 
    j = lig - 1
    while i < n and j >= 0:
    	L += [(i,j)]
    	j += -1
    	
    i = col + 1
    j = lig 
    while i < n and j < n:
    	L += [(i,j)]
    	i += 1
    i = col - 1
    j = lig 
    while i >= 0 and j < n:
    	L += [(i,j)]
    	i -= 1	
    return L

def cases_reine(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un fou positionnée sur la case (col, lig)

    Ex: dame en (6,1)
    - - - - - - - - - -
    |           x x x |
    | x x x x x x D x |
    |           x x x |
    |         x   x   |
    |       x     x   |
    |     x       x   |
    |   x         x   |
    | x           x   |
    - - - - - - - - - -

    """
    return cases_fou(col,lig) + cases_tour(col,lig)

def cases_roi(col,lig):
   """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un roi positionné sur la case (col, lig)

    Ex: Roi en (4,5)
    - - - - - - - - - -
    |                 |
    |                 |
    |                 |
    |                 |
    |      x x x      |
    |      x R x      |
    |      x x x      |
    |                 |
    - - - - - - - - - -
"""
   L = []
   for x in cases_reine(col,lig):
   	if col - 1 <= x[0] <= col + 1 and lig - 1 <= x[1] <= lig +1: 
   	 L += [x]
   return L

def cases_cavalier(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un fou positionné sur la case (col, lig)

    Ex: cavalier en (3,3)
    - - - - - - - - - -
    |                 |
    |     x   x       |
    |   x       x     |
    |       C         |
    |   x       x     |
    |     x   x       |
    |                 |
    |                 |
    - - - - - - - - - -

    """
    L = []
    L += [(col+2,lig-1)]
    L += [(col+1,lig-2)]
    L += [(col+1,lig+2)]
    L += [(col-1,lig+2)]
    L += [(col-2,lig+1)]
    L += [(col-2,lig-1)]
    L += [(col-1,lig-2)]
    L += [(col+2,lig-1)]
    L += [(col+2,lig+1)]
    n = 8
    T = []
    for l in L:
    	if 0 <= l[0] < n and 0<= l[1] < n:
    		T += [l]
    return T
    
   

def cases_pion(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un fou positionné sur la case (col, lig)

    Ex: pions en (1,6) et (5,3)
    - - - - - - - - - -
    |                 |
    |                 |
    |           x     |
    |           P     |
    |   x             |
    |   x             |
    |   P             |
    |                 |
    - - - - - - - - - -

    """
    L = []
  
    if lig - 1 >= 0 :
    	L += [(col, lig - 1)]
    	if lig == 6:
    		L += [(col,lig - 2)]
    
    	
    return L
  
