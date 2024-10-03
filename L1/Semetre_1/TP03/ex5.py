ham = input("Chiffrement (E)ncode ou Dechiffrement (D)ecode ? ")
i = 0
encode = ''
trans = ''
if ham == "E":
	while i < len(ham):
		trans = ord(ham[i])
		print(trans)
		encode += chr(trans + 1)
		i += 1
print(encode)
		
	
