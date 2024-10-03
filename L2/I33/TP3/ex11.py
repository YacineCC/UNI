def is_sym_add(x,y):
    
    return ((x[0]*y[1])-(y[0]*x[1])) == 0 or  ((x[0]*y[1])+(y[0]*x[1])) == 0 

print(is_sym_add([104, 92],[-130, 115]))
