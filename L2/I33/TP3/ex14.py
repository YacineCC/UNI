def is_of_order_mult(a,t,n):
    
    i = 2
    while i <= int(t**0.5)+1:
        if ((t % i == 0) and ((pow(a,i,n) == 1) or(pow(a,t//i,n) == 1))):
            return False
        i += 1

    return pow(a,t,n) == 1

print(is_of_order_mult(68,65,97))
