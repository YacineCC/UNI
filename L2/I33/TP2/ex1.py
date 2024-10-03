def ens_to_int(A):
    t = 0
    for i in A:
        t = t | (1<<i)

    return t

print(ens_to_int([2,5,8,9]))

