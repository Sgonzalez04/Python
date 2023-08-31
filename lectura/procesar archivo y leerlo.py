# cada linea de un archivo de texto llamado "datos.txt" contiene el nombre del mes y una cantidad variable
# de datos numericos correspodiendes a las ventas del respectivo mes.
# elabore un progrma python que lea esta informacion y escriba el promedio de ventas al final de cada linea
# precedido por la marca "**". se debe guardar el archivo actualizado.

import os

os.system("clear")  # clear para borrar en linux
# para ubicar el archivo siempre copiar ruta.


def promedio(ventasmes):
    # cantidad = len(ventasmes)
    # promed = sum(ventasmes) / cantidad
    return 2.5  # promed


misdatos = open(
    "lectura/datos.txt", "r+"
)  # r+ para que sea lectura y escritura (no crea ni sobreescribe)
unalinea = misdatos.readline()  # lee que hay en el archivo mis datos

lineas_actualizadas = []
while unalinea:
    linea_Actualizada = []
    # print(unalinea)#imprime una linea
    lista = unalinea.strip().split(",")  # lista de datos de lo que hay en una linea
    # strip borra los espacios y split los convierte en lista se separa con m

    mes = lista[0]  # contiene el mes ya que es el primero
    ventasmes = lista[1:]
    ventasmes = [
        int(valor) for valor in lista[1:]
    ]  # ventas del mes desde el indice 1 hacia adelante
    # se muestran en enteros
    # print(mes,ventasmes) #imprime ventas mes
    prom = promedio(ventasmes)
    ultimo = "**" + str(prom)  # agrega ** y promedio
    linea_Actualizada = f"{lista.strip()}**{prom:.2f}\n"
    lineas_actualizadas.append(
        linea_Actualizada
    )  # agrega a lineas_actualizadas la linea_Actualizada
    # print(linea_Actualizada)#imprime todas a la vez

    unalinea = misdatos.readline()  # lee una linea mas
# print(lineas_actualizadas)#Impime las lineas actualizadas
misdatos.close()  # termina de mostrar misdatos
misdatos = open("datos.txt", "w")  # sobre escriba mis datos
for linea in lineas_actualizadas:
    misdatos.write(linea)
misdatos.close()
