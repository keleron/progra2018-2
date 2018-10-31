from random import*
dix = {
"tipo1":["+10","+12","+14"],
"tipo2":["+11","+12","+13"],
"tipo3":["+14","+18","+19"],
"tipo4":["+10","+12","+13"]
}

def fun(a,b,dic):
	comunes = []
	for k in dic[a]:
		if k in dic[b]:
			comunes.append(k)
	return comunes