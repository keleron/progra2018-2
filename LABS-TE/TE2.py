from pprint import*

asignacion = { 
'p1':['te2','lab1','lab3'] ,
'p2':['te1','te3','lab2'] ,
'p3':['te2','lab1','te3','lab3'] ,
'p4':['te1','lab2']
}
entregas = [
('p1','lab1'),
('p2','te1'),
('p2','lab2'),
('p2','te3'),
('p3','lab1'),
('p1','lab3'),
('p3','te2')
]
def generar_reporte(asignacion,entregas):
	lista2 = []
	for key in asignacion:
		for act in asignacion[key]:
			lista2.append((key,act))
	new = dict()
	for prof,act in lista2:
		new[act]={}
		new[act]["cumple"] = []
		new[act]["no cumple"] = []
	for tupla in lista2:
		prof,act = tupla
		if tupla in entregas:
			new[act]["cumple"].append(prof)
		else:
			new[act]["no cumple"].append(prof)
		
	return new
			
pprint(generar_reporte(asignacion,entregas))