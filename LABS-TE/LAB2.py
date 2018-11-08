villanos = {
"chanchoman":('muy peligroso','hurto simple'),
"eviltron" : ('intergalactico','golpear ancianos'),
"iwanator" : ("extremo","reprobar alumnos"),
"el profe": ("extremo","reprobar alumnos"),
"gato juanito": ("extremo","chamullero")
}
capturados = [
("san","eviltron"),("san","iwanator"),("maipu","gato juanito"),
("pinta","chanchoman"),("san","el profe")
]
peligrosidad = ["piece","muy poco","usual","muy peligroso","extremo","intergalactico"]

def delitos_frecuente(ciudad,villanos,capturados):
    new = dict()
    for lugar,nombre in capturados:
        if lugar==ciudad:
            if villanos[nombre][1] in new:
                new[villanos[nombre][1]]+=1
            else:
                new[villanos[nombre][1]]=1
    max = 0
    for delito,cantidad in new.items():
        if cantidad>max:
            max = cantidad
            cosa = delito
    return cosa

def mas_buscados(villanos,capturados,peligrosidad):
    ls = []
    for lu,no in capturados:
        for k in range(len(peligrosidad)):
            if villanos[no][0] == peligrosidad[k]:
                peligro_num = k
        a = (lu,peligro_num,no)
        ls.append(a)
    new = dict()
    for lugar,peli,nombre in ls:
        if lugar not in new:
            new[lugar]=[nombre,peli]
        else:
            if new[lugar][1]<peli:
                new[lugar][1] = peli
                new[lugar][0] = nombre
    return new

print "===============DELITOS FRECUENTES==============="
print delitos_frecuente("san",villanos,capturados)
print "===============MAS BUSCADOS      ==============="
print mas_buscados(villanos,capturados,peligrosidad)
