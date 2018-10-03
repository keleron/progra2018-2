def costo(x):
	if x<=8*60:
		return 0
	return 5000*((x-8*60)/60+1)
	
def distancia(x1,y1,x2,y2):
	return ((x1-x2)**2+(y1-y2)**2)**(0.5)

def ppunto(x1,y1,x2,y2):
	return x1*x2+y1*y2
	
def recto(x1,y1,x2,y2,x3,y3):
	vector1x = x2-x1
	vector1y = y2-y1
	vector2x = x3-x1
	vector2y = y3-y1
	p = ppunto(vector1x,vector1y,vector2x,vector2y)
	if p==0:
		return True
	return False
	
def contar(n):
	a = 1
	while (a!=n):
		print a
		a +=1
	return 
	
def multiplos(n):
	a = 1
	while (a<=n):
		if (n%a==0):
			print a
		a+=1
	return
	
def letraporletra(n):
	a = 0
	b = len(n)
	while (a<b):
		print n[a]
		a+=1
	return
	
def fibo(n):
	prev   = 0
	actual = 1
	aux    = 1
	count  = 2
	while (count<n):
		aux = actual
		actual = prev+actual
		prev = aux
		count += 1
	return actual
		
def siete(a,b):
	if (a+b==7):
		return True
	return False

def comb(n):
	a = 1
	b = 1
	while (a<=7):
		while (b<=7):
			if (siete(a,b) and a!=n and b!=n ):
				print "Suman 7: ",a,b
			b+=1
		b=1
		a+=1
	return 
	

	
	

	

