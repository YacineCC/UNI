ch = input("Palindrome ? ")

i = 0
test = False
bop = ''
while i < len(ch):
	if ch[i] != ' ':
		bop += ch[i]
		
		if bop[::] == bop[::-1] :
			test = True
		else :
			test = False			
	i += 1

if test :
	print("OUI")
else :
	print("NON")
