import matplotlib.pyplot as plt

def gcd_original(a, b):
    while a != b:

        if a > b:
            a, b = a - b, b

        else:
            a, b = a, b - a

    return a


#print(gcd_original(1, 1))
#print(gcd_original(14, 24))
#print(gcd_original(11, 5))
    
#L = [x for x in range(1,257) ]

#print(L)

def Fibonacci(n):

    if n == 0 or n == 1:
        return n

    Fn = 0
    Fn1 = 1
    for i in range(n):
        Fn2 = Fn + Fn1 
        Fn = Fn1
        Fn1 = Fn2

    return Fn

def FibonacciSequence(n, m):

    seq = []
    if n == 0:
        seq.append(0)
    Fn = 0
    Fn1 = 1
    for i in range(m):
        Fn2 = Fn + Fn1 
        Fn = Fn1
        Fn1 = Fn2
        if i >= n-1:
            seq.append(Fn)

    return seq

def equi(n):

    seq = FibonacciSequence(0, n)

    nb_or = (1 + 5**0.5)/2
    
    binet = []
    for i in range(n+1):
        fi_n_5 = nb_or ** i / 5**0.5

        binet.append(seq[i] / fi_n_5)
    
    X = [x for x in range(n+1)]

    #plt.plot(X, seq, label='Fn')
    #plt.plot(X, binet, label='Fi^n')
    plt.plot(X, binet, label='fn / fi') 
    plt.legend()
    plt.show()

equi(100)


print(FibonacciSequence(5, 14))

