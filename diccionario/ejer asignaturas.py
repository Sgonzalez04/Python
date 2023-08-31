asig = {}

cont = 0
while True:
    cont += 1
    nom = input(f"desesa continuar #{cont} (o escriba 'NO' para terminar)")
    if nom.lower() == "no":  # devuelve todo en minusculas
        break

    mater = input("ingrese la materia: ")
    # mientras no se cumpla la condicion
    while (
        not mater.strip()
    ):  # Se repetirá si la entrada está en blanco o solo contiene espacios
        print("Error: El nombre de la materia no puede estar en blanco.")
        mater = input("Ingrese la materia: ")

    notaa = int(input("ingrese la nota: "))
    while not notaa.isdigit():  # Se repetirá si la entrada no es un número válido
        print("Error: Ingrese una nota válida (número entero).")
        nota = input("Ingrese la nota: ")
    mate = asig.setdefault(mater, notaa)

    for k, v in asig.items():
        print("materia: ", k, v, "nota: ")

print("programa terminado")
