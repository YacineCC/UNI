def dechiffre(cryptogramme,k):
	
	clair = ""
	i = 0
	while(i < len(cryptogramme)):
		
		if(cryptogramme[i] != " "):
			clair += chr((((((ord(cryptogramme[i])-97) - k[1])*k[2])%26)+97))
		
		else:
			clair += " "
		
		i += 1
	
	return clair

def analyse_freq(cryptogramme):
	dico = {}
	dico["é"] = "e"
	dico["è"] = "e"
	dico["ê"] = "e"
	dico["ë"] = "e"
	dico["à"] = "a"
	dico["â"] = "a"
	dico["ä"] = "a"
	dico["ô"] = "o"
	dico["ö"] = "o"
	dico["ï"] = "i"
	dico["î"] = "i"
	dico["ç"] = "c"
	dico["!"] = ""
	dico["."] = ""
	dico["?"] = ""
	dico[","] = ""
	dico[";"] = ""
	dico[":"] = ""
	dico[" "] = ""

	cryptogramme = cryptogramme.lower()
	cryptogramme1 = ""
	i = 0
	while(i < len(cryptogramme)):
		if(cryptogramme[i] in dico.keys()):
			cryptogramme1 += dico[cryptogramme[i]]
		else:
			cryptogramme1 += cryptogramme[i]
		
		i += 1
	freq = {}
	for i in range(ord('a'),ord('z')+1):
		freq[chr(i)] = 0
	i = 0
	maxi1 = 0
	lettremax1 = 'a' 
	while(i < len(cryptogramme1)):
		freq[cryptogramme1[i]] += 1
		if(freq[cryptogramme1[i]] > maxi1):
			lettremax1 = cryptogramme1[i]
			maxi1 = freq[cryptogramme1[i]]
		i += 1
	
	for i in range(ord('a'),ord('z')+1):
		freq[chr(i)] = 0
	i = 0
	maxi2 = 0
	lettremax2 = 'a'
	while(i < len(cryptogramme1)-1):
		
		if(cryptogramme1[i] == lettremax1):
			freq[cryptogramme1[i+1]] += 1
			if(freq[cryptogramme1[i+1]] > maxi2):
				maxi2 = freq[cryptogramme1[i+1]]
				lettremax2 = cryptogramme1[i+1]
		i += 1
			
	pourcentage1 = round(((maxi1/len(cryptogramme1)) *100),2)
	pourcentage2 = round((maxi2/maxi1 *100),2)
	
	return [lettremax1, maxi1, str(pourcentage1)+'%', lettremax2, maxi2, str(pourcentage2)+'%']

cryptogramme = ",hdyj,yiedqr,liedbdy,ydv,hhdy'jeoi,hhderuudddlydv,hhdzgdyydv,hhddyj,ygreeidbri'ldlvjlydldydetidltdqr'dyldytdb'j,',dlrihdlnjw,yjeylj,uj,deyldb'ruded'zgdbdetjey.iekri'.tdldvdedudeyldy'jeadlgruudegd'deyjldb'rti,'dztdlbd'lreedlt,lbj'i'deyuclyd',dildudeytjelhjqr'dydybd'lreededlduwhj,ygrub'det'dgdoi,ldbjllj,yzhjbdi'lm,elyjhhjtjelhjv,hhddyhdladelgruudegd'deyjdv,yd'hdlpredlwr,lddlzhdljiyr',ydlhrgjhdldeoidyd'deyli'hdlt,lbj',y,reluj,lhdl'dlihyjylqi'deyuj,a'dlzgdbdetjey.iekdiedtdydgy,vderuuddynjedyj,ytdyd'u,edj'dlrit'dhduclyd'dz,hbjlljtdlkri'ljdsbhr'd'hjqr'dy.gnd'gnjeytdl,et,gdlbri'grub'det'dgdoi,ldbjllj,yzljbd'ldvd'jegdq,e,ybj'br'yd'ldlq'i,yldy,htdgriv',yieda'ryydgjgnddtjelhdlb'rqretdi'ltdhjqr'dyzhr'loim,hdey'jtjelhja'ryyd.,hqiygnroidbj'gdoim,hv,ytdldy'jeadlg'djyi'dlhiu,edildlqhryyjeytjelhmj,'zgmdyj,ydhhdloi,dyj,dey'dlbreljwhdltdlt,lbj',y,rel.dhhdljvj,deygjbyi'dtdlniuj,elbri'lmdeeri'','zdynjejbbdhjhdljiyr',ydldy,hl'dill,'deyjljivd'hdlbd'lreedlgjbyi'ddlzhjv,hhddyj,ydeq,edebj,s.uj,lhdlrivde,'tdgdyydjvdeyi'd'dlyd'ja'jvdjkjuj,ltjelhmdlb',ytmdynje"


print(analyse_freq(cryptogramme))
