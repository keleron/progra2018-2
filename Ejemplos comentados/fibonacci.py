n = int(raw_input("Ingrese N:")) #Pide ingresar un numero cualquiera N y lo castea a entero
a = 0 #Primer termino de fibo
b = 1 #Segundo termino de fibo
while n > 0: #Mientras el numero N sea mayor a 0 seguirá en el bucle
  print a #Muestra por pantalla el termino actual
  a = b   #El termino actual pasa al siguiente 
  b = a+b #El siguiente pasa a a ser la suma entre el mismo y el anterior
  n-=1    #Se le esta 1 al numero N ingresado

'''VERSION ALTERNATIVA (REALMENTE ES LO MISMO PERO HAY ASIGNACIONES EN UNA MISMA LINEA POR COMODIDAD)
n = int(raw_input("Ingrese N:")) //Pide ingresar un numero cualquiera N y lo castea a entero
a , b = 0 , 1 
while n > 0:
  print a
  a , b = b , a+b
  n-=1
'''
