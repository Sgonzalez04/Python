import json #requerido para que funcione

data={} #variable diccionario vacio
data["clients"]=[]#los clientes se guardan en lista clientes
data["precios"]=[]
#los nombres de los programas pyton no se pueden usar de nombre

#se guarda en  la lista de clientes un diccionario llamado clients
data["clients"].append({"first_name": 'theodoric',
                        "last_name": 'rivers',
                        "age":36,
                        "amount":1.11})
data["clients"].append({"first_name": 'Sergio',
                        "last_name": 'Silva',
                        "age":19,
                        "amount":9.54})
data["precios"].append({"precio":999,
                        "age":19,
                        "amount":4})

with open("jsonprueba.json","w") as archivo: #abra data.json
    json.dump(data,archivo,indent=2) #guarde en la misma carpeta que corre la terminal
    #indent es para que separe en el archivo todo

#load = lectura
#estritura = dump

print(data)
