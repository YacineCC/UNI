def note(anglais, latex, IA, GL, IG):

	res = (anglais*2 + latex*2 + IA*9 + GL*8 + IG * 9) / (2+2+9+8+9)
	return res

anglais = 20
latex = 20
IA = 0
GL = 10
IG = 10

print(note(anglais, latex, IA, GL, IG))

