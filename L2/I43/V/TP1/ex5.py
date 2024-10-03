def resolution_affine(bigramme):
    
    dico = {}

    for i in range(ord('a'), ord('z') + 1):
        dico[chr(i)] = i - 97

    
    dico[' '] = 26
    dico['\''] = 27
    dico['.'] = 28
    
    u = dico[bigramme[1]] - dico[bigramme[0]]
    u = (u * (-2)) % 29
    a = (dico[bigramme[0]] - 4 * u) % 29
    return [u,a]
print(resolution_affine('fs'))
