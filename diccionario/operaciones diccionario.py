inventario ={"manzanas":40,"bananas":312,"naranjas":132,"peras":90}
#lista claves diccionario
print(inventario.keys())

#lista valores diccionario
print(inventario.values())

#devuelve cad item
print(inventario.items())

#hay tantos valores como claves en stock
#v = valores  ,  k = keys 
for(k,v)in inventario.items():
    print("Hay",v,k,"en stock")

#verificiar si hay una clave en dicionario responde true o false
print("naranjas" in inventario) #true
print("duraznos" in inventario) #false

#limpia el diccionario inventario
inventario.clear()

