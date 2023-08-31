import json
import os
os.system("cls")
def leerDatos():
    # Leer los datos del archivo JSON y devolver la lista de autos
    with open('AutoShopping.json', encoding="utf-8") as miAlmacen:
        misDatos = json.load(miAlmacen)
        miListadeAutos = misDatos["autostore"]["autos"]
    i=0
    for auto in miListadeAutos:
        i+=1
        print (i, " ", auto, "\n") #imprime el numero y auto

def mostrarUno(i):
    # Mostrar los detalles de un auto específico en base al índice
    i-=1
    with open('AutoShopping.json', encoding="utf-8") as miAlmacen:
            misDatos = json.load(miAlmacen)
            miAuto = misDatos["autostore"]["autos"][i]
    print(miAuto)

def mostrarEquipamiento(i):
    # Mostrar el equipamiento de un auto específico en base al índice
    i-=1
    with open('AutoShopping.json', encoding="utf-8") as miAlmacen:
            misDatos = json.load(miAlmacen)
            miAuto = misDatos["autostore"]["autos"][i]["equipamiento"]
    print(miAuto)

def agregarAuto():
    # Agregar un nuevo auto a la lista
    auto = {
        "marca":"Chevrolet",
        "linea": "Monza",
        "modelo": "2000",
        "precio": "9000"
    }
    n=int(input("Cuántos elementos ?"))
    if (n==0):
        auto["equipamiento"] = "Sin Equipamiento "
    else:
        if (n==1):
            equipamiento=input("Ingrese el equipo: ")
        else:
            equipamiento=[]
            for i in range (n):
                equipamiento.add(input("Ingrese el equipo: "))
    auto["equipamiento"]=equipamiento          


def ver_Autos():
    leerDatos()
    for i in range (2):
        indice=int(input("Cuál desea ver? "))
        mostrarUno(indice)
        mostrarEquipamiento(indice)
        input()

def actualizar_Auto():
    data=leerDatos
    ver_Autos()
    indice_a_buscar = int(input("Ingrese el indice del carro a cambiar datos: "))-1
    indice_a_buscar in data["autos"] #buscar la mascota
    print (data["autos"][indice_a_buscar])
    input()


def menu():
    seguir=True
    while seguir:
        print("="*46)
        print("=======Auto Shopping========")
        print("="*46)
        print(" ")
        print(" "*4+" 1) Mostrar lista de autos")
        print(" "*4+" 2) Mostrar un auto")
        print(" "*4+" 3) Mostrar equipamiento")
        print(" "*4+" 4) Agregar auto")
        print(" "*4+" 5) salir del programa\n")
        print("="*46)
       

        opcion = int(input('opcion ==========> '))
        if (opcion) == 5:
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 5):
            return print('\nEl número debe ser entre 0 y 6\n')
        
        switch = {1: ver_Autos ,2:mostrarUno, 3:mostrarEquipamiento, 4:agregarAuto, 5:actualizar_Auto}
        switch[opcion]()

menu()