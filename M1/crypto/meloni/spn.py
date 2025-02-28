def spn_chiffre(m, key, sbox, permutation, nb_tours, subset_key_size):
		key_root = int(subset_key_size ** 0.5)
		w0 = m
		k0 = key
		print(f'm : {bin(m)[2::]}')
		print(f'k{0} : {bin(k0)[2::]}')
		print(f'Sbox : {sbox}')
		print(f'Permutation : {permutation}')
		wi = w0
		for i in range(nb_tours):

			# Xor avec la clef (avec décalage de 4 bits sur la clef)
			ki = (k0 & (((1<<subset_key_size) - 1) << (subset_key_size - (key_root * i)))) >> (subset_key_size - (key_root * i))
			ui = wi ^ ki


			# Application de la sbox
			vi = sbox_transform(sbox, ui)
			
			# Permutation
			if i < nb_tours- 1:

				wi = permutation_transform(permutation, vi)
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
		k4 = k0 & ((1<<subset_key_size) - 1) 
		ui = wi ^ k4
		print(f'k4 : {bin(k4)[2::]}')

		return ui


def spn_dechiffre(c, key, sbox_inv, permutation_inv, nb_tours, subset_key_size):
    key_root = int(subset_key_size ** 0.5)
    k0 = key
    w4 = c

    # XOR avec la dernière clé
    k4 = k0 & ((1<<subset_key_size) - 1) 
    wi = w4 ^ k4



    for i in range(nb_tours - 1, -1, -1):
        # Annuler la permutation sauf au dernier tour
        if i < nb_tours - 1:
            vi = permutation_transform(permutation_inv, wi)
        else:
            vi = wi
        
        # Annuler la SBox
        ui = sbox_transform(sbox_inv, vi)

        # Calculer la clé du tour et annuler le XOR
        ki = (k0 & (((1<<subset_key_size) - 1) << (subset_key_size - (key_root * i)))) >> (subset_key_size - (key_root * i))
        wi = ui ^ ki

    return wi


		


def sbox_transform(sbox, u):
	v = 0
	j = 0
	while u > 0:

		v |= sbox[(u & ((1<<4) - 1))] << (4*j)
		u = u >> 4
		j += 1
	
	return v


def permutation_transform(permutation, v):
	j = 0
	w = 0
	while v > 0:
		
		w |= (v & 1) << permutation[j]			
		j += 1
		v = v >> 1
	return w


entree = 0b0010011010110111

cle = 0b00111010100101001101011000111111
sbox = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
sbox_inv = [14, 3, 4, 8, 1, 12, 10, 15, 7, 13, 9, 6, 11, 2, 0, 5]

permut = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]
permut_inv = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]
c = spn_chiffre(entree, cle, sbox, permut, 4, 16)

print(f'm : {bin(entree)[2::]}')
print(f'c : {bin(c)[2::]}')
print(f'm : {bin(spn_dechiffre(c, cle, sbox_inv, permut_inv, 4, 16))[2::]}')



#permut_inv = [0, 4, 2, 1, 12, 10, 15, 7, 13, 9, 6, 11, 2, 0, 5]

def table_biais(sbox):
	n = len(sbox)
	table = []
	for a in range(n):
		tmp = []

		for b in range(n):
			cpt = 0 
			for x in range(n):
				ax = a & x
				by = b & sbox[x]
				cpt += 1 - ((ax ^ by).bit_count() & 1) 
				#table[j] += 1 - ((el & j).bit_count() & 1)
				#table[j] = (table[j] / (1 << n)) - 1/2
			tmp += [cpt / (1 << n) - 1/2]
		#print(tmp)
		table += [tmp]
	
	return table

#table_biais(sbox)
print(table_biais(sbox))

		

#for m in range(1 << 16):
#	for k in range(1 << 16):
#		spn(m, y, sbox, permut, 4)