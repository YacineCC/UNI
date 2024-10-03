def est_dans(t,e):
    return ((t >> e)  & 1) == 1 

print(est_dans(50173,9))
