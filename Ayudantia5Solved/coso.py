dix = {
'carton1':[1, 2, 5, 7, 8, 10],
'carton2':[2, 5, 6, 7, 9, 10],
'carton3':[8, 1, 2, 10, 6],
'carton4':[1, 10, 3, 5, 6],
'carton5':[2, 3, 5, 6, 9, 10],
'carton6':[10, 7, 2, 5],
'carton7':[1, 2, 3, 4, 8, 10],
'carton8':[3, 4, 5, 6, 7, 9],
}

from random import*
for i in range(10):
	a = []
	for k in range(7):
		a.append(randint(1,10))
	#print list(set(a))

def fun(dic):
	new = dict()
	for llave in dic:
		for value in dic[llave]:
			if value not in new:
				new[value]=1
			else:
				new[value]+=1
	return new
	
def funprob(dic):
	new = []
	for x,y in dic.items():
		new.append((y,x))
	new.sort()
	for x,y in new:
		print y,"se repite",x,"veces"
	#print new
	return

funprob(fun(dix))
