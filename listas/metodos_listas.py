lst = [2 ,3 , 4, 5, [60,80], "maria"]

#AGREGAN
lst.append("Carlos Mario") #agrega al final de la lista
print(lst)

lst.insert(4, -3) #en la posicion 4 (start 0) agrega un -3
print(lst)

lst.extend([10,100]) #agrega elementos de la lista al final de la lista original
print(lst)

lst.append([10,100]) #agrega una lista a posicion
print(lst)

#ELIMINAN
lst.pop() #si no se coloca nada se elimina el final de la lista
print (lst)

lst.pop(3) #elimina un lugar de la lista en este caso 3
print (lst)

lst.remove("Carlos Mario") #elimina una cosa de la lista si no esta sale error, consejo agregar try
print (lst)

#lst.reverse() #cambia el lugar de todo al revez lo ultimo es primero y primero ultimo
print(lst)

lst1=lst.copy() #se hace para hacer una copia de la lista anterior
lst1.pop()
print(lst)  #es lo mismo de abajo
print(lst1) #es lo mismo de arriba

lst.append(2) #agrega un 2 al final
print(lst)
print(lst.count(2)) #cuenta cuantas veces hay un 2 en la lista

print(lst.index("maria")) #da en que posicion esta lo que estoy buscando, si no esta da value error, usar try para evitar errores
#en este caso 5

lst1 = [4, 2, 99, 101, 1, 5, 6] #sobreescribe el arterior
#lst1.sort() #ordene la lista de valor acendete

def myfunc(e): #cambia estrategia de ordenmaiento
    return e % 2  #ordena por modulo 

lst1.sort(reverse=True, key=myfunc) #Ordene la lista por el resultado de la funcion
print(lst1)

lst.clear() #limpia la lista