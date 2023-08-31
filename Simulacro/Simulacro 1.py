#Simulacro CICLO 1
#Elabore un programa Python para gestionar el CRUD del archivo de datos PetShopping.json con las siguientes funcionalidades:
#	1. Mostrar en pantalla todas las mascotas a la venta visualizando: Tipo, Raza, Precio y Servicios
#	2. Crear Nueva mascota con la posibilidad de múltiples ítems de Servicio
#	3. Mostrar los datos de Mascotas por Tipo elegido visualizando: Raza, Precio y Servicios
#	4. Actualizar los datos de una mascota consultada por índice (Mostrar el listado total y elegir por 	índice)
#	5. Eliminar una mascota de la tienda (Mostrar el listado total y elegir por índice)

import json


general={}
general['mascotas']=[]
with open('PetShopping.json', "r") as mascotas:
    data=json.load(mascotas)

#todas mascotas
def tipo_mascota ():
    contador=0
    for usuario in data["pets"]:
        contador+=1

        print(f"***PET # {contador}***")
        print("Tipo:", usuario['tipo'])
        print("Raza:", usuario['raza'])
        print("Precio:", usuario['precio'])
        print("Servicios:", usuario['servicios'])
        print()
    input("Presione una tecla para continuar")

#lee los datos
def leer_Datos():
    with open("PetShopping.json", "r",encoding="utf-8") as file:
        data=json.load(file)
    return data
#escribe los datos
def escribir(data):
    with open ("PetShopping.json","w",encoding="utf-8") as file: #utf-8 para aceptar caracteres especiales
        json.dump(data,file,ensure_ascii=False,indent=4)#ensure_ascii=False es para admitir caracteres especiales

def reintetar():
    act=input("desea volver a realizar la operacion(si) o volver al menu(no): ")
    if act.lower() == "si":
        return True
    elif act.lower() == "no":
        return False
    elif act != "si" or act != "no":
        print("escriba solo si o no")
        return reintetar()

#nueva mascotas
def nueva_Mascota ():
    tipo=input("ingrese el tipo de mascota: ")
    raza=input("ingrese la raza: ")
    talla=input("ingrese la talla(pequeña, mediana, grande): ")
    #!= es diferente que
    if talla != "pequeña" and talla != "mediana" and talla != "grande":
        return print("escriba solo las tallas proporcionadas")
    precio=int(input("ingrese el precio: "))
    servicio=input("Ingrese el servicio: ")

    mascota={"tipo": tipo,
            "raza": raza,
            "talla":talla,
            "precio":precio,
            "servicios": servicio}
    
    #carga los datos
    data = leer_Datos()
    print(data)

    #agrega a la nueva mascota a la lista existente
    data["pets"].append(mascota)

    #escribe datos actualizados
    escribir(data)#se mandan datos guardados
    if reintetar():
        nueva_Mascota()
    else:
        print("Volviendo al menu principal")
    input("Presione una tecla para continuar")
    

#mostrar tipo
def mascota_tipo ():
    mascota_encontrada=False
    for i in data["pets"]:
        print("tipos de mascotas: ", i['tipo'])
    mastipe=input("ingrese el tipo de mascota que desea buscar: ")
    for i in data["pets"]:
        if i ['tipo'] == mastipe:
            print(f"tipo de mascota encontrada:\ntipo: {i['tipo']}\nraza: {i['raza']}\ntalla: {i['talla']}\nprecio: {i['precio']}\nservicio: {i['servicios']}")
            mascota_encontrada=True
            break
    if not mascota_encontrada:
        print("tipo de mascota no encontrada")
    if reintetar():
        mascota_tipo()
    else:
        print("Volviendo al menu principal")
    input("Presione una tecla para continuar")

#actualizar mascota
def actualizar_Mascota(): 
    #para llamar funcion escribir ()
    data= leer_Datos() #para leer todos los datos
    tipo_mascota()
    indice_a_buscar = int(input("Ingrese el indice de mascota a cambiar datos: "))-1
    indice_a_buscar in data["pets"] #buscar la mascota
    print (data["pets"][indice_a_buscar])
    input()
    
    mascota = data["pets"][indice_a_buscar]
    tipon = input("Nuevo tipo: ")
    razan = input("Nueva raza: ")
    tallan = input("Nuevo talla: ")
    precion = input("Nuevo precio: ")
    servicion = input("Nuevo servicio: ")

    mascota['tipo'] = tipon
    mascota['raza'] = razan
    mascota['talla'] = tallan
    mascota['precio'] = precion
    mascota['servicios'] = servicion

    escribir(data)
    print("Mascota modificada con éxito.")
    if reintetar():
        actualizar_Mascota()
    else:
        print("Volviendo al menu principal") 
    input("Presione una tecla para continuar")

def eliminar_mascota ():
    data= leer_Datos() #para leer todos los datos
    
    tipo_mascota()
    indice_a_borrar= int(input("Ingres el indice de la mascota a eliminar: "))-1 #indices a borrar -1
    if indice_a_borrar <0 or indice_a_borrar> len(data["pets"]): #si el indice ensta en la lista
        data["pets"].pop(indice_a_borrar) #borre en "pets" el indice que esta en indice a borrar
    if reintetar():
        eliminar_mascota()
    else:
        print("Volviendo al menu principal") 
    input("Presione una tecla para continuar")



def menu():
    seguir=True
    while seguir:
        print("="*46)
        print("=======selecciona la opccion que desee========")
        print("="*46)
        print(" ")
        print(" "*4+" 1) Mostrar todas las mascotas")
        print(" "*4+" 2) Crear una nueva mascota")
        print(" "*4+" 3) Mostrar mascotas por tipo elegido")
        print(" "*4+" 4) Actualizar mascota")
        print(" "*4+" 5) eliminar mascota")
        print(" "*4+" 6) salir del programa\n")
        print("="*46)
       

        opcion = int(input('opcion ==========> '))
        if (opcion) == 6:
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 6):
            return print('\nEl número debe ser entre 0 y 6\n')
        
        switch = {1: tipo_mascota ,2:nueva_Mascota, 3:mascota_tipo, 4:actualizar_Mascota, 5:eliminar_mascota}
        switch[opcion]()

menu()