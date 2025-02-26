def spn(m, key, sbox, permutation, n):
	w0 = m
	k0 = key
	print(f'm : {bin(m)[2::]}')
	print(f'k{0} : {bin(k0)[2::]}')
	print(f'Sbox : {sbox}')
	print(f'Permutation : {permutation}')
	wi = w0
	for i in range(n):

		# Xor avec la clef (avec décalage de 4 bits sur la clef)
		ki = (k0 & (((1<<16) - 1) << (16 - (4 * i)))) >> (16 - (4 * i))
		ui = wi ^ ki


		# Application de la sbox
		vi = sbox_transform(sbox, ui)
		
		# Permutation
		if i < n- 1:

			j = 0
			wi = 0
			vi2 = vi
			while vi2 > 0:
				
				wi |= (vi2 & 1) << permutation[j]			
				j += 1
				vi2 = vi2 >> 1
		else:
			wi=vi
			
			
		


		print("k",i," :", "{0:16b}".format(ki),sep="")
		print(f'k{i} : {"{0:16b}".format(ki)}')
		#print(":016b".format(bin(ki)))
		print(f'v{i} : {"{0:16b}".format(vi)}')
		print()
		print(f'w{i+1} : {"{0:16b}".format(wi)}')
	
	print(f'w{4} : {bin(wi)[2::]}')
	
# Xor avec la clef (avec décalage de 4 bits sur la clef)
	k4 = k0 & ((1<<16) - 1) 
	ui = wi ^ k4
	print(f'k4 : {bin(k4)[2::]}')

	
	
	return bin(ui)[2::]



def sbox_transform(sbox, u):
	v = 0
	j = 0
	while u > 0:

		v |= sbox[(u & ((1<<4) - 1))] << (4*j)
		u = u >> 4
		j += 1
	
	return v


def permutation_transform(permutation, v):
	w = 0
	j = 0
	while v > 0:
		w |= v & 1


entree = 0b0010011010110111

cle = 0b00111010100101001101011000111111
sbox = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
permut = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]

print(f'c : {spn(entree, cle, sbox, permut, 4)}')
	