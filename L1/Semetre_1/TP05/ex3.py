def som_div_propres(n):
	i = 1
	divs = 0
	while i < n:
		if n % i == 0:
			divs += i
		i += 1
	return divs

def est_parfait(n):
	if som_div_propres(n) == n:
		return True
	else :
		return False
		
def affiche_parfait(k):
	for i in range(1,2**k+1):
		if est_parfait(i):
			print(i)

		

def est_presque_parfait(n):
	if som_div_propres(n) == n-1:
		return True
	else :
		return False
def affiche_presque_parfait(k):
	for i in range(1,2**k+1):
		if est_presque_parfait(i):
			print(i)
def amicaux(n,m):
	if som_div_propres(n) == m and som_div_propres(m) == n:
		return True
	else :
		return False
def affiche_amicaux(k):
	i = 0
	while i <= 2**k:
		j = 0
		while j <= 2**k :
			if amicaux(i,j):
				if i != j:
					print(i,j)
			j += 1
		i += 1 
