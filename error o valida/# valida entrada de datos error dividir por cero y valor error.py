
while True:
    # intenta una operacion
    try:
        n = int(input("ingrese un numero: "))
        break
    # continua despues de que el try falle
    except ValueError:  # error de valor
        print("Oops! No es un entero. intenta de nuevo...")
        input("presione cualquier tecla para continuar...")  # espera a que digite algo para que lea el mensaje
    except Exception as e: #excepcion generica
        print("Ha sucedido un error.", e)
        input("presione cualquier tecla para continuar...")

print("\n el numero que se digito es: ", n)
