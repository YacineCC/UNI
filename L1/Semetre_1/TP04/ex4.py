ch = input()
liste = []
while ch !='' :
	liste += [ch]
	ch = input()
petit = []
grand = []
for i in liste :
	if len(i) < 5:
		petit += [i]
	elif len(i) > 10:
		grand += [i]
			
print(liste,grand,petit)
	
