

def Añadirmodificar():
    


def menu():
    seguir=True
    while seguir:
        print("="*46)
        print("=======Telefonos agenda========")
        print("="*46)
        print(" ")
        print(" "*4+" 1) Añadir/Modificar")
        print(" "*4+" 2) Buscar")
        print(" "*4+" 3) Borrar")
        print(" "*4+" 4) Listar")
        print(" "*4+" 5) salir del programa\n")
        print("="*46)
       

        opcion = int(input('opcion ==========> '))
        if (opcion) == 5:
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 5):
            return print('\nEl número debe ser entre 0 y 5\n')
        
        switch = {1: Añadirmodificar ,2:mostrarUno, 3:mostrarEquipamiento, 4:agregarAuto, 5:actualizar_Auto}
        switch[opcion]()

menu()