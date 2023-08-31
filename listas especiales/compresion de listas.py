import math

numeros=[ 1, 4, 9, 16, 25]

#-----1-----
#raices =[int(math.sqrt(x)) for x in numeros]
#la lista interna es asignada a la variable cuando todos los elementos han sido procesados
#recorrer la lista numeros y se le coloca un alias de x, y para cada uno se hace math.sqrt(x)

#for n in numeros: #recorrer listado de numeros
##    #a raices agrega elementos(Apend) convierte en enteros con math saca raices(sqrt)

#print(raices)


#-----2------
# for x in numeros = recorrido para cada uno de los elementos como x
# asgnar x como elemento a la nueva lista si es mayor a 10
# si es menor a 10 se coloca como *
#v=[x if (x>10) else "*" for x in numeros]

#-----3-----
#iskokrum2010 separa cada uno  y lo convierte en c
#a c cada uno lo convierte en mayuscula
#l=[c.upper() for c in "iskokrum2010"]
#print(l)

#-----4-----
#for l in "murcialago" = recorrer cada letra en la palabra murcielago
#coloca l es "aeiou" y lo escribe
#sino coloca "*"
#a=[l if l in "aeiou" else "*" for l in "murcialago"]
#print(a)