from fctions import multiplie

def evalue(Q,y,P):
    result = 0
    for i in range(-1, -len(Q), -1):
        result = result ^ Q[i]
        result = multiplie(result, y, P)

    return result ^ Q[0]


print(evalue([6, 3, 4], 2, 13))
print(evalue([832, 575, 523, 450, 1168, 1391],1878,2053))
print(evalue([238, 138, 203, 252],125,285))
