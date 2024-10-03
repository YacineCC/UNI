def ens_to_int(A) :
    res = 0
    for el in A :
        res = res | (1<<al)
    return res 

def int_to_ens(t):
    i = 0
    l = []
    while t != 0 :
        if t&1 :
            l += [i,]
        i+=1
        t = t>>1
    return l
def est_dans(t,e) :
    return (t>>e)&1

print(est_dans(226325,14))
print(est_dans(71359,0))
print(est_dans(320094,4))
print(est_dans(404321,12))