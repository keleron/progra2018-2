dix = {
"libro1": {"autores":["felipe","jotaro"]   ,"ediciones":[(1,10,1998),(4,12,1990),(7,10,2008)]},
"libro2": {"autores":["okabe","rintarou"]  ,"ediciones":[(2,8,1998),(5,16,1990),(8,2,2018)]},
"libro3": {"autores":["soyunim","becil"]   ,"ediciones":[(3,4,1972),(6,10,1983),(9,1,1930)]}
}
dix2 = { # HITOS LOGROS NO SE xdxdxd
"felipe":		["Nadador profecional","piloto"],
"jotaro":		["Campeon de ping-pong","biologo marino"],
"okabe" :		["MadSCIENTISTO","Viajero en el tiempo","inventor"],
"rintaro":  ["Depresivo de vocacion", "gansta"],
"soyunim":	["Heroe de las guerras pasadas y futuras"],
"becil"  :	["Alterego", "vendedor de cuchuflis"]
}
dix3 = {
1: "Nobtubre", #mes 1 5 9
2: "Eviembre", #mes 2 6 10 
3: "Maryo"	 ,#mes 3 7 11
4: "Jugosto" ,#mes 4 8 12
}

libro = raw_input("Ingrese nombre libro: ")
print "Nombre del libro:",libro
autores = dix[libro]["autores"]
for k in autores:
	print "Autor:",k,"tiene los siguientes hitos",dix2[k]
ediciones = dix[libro]["ediciones"]
fechas = []
for m,d,a in ediciones:
	fechas.append((a,m,d))
print "La ultima edicion fue en"
print "anio:",a
print "mes:" ,m
print "dia:" ,d
print "Y el mes en el universo paralelo seria",dix3[m%4+1]


