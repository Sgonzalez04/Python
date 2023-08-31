def frutas():
    item={1:'platano',2:'manzana',3:'pera',4:'naranja'}
    valor= {1:1.35, 2:0.80, 3:0.85, 4:0.70}

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
        if code < 0 or code > 4:
            print("Error codigo invalido")
            print("Se volvera a iniciar")
            print()
            return frutas()
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
        print(f"Valor unitario: ${item['valor_unitario']:,.2f}")
        print(f"Valor total: ${item['valor_total']:,.2f}")
        print("=" * 30)
        print()

    print(f"el total de la compra es: {Tcompra:,.3f}")
frutas()