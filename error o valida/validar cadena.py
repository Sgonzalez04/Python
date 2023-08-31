while True:
    # intenta una operacion
    try:
        n = input("Nombre: ")
        if (n == None or n.strip() == ""):  # no se coloca si esta vacio o si solo espacios
            print("nombre invalido.")
            continue
        break
    except Exception as e:  # excepcion generica
        print("Ha sucedido un error.", e)
        input("presione cualquier tecla para continuar...")

print("\n el nombre que se digito es: ", n)
