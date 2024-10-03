def sous_groupe_gen_add(a,n):
	y = a
	add = [a]
	while (a%n) != 0:

		a = (a + y) % n
		add += [a]
		
	
	return add

print(sous_groupe_gen_add(4,10))
		
		
		
		
