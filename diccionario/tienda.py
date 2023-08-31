tienda = {"item":['lapiz','carpeta','marcador'],
          "cantidad" : [3, 10, 5],
          "valor": [3.50,4.25,7.85]}

#valor es una llave ya que sirve para acceder a otros

#marcador valor 7.85
#print(tienda["valor"][2])
# print(tienda.get("valor")[2]) #get devuelve una lista
# print(tienda.fromkeys(["proveedor","Mongol"],"pencil")) #provedor y mongol tienen como resultado pencil
# print(tienda.items()) #escribe todos los items
# print(tienda.keys()) #escribe todas las llaves 
# print(tienda.values()) #devuelbe una lista con cada uno de los valores

# tienda["proveedor"] = ["mongol", "norma", "pencil"]
# print(tienda.pop("proveedor"))#permite elminar una llave

# tienda.setdefault("proveedor")#busca si hay una llave y si no esta agrega lo que tiene
# print(tienda)

#recorridos por valor
for k in tienda.keys():#guarda las opciones de valores de keys en k
    print(tienda[k])

print()


#recorrido por diccionario
for elem in tienda:
    print(tienda[elem])

print()

#recorrido por items
for k,v in tienda.items(): #recorre todo y le asigna a k llas llaves y a v los resultados
    print(k, "-->", v) #luego imprime lo de k y v mostrandolos bien
