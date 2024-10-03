def minimum(L):

    mini = L[0]

    i = 1
    while i < len(L):

        if L[i] < mini :

            mini = L[i]
        i += 1

    return mini

print(minimum([3,2,5,7,2]))

