#d:\roy\origen.txt
import os
os.system('cls')
rutaorigen = input("cual archivo a procesar: ")
archlectura = open(rutaorigen, "r") #archivo desde donde toma la informacion(que exista una ubicacion es necesaria)
archdestino = open("D:\Roy\destino.txt","w")#archivo donde escribe elemento (que exita la ubicacion es innecesaria)

unalinea = archlectura.readline() #lee la primera linea de texto
while unalinea:
    print(unalinea) #muestra una linea en pantalla
    listapalabras = unalinea.split(" ") #donde encuentre un espacio considere que es un pabra(sigue siendo espacio)
    print(listapalabras)#Imprime la lista
    lineaCSV = "\t".join(listapalabras) #coloque un tabular para unir cada palabra
    archdestino.write(lineaCSV) #escribe de nuevo todo con las condiciones dadas

    unalinea = archlectura.readline() # va por otra linea
archlectura.close()#cierra lectura despues de leer
archdestino.close()#cierra el destino

print("*** fin del proceso ***")
