def sous_groupe_gen_mult(a,n):
	y = a
	gens = []
	while a%n != 1:
		gens += [a]
		a = (a*y) % n
	gens += [a]
	return gens

print(sous_groupe_gen_mult(3,10))
