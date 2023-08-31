#vendedores
vendedores = int(input("ingrese la cantidad de vendedores: "))

while vendedores <= vendedores:
    if vendedores < 0:
        print("error. ingrese cantidad de vendedores o -1 para terminar")
    if vendedores >= 1:
        print(f"la cantidad de vendedores es: {vendedores}")
    while True:
        try:
            di = int(input("ingrese documento de identidad: "))
        except ValueError:
            print("Oops! No es un entero. intenta de nuevo...")
            input("presione cualquier tecla para continuar...")
            continue
        break
    print("\n el documento que se digito es: ", di)

    while True:
        try:
            nom = input("ingrese nombre: ")
            if (nom == None or nom.strip() == ""):
                print("nombre invalido.")
                continue
            break
        except Exception as e:
            print("Ha sucedido un error.", e)
            input("presione cualquier tecla para continuar...")
    print("\n el nombre que se digito es: ", nom)

                            
    while True:
        try:
            tv = int(input("ingrese tipo vendedor 1(puerta a puerta), 2(telemercadeo), 3 (Ejecutivo de ventas)"))
        except ValueError:
            print("Oops! No es un entero. intenta de nuevo...")
            input("presione cualquier tecla para continuar...")
            continue
        break
    print("\n el vendedor que se digito es: ", tv)


                    #ventas
    while True:
        try:
            nomventas = input("ingrese nombre del cliente: ")
            if (nom == None or nom.strip() == ""):
                print("nombre invalido.")
                continue
            break
        except Exception as e:
            print("Ha sucedido un error.", e)
            input("presione cualquier tecla para continuar...")
    print("\n el nombre del cliente que se digito es: ", nom)



    ventas = int(input("ingrese la cantidad de ventas: "))
    for i in  range(ventas):
        if ventas < 0:
            print("error. ingrese cantidad de ventas o -1 para terminar")
        if ventas >= 1:
            while True:
        
        
        
        
        try:
            nom = input("ingrese nombre: ")
            if (nom == None or nom.strip() == ""):
                print("nombre invalido.")
                continue
            break
        except Exception as e:
            print("Ha sucedido un error.", e)
            input("presione cualquier tecla para continuar...")
    print("\n el nombre que se digito es: ", nom)

# ventas
nomventas = input("ingrese nombre del cliente: ")
codcli = int(input("ingrese el codigo del cliente: "))
tipvent = int(input("Ingrese el codigo de venta (1=contado 2=credito)"))


while True:
    valventa = int(input("Ingrese el valor de la venta: "))
    tv == 1
    if tipvent == 1:
        valventa * 0.75

