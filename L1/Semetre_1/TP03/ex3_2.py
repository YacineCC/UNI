ch = input("Palindrome ? ")

i = 0
j = -1
test = False
while i < len(ch):

	if ch[i] == ch[j] :
		test = True
	i += 1
	j -=1

if test :
	print("OUI")
else :
	print("NON")
