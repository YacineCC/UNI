from pilefile import *

P = pile_init()

empiler(P,5)
empiler(P,12)
empiler(P,4)

def pile_affiche(P):
	p = pile_init()
	maxi = 0
	while not(pile_vide(P)):
		element = depiler(P)
		if element > maxi:
			maxi = element
		empiler(p,element)
	taille = 3 * len(str(maxi))
	ligne = '-' * taille
	print(ligne)
	while not(pile_vide(p)):
		element = depiler(p)
		espace = ' ' * (taille-len(str(element))-3)
		print('|'+espace+str(element)+' |')
		print(ligne)
	


pile_affiche(P)


def file_affiche(F):
	f = file_init()
	taille = 0
	while not(file_vide(F)):
		element = defiler(F)
		taille+=len(str(element))+3
		enfiler(f,element)
	ligne = '-' * (taille+1)
	print(ligne)
	while not(file_vide(f)):
		element = defiler(f)
		print('| '+str(element)+' ',end="")
	print('|')
	print(ligne)

empiler(P,5)
empiler(P,12)
empiler(P,4)

file_affiche(P)	
