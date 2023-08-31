# D:\roy\origen.txt este es para windows
import os

os.system("cls")
rutaOrigen = input("en que ubicacion esta el archivo")
archivo = open(rutaOrigen, "r")  # r lectura de donde lo lee
destino = open("D:\Roy\destino.doc", "w")  # w escritura donde lo escribe

line = archivo.readline()  # lee la primera linea del archivo
while linea:
    print(linea)
    listaPalabras = linea.split("")  # la linea la separa fromando lista
    print(listaPalabras)  # imprime la lista seguida
    lineaCSV = "\t".join(listaPalabras)  # une la lista con tabulador
    destino.write(lineaCSV)  # escriba lo que salio en la linea csv

    linea = archivo.readline()  # procesar o escribir en el archivo de destino
archivo.close()  # cierra los archivos
destino.close()

print("***FIN DEL ARCHIVO***")
