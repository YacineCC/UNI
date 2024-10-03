from pocketgl import *
import random as r

tab3 = [0]*13
init_window('Histogramme',900,700)
current_color('red')

for i in range(1,10001):
	de1 = r.randrange(1,7)
	de2 = r.randrange(1,7)
	a = de1 + de2
	tab3[a] += 1/3	
			
i = 2
j = 15

while i < len(tab3):
	box(j,tab3[i],j+70,-tab3[i])
	i += 1
	j += 80
			
main_loop()

