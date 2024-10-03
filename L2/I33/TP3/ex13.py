def ord(a,p):
    i = 1
    divs1 = []
    divs2 = []
    while i <= int((p-1)**0.5)+1:
        if (p-1) % i == 0:
            divs1.append(i)
            divs2.append((p-1)//i)
        i += 1
    divs1 += [int((p-1)** 0.5)]
    i = 0
    while i < len(divs1):
        if pow(a,divs1[i],p) == 1:
            return divs1[i]
        i += 1

    i = 1
    while i < len(divs2):
        if pow(a,divs2[-i],p) == 1:
            return divs2[-i]
        i += 1

    return p-1


print(ord(22,71))

