def combinaison_lineaire(c,V):
    combi = [0] * len(V[0])
    i = 0
    while i < len(c):
        j = 0
    
        while j < len(V[0]):
            combi[j] += c[i] * V[i][j]
            j += 1
        i += 1
    return combi

print(combinaison_lineaire([1,2,3],[[1,1,1],[1,2,3],[2,2,2]]))
