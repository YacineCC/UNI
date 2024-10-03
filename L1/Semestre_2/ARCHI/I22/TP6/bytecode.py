import struct
import sys
import time
from binascii import hexlify
def magic_number(filename):
	f = open(filename,'rb')
	octet = f.read(2)
	f.close()
	return struct.unpack('H',octet)[0]


def affiche_version(magic_number):
	dico = {
	20121: "Python 1.5",
	50428: "Python 1.6",
	50823: "Python 2.0",
	60202: "Python 2.1",
	60717: "Python 2.2",
	62021: "Python 2.3",
	62061: "Python 2.4",
	62131: "Python 2.5",
	62161: "Python 2.6",
	62211: "Python 2.7",
	3131: "Python 3.0",
	3151: "Python 3.1",
	3180: "Python 3.2",
	3230: "Python  3.3",
	3310: "Python 3.4",
	3350: "Python 3.5",
	3379: "Python 3.6",
	3394: "Python 3.7",
	3413: "Python 3.8",
	3425: "Python 3.9",
	}

	if magic_number in dico:
		print(dico[magic_number])
	else:
		print( "Version inconnue" )
def set_magic_number(valeur, filename, filenameout=None):
	f = open(filename,'rb')
	val = struct.pack('H', valeur)
	f.seek(2)
	x = f.read()
	f.close
	if not filenameout:
		f = open(filename,'wb')
		f.write(val)
		f.write(x)
		f.close
	else:
		f = open(filename,'rb')
		fo = open(filenameout, 'wb')
		fo.write(val)
		fo.write(x)
		fo.close()
		f.close

def affiche_date(filename):
	f = open(filename,'rb')
	f.seek(8)
	octet = f.read(4)
	date = struct.unpack('<I',octet)[0]
	f.close()
	date = time.ctime(date)
	print(date)
	
def affiche_sous_structure(filename):
	f = open(filename,'rb')
	f.seek(42)
	octet = (f.read(4))
	return struct.unpack('<I',octet)[0]
	

	
def affiche_structure(filename):
	print ("Magic number: ",magic_number(filename),"- ",end="")
	affiche_version(magic_number(filename))
	print("Date de création: ",end="")
	affiche_date(filename)
	a = affiche_sous_structure(filename)
	print(f"Partie code: adresse=42, longeur={a} octets")
	

	

if __name__ == "__main__" :
	#set_magic_number(3413,sys.argv[1],)
	print(magic_number(sys.argv[1]))
	affiche_version(magic_number(sys.argv[1]))
	affiche_structure(sys.argv[1])
	
