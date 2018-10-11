def get_pos(a,b): #no es parte de la respuesta 
	if b not in a:
		return -1
	return a.find(b)

def get_palabra(a,b):
	pos = get_pos(a,b)
	if pos == -1:
		return -1 
	return a[:pos] + a[pos+len(b):]

#Esto es la B
h = True
texto = ""
key = raw_input("Ingrese clave: ")
while (h):
	a = raw_input("Ingrese palabra: ")
	if a!='out':
		if get_palabra(a,key)!=-1:
			texto += get_palabra(a,key) + " "
	else:
		h = False
print "Mensaje oculto:",texto
		


