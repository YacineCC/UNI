import random as rd

def init_ram_list(taille):
	return [0]*taille
	


RAM = init_ram_list(16)
print(RAM)

def fill_ram_random(ram,N):

	"""On remplace N valeurs dans le tableau par un entier aléatoire entre 1 et 255, avec à chaque fois une position aléatoire entre 
	l'indice 0 et la longueur du tableau - 1  """
	i = 0
	indices = []
	while i < N:
		aux = rd.randrange(len(ram))
		if not aux in indices:
			ram[aux] = rd.randrange(1,256)
			i += 1
			indices += [aux]
	return ram


RAM = fill_ram_random(RAM,5)
print(RAM)

def fill_ram_place(ram,N):
	i = 0
	indices = []
	while i < N:
		aux = rd.randrange(len(ram))
		if not aux in indices:
			ram[aux] = aux
			i += 1
			indices += [aux]
	return ram
	
RAM = init_ram_list(16)

RAM = fill_ram_place(RAM,5)
print(RAM)


def get_value_list(ram,adresse):
	return ram[adresse]


def init_ram_dict(taille):
	dico = {'taille' : taille}
	return dico
	
RAM = init_ram_dict(16)
print(RAM)


def fill_ram_random_dict(ram,N):
	i = 0
	indices = []
	while i < N:
		aux = rd.randrange(ram['taille'])
		if not aux in indices:
			ram[aux] = rd.randrange(1,256)
			i += 1
			indices += [aux]
			
	return ram
	
RAM = fill_ram_random_dict(RAM,5)
print(RAM)

def fill_ram_place_dict(ram,N):
	i = 0
	indices = []
	while i < N:
		aux = rd.randrange(ram['taille'])
		if not aux in indices:
			ram[aux] = aux
			i += 1
			indices += [aux]
	return ram
	
RAM = init_ram_dict(16)
RAM = fill_ram_place_dict(RAM, 5)
print(RAM)

def get_value_dict(ram,adresse):
	if adresse > ram['taille']:
		return "Erreur: adresse invalide"
	else:
		return ram.get(adresse,0)


def is_in(mem_asso,mot):
	tup = ()
	booleens = []
	j = 0
	for i in mem_asso:
		if i != mot:
			booleens += [False]
		else:
			booleens += [True]
			indice = j
		j += 1
	if True in booleens:
	
		tup = ('HIT',booleens,indice)
	else:
		tup = ('Miss',booleens,None)
	return tup
	
M = [4, 1, 2, 0]
print(is_in(M,3))
print(is_in(M,1))
print(is_in(M,0))

def get_value(mem, idx):
	if mem[idx]['ok'] == True:
		return M[idx]
	else:
		aux = M[idx]
		aux['data'] = None
		return aux

M = [{'ok': True, 'data': 0x44}, {'ok': False, 'data': 0xFF},
         {'ok': True, 'data': 0x22}, {'ok': True, 'data': 0x99}]
         
print(get_value(M,3))

print(get_value(M,1))
	

mem_associative = [4, 1, 2, 0]
mem_classique = [{'ok': True, 'data': 0x44}, {'ok': False, 'data': 0xFF},
                     {'ok': True, 'data': 0x22}, {'ok': True, 'data': 0x00}]


def in_cache(mem_associative, mem_classique, adresse):
	return(is_in(mem_associative,adresse)[0],get_value(mem_classique,adresse)['data'])

print(in_cache(mem_associative, mem_classique, 3))
print(in_cache(mem_associative, mem_classique, 1))
print(in_cache(mem_associative, mem_classique, 2))




