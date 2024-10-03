semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
i= 1
octo = "octobre"
calendOct18=[]
while i <= 31:
	for j in semaine:
		calendOct18 += [str(j)+' '+str(i)+' '+octo]
		i +=1
	
print(calendOct18)

	
