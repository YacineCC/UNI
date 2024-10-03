def puiss(x,y,n):
    z = 1
    while y > 0:
        if ((y & 1) > 0):
            z = (z*x) % n
        x = (x*x) % n
        y >>= 1
    return (z)


print(puiss(10,196,18))
print(puiss(16,147,16))
print(puiss(15,161,15))
print(puiss(16,186,24))
print(puiss(13,1000000000000000,15))

print(puiss(16,147,19))
print(puiss(11,161,19))
print(puiss(10,132,17))

print(puiss(16,188,21))
print(puiss(17,130,18))


