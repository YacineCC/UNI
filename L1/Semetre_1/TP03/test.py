T = input("Chiffrement (E)ncode ou Dechiffrement (D)ecode ? ")
cle = int(input("Cle de chiffrement ? "))
txt = input("Texte ? ")
i = 0
encode = ''
trans = ''

if T == "E" :
	while i < len(txt):
		if txt[i] == ' ':
			encode += txt[i]
			
		else :
			trans = ord(txt[i]) 
			if trans + cle > 122 :
				trans = (trans - 26) + cle 
				encode += chr(trans)
			else :
				encode += chr(trans+cle)
		i += 1
	print(encode)
elif T == "D" :
	while i < len(txt):
		if txt[i] == ' ':
			encode += txt[i]
			
		else :
			trans = ord(txt[i]) 
			if trans - cle < 97 :
				trans = (trans + 26) - cle
				encode += chr(trans)
			else :
				encode += chr(trans-cle)
		i += 1
	print(encode)
else : 
	print("NON")
		
	
