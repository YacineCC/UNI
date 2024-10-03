def multiplie(x,y,P):
    # Accès à 2 dict:
    # log_table[x] renvoie i tq x = alpha^i
    # alpha_table[i] renvoie z tq z = alpha^i
    if x * y == 0: return 0
    puiss_x = log_table[x]
    puiss_y = log_table[y]

    # On calcule la puissance de z
    puiss_z = (puiss_x + puiss_y) % ((1 << len(bin(P)[2:]) - 1) - 1)
    return alpha_table[puiss_z]
