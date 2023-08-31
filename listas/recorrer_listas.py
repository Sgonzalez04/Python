lst = [2 ,3 , 4, 5, [60,80], "maria"]

#recorrido por sus posiciones o indices
for i in range(len(lst)): #para i en el rango de la longitud de la lista
    print(lst[i], end=" - ")#recorre la lista por posicion de 0 a 5

print()

#recorrido por elementos
for elem in lst:
    print(elem, end=" * ") 