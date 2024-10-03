def euler_phi(n):
    i = 1
    phi = 0
    while i < n:
        x = n
        k = i
        while x != 0:
            k,x = x, k % x


        if k == 1:
            phi += 1

        i += 1 

    return phi

print(euler_phi(12))
        
