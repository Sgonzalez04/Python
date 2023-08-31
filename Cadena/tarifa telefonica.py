# sirve para hacer una funcion vacia para que no marque error
def leerEntero(Msg):
    pass


# funcion leer entero
def leerEntero(msg):
    while True:
        try:
            num = int(input(msg))
            if n < 1:
                print("el numero no puede menor a 1")
                input("Presione una tecla para continuar")
                continue
            break
        except ValueError:
            print("Numero invalido")
            input("presione una tecla para continuar")

    return num  # devuelve el resultado


# msg es mensaje


# LEER NOMBRE FUNCION
def leerNombre(msg):
    while True:
        try:
            num = int(input(msg))
            if nom == None or nom.strip() == "":
                print("el nombre no puede ser vacio")
                input("Presione una tecla para continuar")
                continue
            break
        except ValueError:
            print("nombre invalido")
            input("presione una tecla para continuar")

    return num  # devuelve el resultado


def leerEstrato(msg):
    while True:
        try:
            num = int(input(msg))
            if n < 1 or n > 5:
                print("el estrato debe ser de uno a 5")
                input("Presione una tecla para continuar")
                continue
            break
        except ValueError:
            print("numeRo invalido invalido")
            input("presione una tecla para continuar")

    return num  # devuelve el resultado


def tarifabasica(est):
    if est == 1:
        return 10_000
    elif est == 2:
        return 15_000
    elif est == 3:
        return 20_000
    elif est == 4:
        return 25_000
    elif est == 5:
        return 30_000


def calcularImpulso(imp):
    return imp * 100


def mostrarVAlPagar(nom, tbas, valimp):
    print("\nnombre: ", nom)
    print(f"\nvalor a pagar: ${tbas+valimp:,.0f}")
    print(f"\nvalor a pagar tarifa basica: ${tbas:,.0f}")
    print(f"\nvalor a pagar: ${valimp:,.0f}")


# primero se hizo esta parte
n = leerEntero("cantidad abonados: ")
# crea una funcion
for i in range(1, n + 1):
    print("\nabonado #", i)
    nom = leerNombre("nombre: ")
    est = leerEstrato("Estrato: ")
    imp = leerEntero("cantidad Impulso: ")
    tbas = tarifabasica(est)
    valimp = calcularImpulso(imp)

    mostrarVAlPagar(nom, tbas, valimp)
    valtot += tbas + valimp

print(f"\nValor total a pagar: ${vaktit:,.0f} ")
