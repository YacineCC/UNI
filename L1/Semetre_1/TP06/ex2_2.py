from pocketgl import *
import random as r
init_window("Histogramme",1000,1000)
current_color("red")
couple = ()
c1,c2,c3,c4,c5,c6 = 0,0,0,0,0,0
cpt1 = 0
for i in range(1,10001):
	a = r.randrange(1,7)
	b = r.randrange(1,7)
	couple += ([a,b],)
	if a == 1:
		b = r.randrange(1,7)
		cpt1 += 1
		box(10,cpt1,50,cpt1)
		
main_loop()	
print(couple)
