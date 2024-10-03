from pocketgl import *
RGV = (0,0,0)
lines = (0,0,0,0,10)
init_window('spoonge bobe', 500, 500)
i = 0
cool = 0
while i <= 500 and cool < 255:
	current_color(cool,cool,cool)
	cool += 1
	line(0,i,500,i,10)
	i += 1
main_loop()
