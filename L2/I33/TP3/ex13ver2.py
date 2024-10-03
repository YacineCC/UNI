def ord(a,p):

    if a == 1:
        return 1

    i = 2
    ordre = p-1
    while i <= int((p-1) ** 0.5) + 1:

        if (p-1) % i == 0:

            if pow(a,i,p) == 1 and i < ordre:
                ordre = i

            elif pow(a,((p-1)//i),p) == 1 and ((p-1)//i) < ordre:

                ordre = (p-1) // i

        i += 1

    return ordre

print(ord(13,17))


