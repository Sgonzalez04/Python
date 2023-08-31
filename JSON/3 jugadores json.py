import json

cant=int(input("ingrese la cantidad de veces que se repite la lista:"))
data={} #variable diccionario vacio
data["jugadores"]=[]#los clientes se guardan en lista clientes

for i in range (1, cant+1):
    nom=input("ingrese nombre: ")
    edad=input("ingrese edad: ")
    peso=input("ingrese su peso: ")

    data["jugadores"].append({"Nombre":nom,
                            "Edad": edad,
                            "Peso":peso})


with open("/media/spukN01-004/SERGIO/Programacion/Pyton/JSON/ jugadores.json","w") as archivo:
    #se colocan las cordenadas a guardar

    json.dump(data,archivo,indent=2)

print(data)
