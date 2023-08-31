# valida entrada de datos

while True:
    # intenta una operacion
    try:
        n= int(input("ingrese un numero: "))
        break
    # continua despues de que el try falle
    except ValueError:
        print("Oops! No es un entero. intenta de nuevo...")
        input("presione cualquier tecla para continuar...") #espera a que digite algo para que lea el mensaje
    
print("\n el numero que se digito es: ",n)
        




