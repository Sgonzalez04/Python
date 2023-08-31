contactos = {}

cont=0
while True:
    cont +=1
    nom = input(f"Digite el nombre del usuario # {cont} (o escriba 'NO' para terminar)")
    if nom.lower()== "no": #devuelve todo en minusculas
        break#rompe ciclo
    if nom in contactos: #busca si hay repetido 
        print("Nombre repetido")
        continue #devuelve al ciclo mas cercano
    telefono = int(input("digite el telefono: "))

    contactos[nom]=telefono #se le agrega al nombre anterior un telefono
    print("**"*30)
    for nom,telefono in contactos.items(): #busca la llave nombre y telefono en la lista y la imprime
        print(f"nombre: {nom}") 
        print(f"telefono: {telefono}")
        print()