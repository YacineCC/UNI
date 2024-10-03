from pocketgl import *
from random import *
N = int(input("Medele"))
n = 0
for i in range(N):
	a = random()
	b = random()
	if (a*a+b*b)**0.5 <= 1:
		n += 1
pi = 4*(n/N)
print(pi)
