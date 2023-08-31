import os #reciba ordenes sistema operativo

def validarinput(Mensaje): #ver si el mensaje no esta vacio
    data = input(Mensaje)
    #valida que no este vacio
    while(data.strip()==''):
        print("\ningrese algun dato\n")
        data = input(Mensaje)
    return data #devuelve los valores

def validarid (cod, estudiante): #valida si hay id en la lista
    for i in range(len(estudiante)):
        if (estudiante[i]['codigo'] ==cod):
            return True
    return False

def leerNombre(Msg): #lee que solo sea un nombre
    while True:
        try:
            nombre=input(Msg)
            if nombre.isalpha(): #que solo lea nombre y no numeros
                return nombre
            print("error digite un nombre valido")
            continue
        except ValueError:
            print("error digite un nombre valido")
            continue


#nuevo estudiante
def ingresar_Estudiante():
    os.system('clear')#limpiar pantalla comando con linux es cls con windows cls
    #valida si el docuemnto existe
    codigo = validarinput("digite el codigo de estudiante: ")
    while(validarid (codigo,estudiante)):
        print("\nEl estudiante ya existe\n")
        codigo = validarinput("Digite el codigo: ")
    #guarda dentro de ingresar datos
    #validarinput 
    nombre= leerNombre("digite el nombre: ")
    nota1= round(float(validarinput("digite la primera nota: ")), 1)
    nota2= round(float(validarinput("digite la segunda nota: ")), 1)
    nota3= round(float(validarinput("digite la tercera nota: ")), 1)
    

    #en la lista estudiantes se agregan los datos
    estudiante.append({
        "codigo":codigo,
        "nombre":nombre,
        "nota 1":nota1,
        "nota 2":nota2,
        "nota 3":nota3,
    })
    input()

#Buscar estudiante
def buscar_estudiante():   
    os.system('clear')
    busdoc= validarinput("ingrese el codigo del estudiante que desea buscar: ")
    estudiante_Encontrado=False #cominza falso
    for i in estudiante: #Diccionario de empleados, i es el diccionario
        if i ['codigo'] == busdoc: #busca estudiante en i 
            #en i se busca en el diccionario el resultado
            print(f"Empleado encontrado:\ncodigo: {i['codigo']}\nnombre: {i['nombre']}\nnota 1: {i['nota 1']}\nnota 2: {i['nota 2']}\nnota 3: {i['nota 3']}")
            estudiante_Encontrado=True #si se encuentra es verdadero
            break

    if not estudiante_Encontrado: # si no se encuentra es falso
        print("Empleado no encontrado.")
    input()

#actualiza el estudiante
def actualizar_estudiante():
    doc = input("codigo del estudiante a cambiar datos: ")
    for idx, mod in enumerate(estudiante): #enumerate es para lista
        if mod['codigo'] == doc: #en la ubicacion de 'estudiante' en la lista validarinput remplace
            nomn = leerNombre("Nuevo nombre del estudiante: ")
            nota1n= round(float(validarinput("digite la nueva primera nota: ")), 1)
            nota2n= round(float(validarinput("digite la nueva segunda nota: ")), 1)
            nota3n= round(float(validarinput("digite la nueva tercera nota: ")), 1)

            mod['codigo'] = doc
            mod['nombre'] = nomn
            mod['nota 1'] = nota1n
            mod['nota 2'] = nota2n
            mod['nota 3'] = nota3n
            
            print("estudiante modificado con éxito.")
            input()
            return
    print("estudiante con codigo dado no encontrado.")
    input()

#elimina al estudiante
def eliminar_estudiante():
    os.system('clear')
    cod = input("ingrese el codigo que desea eliminar: ")
    
    #busca en la lista el domumento y con pop lo borra
    for i in range(len(estudiante)):
        if (estudiante[i]['codigo'] == cod):
            empl =estudiante.pop(i)
            return print('\n se ha eliminado el estudiante', empl, '\n')
        
    return print('\n no existe el estudiante con ese codigo \n')
    input()

#definita del destudiante
def definitivo_estudiante():
    os.system('clear')
    busdoc= validarinput("ingrese el codigo del estudiante que desea buscar notas definitivas: ")
    estudiante_Encontrado=False #cominza falso
    for i in estudiante: #Diccionario de empleados, i es el diccionario
        if i ['codigo'] == busdoc: #busca estudiante en i 
            #en i se busca en el diccionario el resultado
            notaD = round((i['nota 1']+i['nota 2']+i['nota 3'])/3,1)
            i['notaDef'] = notaD #agregar a i en diccionario la nota definitiva
            print(f"estudiante encontrado:\ncodigo: {i['codigo']}\nnombre: {i['nombre']}\nnota 1: {i['nota 1']}\nnota 2: {i['nota 2']}\nnota 3: {i['nota 3']}\nnota definitiva: {i['notaDef']}")
            print()
            estudiante_Encontrado=True #si se encuentra es verdadero
            break
    if not estudiante_Encontrado: # si no se encuentra es falso
        print("Empleado no encontrado.")
    input()

#calcula definitiva general y promedio
def calcular_defypro():
    os.system('clear')
    total_notasD = 0  # Inicializar la suma de notas definitivas
    total_estudiantes = len(estudiante)  # Obtener la cantidad total de estudiantes
    
    for i in estudiante:
        notaD = round((i['nota 1']+i['nota 2']+i['nota 3'])/3,1)
        i['notaDef'] = notaD #agregar a i en diccionario la nota definitiva
        print(f"estudiante encontrado:\ncodigo: {i['codigo']}\nnombre: {i['nombre']}\nnota 1: {i['nota 1']}\nnota 2: {i['nota 2']}\nnota 3: {i['nota 3']}\nnota definitiva: {i['notaDef']}")
        print()
        total_notasD += i   ['notaDef']  # Sumar la nota definitiva al total
    promedio_general = total_notasD / total_estudiantes  # Calcular el promedio general
    print(f"Promedio general de notas definitivas: {promedio_general:.1f}\n")
    input()

#menu
def menu():
    seguir=True
    while seguir:
        print("*** Selecciona la opccion que desee ***")
        print(" "*4+"1) Ingresar un nuevo estudiante")
        print(" "*4+"2) Buscar un estudiante")
        print(" "*4+"3) Actualizar datos estudiante")
        print(" "*4+"4) Borrar un estudiante")
        print(" "*4+"5) Calcular definitiva de un estudiante")
        print(" "*4+"6) Calcular definitivas y promedio general")
        print(" "*4+"7) salir")
        print()

        opcion = int(input('opcion -->'))
        if (opcion) == 7:
            seguir = False
            return print('\nFin del programa\n')
        if(opcion < 1 or opcion > 6):
            return print('\nEl número debe ser entre 1 y 6\n')
        
        switch = {1: ingresar_Estudiante ,2: buscar_estudiante ,3: actualizar_estudiante ,4:eliminar_estudiante, 5:definitivo_estudiante, 6:calcular_defypro }

        switch[opcion]()
estudiante = []
menu()