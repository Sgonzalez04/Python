import json

general={}
general['Departamentos']=[]
with open('paisciudad.json', "r") as pais:
    data=json.load(pais)

#lee los datos
def leer_Datos():
    with open("paisciudad.json", "r",encoding="utf-8") as file:
        data=json.load(file)
    return data

#escribe los datos
def escribir(data):
    with open ("paisciudad.json","w",encoding="utf-8") as file: #utf-8 para aceptar caracteres especiales
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

def IdCiudades():
    with open('PaisCiudad.json', encoding="utf-8") as miPais:
        misDatos = json.load(miPais)
        listaDepatamentos = misDatos["Departamentos"]
    listaIds=[]
    for depto in listaDepatamentos:
        for ciudad in depto["Ciudades"]:
            listaIds.append(ciudad["idCiudad"])
    return(listaIds)

listaids = IdCiudades()


def iddepartamentos():
    with open('PaisCiudad.json', encoding="utf-8") as miPais:
        misDatos = json.load(miPais)
        listaDepatamentos = misDatos["Departamentos"]
    listaIdsdep=[]
    for depto in listaDepatamentos:
        listaIdsdep.append(depto["idDep"])

listaidsdep= iddepartamentos()

def listarciudades():
    for departamentos in data["Departamentos"]:
        for ciudades in departamentos["Ciudades"]:
            print("Id de la ciudad:", ciudades['idCiudad'])
            print("Nombre de la ciudad:", ciudades['nomCiudad'])
            print("Imagen:", ciudades['imagen'])
            print("Coordenadas:", ciudades['coordenadas'])
            print()
    input("Presione una tecla para continuar")

def agregar_Ciudad():
    data = leer_Datos()
    depart_existente=input("Ingrese en que departamento desea agregar la nueva ciudad: ")
    for departamentos in data["Departamentos"]:
        if depart_existente == departamentos["nomDepartamento"]:
            nuev_idciudad=int(input("Ingrese la id de la nueva ciudad: "))
            if nuev_idciudad in IdCiudades():
                print("Id de la ciudad ya tomada eliga una diferente")
                input("Presione una tecla para continuar")
                print()
                return agregar_Ciudad()
            nuev_nomciudad=input("Ingrese el nombre de la nueva ciudad: ")
            nuev_imagen=input("Ingrese el nombre del archivo de imagen a colocar: ")
            nuev_cordena=input("Ingresae las cordenadas de la nueva ciudad: ")
            
            nuev_Ciudad={"idCiudad":nuev_idciudad,
                        "nomCiudad":nuev_nomciudad,
                        "imagen":nuev_imagen,
                        "coordenadas":nuev_cordena}
            #carga los datos
            data = leer_Datos()
            print(data)

            #agrega a la nueva mascota a la lista existente
            data["Ciudades"].append(nuev_Ciudad)

            #escribe datos actualizados
            escribir(data)#se mandan datos guardados

            if reintetar():
                agregar_Ciudad()
            else:
                print("Volviendo al menu principal")
            input("Presione una tecla para continuar")
        else:
            print("departamento no encontrado")
            input("Presione una tecla para continuar")
            return
        
def eliminar_ciudad():
    data= leer_Datos()
    listarciudades()
    idciudadborrar=int(input("ingrese el id de la ciudad a borrar: "))
    for departamento in data["Departamentos"]:
        ciudades = departamento["Ciudades"]
        ciudad_encontrada = None
        for city in ciudades:
            if city["idCiudad"] == idciudadborrar:
                ciudad_encontrada = city
                break
        if ciudad_encontrada:
            ciudades.remove(ciudad_encontrada)
            escribir(data)
            print("Ciudad eliminada exitosamente")
            if reintetar():
                eliminar_ciudad()
            else:
                print("Volviendo al menú principal")
                break
        else:
            print("ID de ciudad no encontrada")
            input("Presione una tecla para continuar")


def eliminar_departamento():
    data= leer_Datos()

    listar_departamentos()
    indice_a_borrar= int(input("Ingrese el indice del departamento a eliminar: "))
    departamento_encontrado=None
    for departamento in data["Departamentos"]:
        if departamento["idDep"] == indice_a_borrar:
            departamento_encontrado= departamento
            break
    if departamento_encontrado:
        departamento.remove(departamento_encontrado)
        escribir(data)
        print("departamento eliminado exitosamente")
        if reintetar():
                eliminar_departamento()
        else:
            print("Volviendo al menú principal")
    else:
        print("ID de departamento no encontrada")
        input("Presione una tecla para continuar")

def creardepartamento():
    data = leer_Datos()
    for departamentos in data["Departamentos"]:
        nuev_iddep=int(input("Ingrese el id del departamento a agregar: "))
        if nuev_iddep == departamentos["idDep"]:
            print("Id de la ciudad ya tomada eliga una diferente")
            input("Presione una tecla para continuar")
            print()
            return creardepartamento()
        nuev_nomdep=input("Ingrese el nombre del nuevo departamento: ")
        nuev_ciudades=agregar_Ciudad()
        nuev_Dep={"nueva id del departamento": nuev_iddep,
                "nuevo nombre del departamento": nuev_nomdep,
                "nuevas ciudades":nuev_ciudades}
        data = leer_Datos()
        print(data)
        data["Departamentos"].append(nuev_Dep)
        escribir(data)
        if reintetar():
            creardepartamento()
        else:
            print("Volviendo al menu principal")
    input("Presione una tecla para continuar")
 


def listar_departamentos():
    for departamentos in data["Departamentos"]:
        print("Id departamento:", departamentos['idDep'])
        print("Nombre departamento:", departamentos['nomDepartamento'])
        print("Ciudades:", departamentos['Ciudades'])
        print()
    input("Presione una tecla para continuar")


def menu():
    seguir=True
    while seguir:
        print("="*46)
        print("=======MODULO GESTOR DE CIUDADES========")
        print("="*46)
        print(" ")
        print(" "*4+" 1) Listar todas las ciudades, sin clasificar por departamento.")
        print(" "*4+" 2) Adicionar una nueva ciudad en un departamento existente.")
        print(" "*4+" 3) Eliminar una ciudad de un departamento")
        print(" "*4+" 4) Crear un Departamento.")
        print(" "*4+" 5) Eliminar un Departamento")
        print(" "*4+" 6) Listar todos los departamenos")
        print(" "*4+" 7) Salir del programa\n")
        print("="*46)

        opcion = int(input('opcion ==========> '))
        if (opcion) == 7:
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 7):
            return print('\nEl número debe ser entre 0 y 6\n')
        
        switch = {1: listarciudades ,2:agregar_Ciudad ,3:eliminar_ciudad ,4:creardepartamento ,5:eliminar_departamento, 6:listar_departamentos}
        switch[opcion]()

menu()