h = True
n = 0
pares = 0
while (h):
	cadena = raw_input("Ingrese cadena:")
	c = 0
	num = 0
	if len(cadena)>8 or len(cadena)<8:
		h = False 
	while(c<len(cadena)):
		if cadena[c] not in "01":
			h = False
			print "Invalido"
		c+=1
	c = 0
	if (h):
		n += 1
		if cadena[len(cadena)-1]=="0":
			pares += 1
		while(c<len(cadena)):
			if cadena[c]=="1":
				num += 2**(len(cadena)-c-1)
			c+=1
		print "suma:",num 
print "Total  :",n 
print "Impares:",n-pares
print "Pares  :",pares