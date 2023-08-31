def cesta(): #funcion inicio
    item={}
    Tcompra= 0 #total compra
    detal_compra = [] #detalles compra

    cant=int(input("cantidad de elementos a comprar: "))

    for i in range (cant):
        print("=" * 30)
        print("Datos de la compra #",i+1)
        nom=input("Nombre del producto: ")
        precio=int(input("Introdusca el precio del producto: "))
        if precio < 0:
            print("Error introdusca un numero valido")
            print("Se volvera a iniciar")
            print()
            return cesta()
        #la llave del item es el nombre y muestra el precio
        item[nom]=precio
        for key,value in item.items():
            print(key,value)
        print("=" * 30)
        cant = float(input(f"ingrese la cantidad del articulo {i+1}: "))
        Val_uni = item[nom]
        Vcompra = Val_uni*cant
        detal_compra.append({'nombre': nom,
                    'cantidad': cant,
                    'valor_unitario': Val_uni,
                    'valor_total': Vcompra
                    })
        Tcompra += Vcompra
        print("=" * 30)
        print(" "*30)

    print("\ndetalle de la compra: ")
    for item in detal_compra:
        print("=" * 30)
        print(f"Nombre: {item['nombre']}")
        print(f"Cantidad: {item['cantidad']:,.0f}")
        print(f"Valor unitario: ${item['valor_unitario']:,.0f}")#, separa cada miles
        print(f"Valor total: ${item['valor_total']:,.0f}")
        print("=" * 30)
        print()

    print(f"el total de la compra es: {Tcompra:,}")

cesta()
