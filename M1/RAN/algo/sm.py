import time
import matplotlib.pyplot as plt

def SquareMultiplyIterative(x,n):
    #global s,m
    result , base = 1 , x
    while n > 0:
        if n%2 != 0:
            #m+=1
            result = result*base
        #s +=1

        n = n//2
        if n != 0 : 
            base = base*base
    return result

def SquareMultiplyRecursive(x,n):
    #global S,M
    if n == 0:
        return 1
    elif n%2 == 0:
        #S = S + 1
        return SquareMultiplyRecursive(x**2,n//2)
    else :
        #M = M + 1
        #S = S + 1
        return x*SquareMultiplyRecursive(x**2,n//2)


def naive_pow(x,n):
    i , a = 0 , 1
    while i!=n:
        a , i = a*x , i+1
    return a

#naive_pow(2,4)


def measure_time(func, x, n):
    start_time = time.time()
    func(x, n)
    return time.time() - start_time

x = 2
n_values = [i for i in range(1, 100000, 1000)]
time_naive = []
time_recursive = []
time_iterative = []

for n in n_values:
    #time_naive.append(measure_time(naive_pow, x, n))
    time_recursive.append(measure_time(SquareMultiplyRecursive, x, n))
    time_iterative.append(measure_time(SquareMultiplyIterative, x, n))

#plt.plot(n_values, time_naive, label='Naif')
plt.plot(n_values, time_recursive, label='Recursive')
plt.plot(n_values, time_iterative, label='Iterative')
plt.xlabel('n')
plt.ylabel('Temps (secondes)')
#plt.xscale('log')
#plt.yscale('log')
plt.legend()
plt.title('Comparaison des Algorithmes de Calcul de x^n')
plt.show()
