def centro(): #funcion inicio
    item={1:'lapiz',2:'cuadernos',3:'borrador',4:'calculadora',5:'escuadra'}
    valor= {1:2.500, 2:3.800, 3:1.200, 4:3.500, 5:3.700}

    Tcompra= 0 #total compra
    detal_compra = [] #detalles compra

    cant=int(input("cantidad de elementos a comprar: "))

    for i in range (cant):
        print("=" * 30)
        print("codigos de items")
        #imprime primero la llave y luego el valor dentor de esta en orden 
        for key,value in item.items():
            print(key,value)
        print("=" * 30)
        code = int(input(f"ingrese el codigo del articulo: ")) 
        cant = int(input(f"ingrese la cantidad del articulo {i+1}: "))
        print("=" * 30)
        print(" "*30)

        if code in item:
            Nom_item = item[code] #nombre item en el item codigo
            Val_uni = valor[code]
            Vcompra = Val_uni*cant 
            #detalles de la compra
            detal_compra.append({'codigo': code,
                    'nombre': Nom_item,
                    'cantidad': cant,
                    'valor_unitario': Val_uni,
                    'valor_total': Vcompra
                    })
            
            Tcompra += Vcompra

        else:
            print("Error. codigo invalido.")
    print("\ndetalle de la compra: ")
    for item in detal_compra:
        print("=" * 30)
        print(f"Código: {item['codigo']}")
        print(f"Nombre: {item['nombre']}")
        print(f"Cantidad: {item['cantidad']}")
        print(f"Valor unitario: ${item['valor_unitario']:,.3f}")
        print(f"Valor total: ${item['valor_total']:,.3f}")
        print("=" * 30)
        print()

    print(f"el total de la compra es: {Tcompra:,.3f}")

centro()
