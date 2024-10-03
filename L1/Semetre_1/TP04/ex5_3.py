semaine=["jeudi","vendredi","samedi","dimanche","lundi","mardi","mercredi"]
i= 1
octo = "octobre"
calendNow=[]
while i <= 30:
	for j in semaine:
		calendNow += [str(j)+' '+str(i)+' '+octo]
		i +=1
	

print(calendNow)

	
