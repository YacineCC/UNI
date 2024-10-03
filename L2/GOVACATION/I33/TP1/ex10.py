def minimum2(L):
    mini1 = L[1]
    mini2 = L[0]
    tab = []
    for i in L:

        if i < mini1 :
            mini2 = mini1
            mini1 = i
        elif(i < mini2 and i != mini1):
            mini2 = i
    return mini2
