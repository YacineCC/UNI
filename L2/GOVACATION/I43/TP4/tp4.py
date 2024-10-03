def make_log_table_Z29():

	L = [0]*29
	L[0] = -1
	i = 2
	j = 1
	while(i%29 != 1):
		
		L[i%29] = j
		j += 1
		i <<= 1
	
	return L

print(make_log_table_Z29())




def inverse_Z29(x):
	
	table_log = make_log_table_Z29()
	return(1<<(28-table_log[x]))%29


print(inverse_Z29(3))
