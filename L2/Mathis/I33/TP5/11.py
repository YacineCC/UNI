def is_sym_mul(b,c,f):
    puiss = 1 << (len(bin(f)[2:]) - 1)
    return alpha_table[(log_table[b] + log_table[c]) % puiss] == 1
