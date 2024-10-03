import random as rd

def randtable(n, a, b):
    return [rd.randint(a, b) for i in range(n)]

test = randtable(10, 1, 10)
#print(test)


def insertion(T):
    
    i = 1
    while i < len(T):
        x = T[i]
        j = i
        while j > 0 and (T[j-1] > x):
            #T[j], T[j-1] = T[j-1], T[j]
            T[j] = T[j-1]
            j = j - 1
        T[j] = x
        i = i + 1

    return T

#print(insertion(test))


def iterative_merge(T1, T2):

    T = []

    i = 0
    k = 0
    while i < min(len(T1), len(T2)):

        if T1[i] < T2[k]:
            T.append(T1[i])
            i += 1
        else:
            T.append(T2[k])
            k += 1

    if i == len(T1):
        while i < len(T1):
            T.append(T1[i])
            i += 1
    elif k == len(T2):
        while k < len(T2):
            T.append(T2[k])
            k += 1

    return T


print(iterative_merge(A, B))
        



