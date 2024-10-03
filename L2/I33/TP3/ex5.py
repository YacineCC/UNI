from random import randrange

def generateur(p):
    g = randrange(1,p)
    
    formule = pow(g,(p-1)//2,p)

    while formule == 1:
        g = randrange(1,p)

        formule = pow(g,(p-1)//2,p)

    return g

print(generateur(5))
print(generateur(263))
print(generateur(383))
