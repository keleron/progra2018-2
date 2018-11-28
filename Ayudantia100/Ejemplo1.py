
"""TEXTO INICIAL
linea1	NO SE ECHEN
linea2	EL RAMO
"""

file = open("textito.txt","a") #Agrega texto
file.write("\nlinea3 POR FAVOR NO")
file.close()

"""TEXTO HASTA ACA
linea1	NO SE ECHEN
linea2	EL RAMO
linea3 por favor no
"""

file = open("textito.txt","r") #Abrir para lectura
print "=========MAL PRINTEO==========="
for line in file:
	print line
file.close()
"""
EN ESTA PARTE VERAN QUE EL FOR PRINTEA CON UN SALTO DE LINEA ADICIONAL. 
ESTO ES DEBIDO A QUE CUANDO LEEN UNA LINEA TIENEN TODOS LOS CARACTERES OCULTOS QUE NORMALMENTE NO VEMOS 
PRIMERA LINEA VENDRIA SIENDO = "linea1	NO SE ECHEN\n" donde \n representa los saltos de linea 
Y PARA ELLO TIENEN LA SIGUIENTE FUNCION QUE ELIMINA TODO ESO
"""
print "========BUEN PRINTEO==========="
file = open("textito.txt","r")
for line in file:
	print line.strip()
file.close()

file = open("textito.txt","w")
file.write("SOBRESCRIBIENDO TODO")
file.close()