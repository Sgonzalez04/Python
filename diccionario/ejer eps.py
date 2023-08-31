import os #reciba ordenes sistema operativo


def validarinput(Mensaje):
    data = input(Mensaje)
    #valida que no este vacio
    while(data.strip()==''):
        print("\ningrese algun dato\n")
        data = input(Mensaje)
    return data #devuelve los valores

#revisa si esta el documento
def validadocumento (id, empleados):
    for i in range(len(empleados)):
        if (empleados[i]['documento'] ==id):
            return True
    return False
    
def ingresardatos():
    os.system('clear')#limpiar pantalla comando con linux es cls con windows cls
    #valida si el docuemnto existe
    documento = validarinput("digite el documento: ")
    while(validadocumento(documento,empleados)):
        print("\nel documento ya existe\n")
        documento = validarinput("digite el documento: ")

    #guarda dentro de ingresar datos
    #validarinput 
    nombre= validarinput("digite el nombre: ")
    edad= validarinput("digite la edad: ")
    eps= validarinput("digite la eps: ")

    #en la lista empleados se agregan los datos
    empleados.append({
        "documento":documento,
        "nombre":nombre,
        "edad":edad,
        "eps": eps
    })
    input()

#recorrer la lista y si esta eliminar
def eliminarregisto():
    os.system('clear')
    doc = input("ingrese el documento que desea eliminar: ")
    
    #busca en la lista el domumento y con pop lo borra
    for i in range(len(empleados)):
        if (empleados[i]['documento'] == doc):
            empl =empleados.pop(i)
            return print('\n se ha elminado el registro', empl, '\n')
        
    return print('\n no existe el registro con ese documento \n')
    input()

#impirme el listado
def listadototal():
    os.system('clear')
    for i in empleados:
        print(f"Empleado encontrado:\ndocumento: {i['documento']}\nnombre: {i['nombre']}\nedad: {i['edad']}\neps: {i['eps']}")
        print()
    input()

#buscar y mostrar un registro
def buscarregistro():   
    os.system('clear')
    busdoc= validarinput("ingrese el documento que desea buscar: ")
    empleado_encontrado=False #cominza falso
    for i in empleados: #Diccionario de empleados, i es el diccionario
        if i ['documento'] == busdoc: #busca documento en i 
            #en i se busca en el diccionario el resultado
            print(f"Empleado encontrado:\ndocumento: {i['documento']}\nnombre: {i['nombre']}\nedad: {i['edad']}\neps: {i['eps']}")
            empleado_encontrado=True #si se encuentra es verdadero
            break

    if not empleado_encontrado: # si no se encuentra es falso
        print("Empleado no encontrado.")
    input()

def actualizarregistro():
    doc = input("documento del empleado a cambiar datos: ")
    for idx, mod in enumerate(empleados): #enumerate es para lista
        if mod['documento'] == doc: #en la ubicacion de 'documento' en la lista validarinput remplace
            docn = validarinput("Nuevo documento del empleado: ") 
            nomn = validarinput("Nuevo nombre del empleado: ")
            edadn = validarinput("Nuevas edad: ")
            epsn = validarinput("Nueva eps: ")

            mod['documento'] = docn
            mod['nombre'] = nomn
            mod['edad'] = edadn
            mod['eps'] = epsn
            print("Empleado modificado con éxito.")
            input()
            return
    print("Empleado con ID dado no encontrado.")
    input()


def menu():
    seguir=True
    while seguir:
        print("selecciona la opccion que desee")
        print(" "*6+"1) ingresar un nuevo registro")
        print(" "*6+"2) eleminar un registro")
        print(" "*6+"3) mostrar listado total")
        print(" "*6+"4) buscar y mostrar un registro")
        print(" "*6+"5) actualizar un registro")
        print(" "*6+"6) salir del programa\n")
        print()

        opcion = int(input('opcion -->'))
        if (opcion) == 6:
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 6):
            return print('\nEl número debe ser entre 0 y 6\n')
        
        switch = {1: ingresardatos ,2: eliminarregisto ,3: listadototal ,4:buscarregistro ,5:actualizarregistro }

        switch[opcion]()
empleados = []
menu()
    