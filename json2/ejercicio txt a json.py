import json
general={}
general['Vendedores']=[]
with open("archivo.txt","r") as archivo: #r para que lo lea, w es para escribir
    lineas=archivo.readlines() #lea todas las lineas por aparte
print(lineas)

#eliminar linea 1 = data.pop(0)

for linea in lineas[1:]:#lee las lineas desde 1
    valores_de_linea=linea.replace("\n","").split(", ")# lista de la linea 
    #quito los \n y las , 
    lista_numeros=[] #creo un diccionario lista de numeros
    for i in valores_de_linea[2:]: #convertir en numeros las ventas
        lista_numeros.append(int(i)) 
    vendedor={
        "Apellido":valores_de_linea[0], #creo la lista lineas
        "Id":valores_de_linea[1],
        "Ventas":lista_numeros
    }
    general["Vendedores"].append(vendedor)#guardo en vendedores los resultados

with open ("vendedores.json","w") as file: #que lo guarde como json
    json.dump(general,file,indent=4)

