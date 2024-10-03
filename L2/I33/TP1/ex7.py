def som_div_propres(n):
    if n == 1:
        return 0
    som = 1
    i = 2
    while i < ((int(n**0.5))+1):
        
        if n % i == 0:
            som += i
            if i != n/i:
                som += n // i
        i += 1
    return som
print(som_div_propres(84))
print(som_div_propres(42))
print(som_div_propres(88882279))
print(som_div_propres(36))
print(som_div_propres(1))
print(som_div_propres(163986456))
print(som_div_propres(12))
print(som_div_propres(32))
print(som_div_propres(192869380))
print(som_div_propres(90))
