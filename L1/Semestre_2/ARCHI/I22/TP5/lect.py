import struct
f = open("valeurs",'rb')

nombre1 = f.read(1)

nombre = struct.unpack('<b',octet)[0]
print(nombre1)

print(nombre,octet)
