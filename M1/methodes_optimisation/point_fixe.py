

#F = lambda x : x**3 - 1
F = lambda x, a : 1/x - a

a = 2
#omega = -1/3
omega = -1/a**3

print(omega)

G = lambda t : t + omega * F(t, a)

x = 0.2

c = 0
while abs(F(x, a)) > 1e-20 :
    x = G(x)
    c += 1
    print(x)
    print(c)
