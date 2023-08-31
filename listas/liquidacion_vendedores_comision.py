#vendedores
vTcomisiones = 0
vendedores = int(input("ingrese la cantidad de vendedores: "))
for i in range (vendedores):
    if vendedores < 0:
        print("error. ingrese cantidad de vendedores o -1 para terminar")
    if vendedores >= 1:
        print(f"la cantidad de vendedores es: {vendedores}")
    tComisiones=0
    tVentas= 0
    while True: #documento identidad vendedores
        try:
            di = int(input("ingrese documento de identidad del vendedor: "))
            break
        except ValueError:
            print("Oops! No es un entero. intenta de nuevo...")
            input("presione cualquier tecla para continuar...")
    print("\n el documento que se digito del vendedor es: ", di)

    while True: # nombre vendedores
        try:
            nom = input("ingrese nombre del vendedor: ")
            if (nom == None or nom.strip() == ""):
                print("nombre invalido.")
                continue
            break
        except Exception as e:
            print("Ha sucedido un error.", e)
            input("presione cualquier tecla para continuar...")
    print("\n el nombre que se digito del vendedor es: ", nom)

    while True: # tipo de vendedor
        try:
            tv = int(input("ingrese tipo vendedor 1(puerta a puerta), 2(telemercadeo), 3 (Ejecutivo de ventas)"))
            break
        except ValueError:
            print("Oops! No es un entero. intenta de nuevo...")
            input("presione cualquier tecla para continuar...")
            continue
    print("\n el tipo de vendedor que se digito es: ", tv)

#ventas

    ventas = int(input("ingrese la cantidad de ventas: "))
    for i in range (ventas): 
        if ventas < 0: #error ventas 0
            print("error. ingrese cantidad de ventas o -1 para terminar")
        if ventas >= 1:
            while True: #nombre venta
                try:
                    nomventa = input("ingrese nombre de a persona a la que se realizo la venta: ")
                    if (nomventa == None or nomventa.strip() == ""):
                        print("nombre invalido.")
                        continue
                    break
                except Exception as e:
                    print("Ha sucedido un error.", e)
                    input("presione cualquier tecla para continuar...")
            print("\n el nombre de la persona a la que se realizo la venta: ", nomventa)
            
            while True: #codigo cliente
                try:
                    codcli = int(input("ingrese codigo del cliente: "))
                    break
                except ValueError:  
                    print("Oops! No es un entero. intenta de nuevo...")
                    input("presione cualquier tecla para continuar...") 
                except Exception as e: 
                    print("Ha sucedido un error.", e)
                    input("presione cualquier tecla para continuar...")
            print("\n el codigo del cliente es: ", codcli)

            while True: #codigo de venta contado o credito
                try:
                    tipvent = int(input("Ingrese el codigo de venta (1=contado 2=credito)"))
                    if (tipvent < 1 or tipvent > 2):
                        print("eliga el codigo de venta 1(Contado) o 2(credito) solamente")
                        input("presione cualquier tecla para continuar...")
                        continue
                    break
                except ValueError:  # error de valor
                    print("Oops! No es un entero. intenta de nuevo...")
                    input("presione cualquier tecla para continuar...") 
            print("\n el codigo de venta es: ", tipvent)

            while True: # valor venta
                valventa = int(input("Ingrese el valor de la venta: "))
                tVentas+=valventa
                
                #puerta a puerta
                if tv == 1:
                    #contado
                    if tipvent == 1:
                        ppcon = valventa *0.25
                        tComisiones +=valventa*.25 #si es se le agrega a tcomisiones un 25% de la venta
                    #credito
                    if tipvent == 2:
                        tComisiones += valventa * 0.20
                    break
                #telemercadeo
                if tv == 2:
                    #contado
                    if tipvent == 1:
                        tComisiones += valventa *0.15
                    #credito
                    if tipvent == 2:
                        tComisiones += valventa * 0.10
                    break
                
                #ejecutivo de ventas
                if tv == 3:
                    #contado
                    if tipvent == 1:
                        tComisiones += valventa *0.20
                    #credito
                    if tipvent == 2:
                        tComisiones += valventa * 0.15
                    break
                break
            print(f"\n el valor de venta es: ${valventa:,.0f}",)

#pagos
        print(f"el valor comisiones es: ${tComisiones:,.0f}")
        print(f"El valor de total ventas es: ${tVentas:,.0f}")
        vTcomisiones += tComisiones

print(f"el valor a pagar por total de comisiones es: ${vTcomisiones:,.0f}")
