list=[]
somme=0
inp = int(input())
while inp != 0:
	list += [inp]
	somme += inp
	inp = int(input())
print(len(list),somme)
