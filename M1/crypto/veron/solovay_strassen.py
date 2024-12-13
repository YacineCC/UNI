import random
def jacobi(m, n):

    a = m
    b = n

    #while b!= 0:
    #    a,b = b, a%b

    #if a != 1:
    #    return 0
    jac = 1
    while m > 1:
        if m % 2 == 0:
            m = m//2
            if n % 8 == 3 or n%8 == 5:
                jac = -jac

        elif(m < n):
            if m % 4 == 3 and n % 4 == 3:
                jac = - jac
            m,n = n, m
            m = m % n
       
        
    return m*jac


            

#print(jacobi(10, 21))
#print(jacobi(62, 75))
#print(jacobi(62, 63))
#print(jacobi(11, 17))
#print(jacobi(23, 69))
#print(jacobi(70, 71))
#print(jacobi(67, 75))
#print(jacobi(9, 89))
#print(jacobi(68, 69))
#print(jacobi(17, 51))



def solovay_strassen(n, t):
    
    for i in range(t):
        a = random.randint(1,n)
        if (jacobi(a, n) % n) != pow(a, (n-1)//2, n):
            return 0

        

    return 1
print(solovay_strassen(2461621572185378719489232151655868788959601584166591523174513,20))
