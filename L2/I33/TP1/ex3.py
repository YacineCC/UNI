def somme(L,M):
    res = [L[0]*M[1]+M[0]*L[1],L[1]*M[1]]
    a = res[0]
    b = res[1]
    if a % b == 0:
        res = a / b
    else:
        while b != 0:

            a,b = b,a%b

        res[0] /= a
        res[1] /= a
    return res

print(somme([1,2],[3,2]))
