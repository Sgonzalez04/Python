def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar ...")

def leerValHora(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 8000 or n > 150000:
                msgError("Error. eliga un valor entre 8.000 o 150.000")
                continue
            if n < 1:
                msgError("Error. Valor de las horas mayor que 0")
                continue
            return n
        except ValueError:
            msgError("Error. Valor de las Horas invalidas")
            continue

def leerHoras(msg):
    while True:
        try:
            n = int(input(msg))
            if n > 160:
                msgError("Error. No se pueden hacer mas de 160 horas")
                continue
            if n < 1:
                msgError("Error. Horas mayor que 0")
                continue
            return n
        except ValueError:
            msgError("Error. Horas invalidas")
            continue

def leerNom(msg):
    while True:
        try:
            n = input(msg)
            if n == None or n.strip() == "":
                print("Error Nombre invalido.")
                continue
            return n
        except Exception as e:
            print("Ha sucedido un Error: ", e)
            continue

def leerId(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                msgError("Error. Id mayor que 0")
                continue
            return n
        except ValueError:
            msgError("Error. Id invalido")
            continue

#agregar empleado 1
def agregarEmpleado(lstEmpl):
    print("\n\n*** 1. Agregar empleado - ACME ***\n")
    
    id = leerId("Id del empleado: ")
    nom = leerNom("Nombre del empleado: ")
    hora = leerHoras("Horas trabajadas (solo 1 a 160 Horas.): ")
    valh = leerValHora("Valor de la Hora trabajada (entre $8,000 y $150,000): ")
    print("")
    print("empleado nuevo:")
    datempl = [id, nom, hora, valh]
    lstEmpl.append(datempl) 
    print(f"Id: {id} ,\nNombre: {nom} ,\nHoras trabajadas: {hora} ,\nValor por hora: {valh}\n")
    input()

#modificar empleado 2
def modificarEmpleado(lstEmpl):
    print("\n\n*** 2. modificar empleado - ACME ***\n")
    id = leerId("Id del empleado a cambiar datos: ")
    for idx, mod in enumerate(lstEmpl): #enumerate es para lista
        if mod[0] == id:
            idm = leerId("Nuevo ID del empleado: ")
            nomm = leerNom("Nuevo nombre del empleado: ")
            horam  = leerHoras("Nuevas horas trabajadas (solo 1 a 160 Horas.): ")
            valhm = leerValHora("Nuevo valor de la Hora trabajada (entre $8,000 y $150,000): ")

            lstEmpl[idx] = [idm, nomm, horam, valhm]
            print("Empleado modificado con éxito.")
            input()
            return
    print("Empleado con ID dado no encontrado.")
    input()


#buscar empleado 3
def buscarEmpleado(lstEmpl):
    print("\n\n*** 3. Buscar empleado - ACME ***\n")
    id = leerId("Id del empleado: ")
    for empleado in lstEmpl:
        if empleado[0] == id:
            print(f"Empleado encontrado:\n ID: {empleado[0]}\nNombre: {empleado[1]}\nHoras trabajadas: {empleado[2]}\nValor por hora: {empleado[3]}")
            return
    print("Empleado no encontrado.")
    input()

#eliminar empelado 4
def eliminarEmpleado(lstEmpl):
    print("\n\n*** 4. Eliminar empleado - ACME ***\n")
    id = leerId("Id del empleado a eliminar: ")
    for eliminar in lstEmpl:
        print(eliminar[0])
        if eliminar[0] == id: #si eliminiar esta en la id espacio 0
            lstEmpl.remove(eliminar)
            print("Empleado eliminado")
            break
    else:
        print("Empleado no encontrado")
    input()

#lista empleados 5
def listarempleados(lstEmpl):
    print("\n\n*** 5. lista empleados - ACME ***\n")
    e=0
    for empleado in lstEmpl:
        if len(lstEmpl)==0:
            print("no hay empleados registrados")
        else:
            print(f"Id: {empleado[0]} ,\nNombre: {empleado[1]} ,\nHoras trabajadas: {empleado[2]} ,\nValor por hora: {empleado[3]}\n")
            #condicion que se muestren solo 5 y se pida si hay mas que se continue
            e+=1  #cada empleado le va sumando 1
            if e==5: #si e llega a 5 haga la pregunta
                op = int(input("desea seguir? 1,Si  2,No"))
                if op == 1: #vuelva a seguir con los empleados
                    e=0
                if op == 2:
                    break
    input()

#lista nomina de empleados 6
def Listarnominadeempleado(lstEmpl):
    print("\n\n*** 6. listar nomina de empleado - ACME ***\n")
    id = leerId("Id del empleado para nomina: ")
    for nomina in (lstEmpl):
        print(nomina[0])
        if nomina[0] == id:
            salariobruto = nomina[3]* nomina[2] #lista nomina
            if salariobruto < 1_160_000:
                transporte =  140_606
            else:
                transporte = 0
            eps = salariobruto * 0.04
            pension = salariobruto * 0.04
            descuento = eps + pension
            salarioneto = (salariobruto+transporte-eps-pension)
            print(f"Id: {nomina[0]} ,\nNombre: {nomina[1]} ,\nHoras trabajadas: {nomina[2]} ,\nValor por hora: {nomina[3]}\n")
            print(f"su salario bruto es: ${salariobruto:,.0f}, su auxilio de transporte es: ${transporte:,.0f}, su descuento por eps y pension es: ${descuento:,.0f}, su salario neto es: ${salarioneto:,.0f}")
            return
    input()

#lista nomina 7
def Listarnominadetodosempleados(lstEmpl):
    print("\n\n*** 7. listar nomina total de empleado - ACME ***\n")
    print("Oprima una tecla para pasar al siguiente empleado")
    e=0
    for listnomina in lstEmpl:
        if len(lstEmpl)==0:
            print("no hay empleados registrados")
        else:
            print(f"Id: {listnomina[0]} ,\nNombre: {listnomina[1]} ,\nHoras trabajadas: {listnomina[2]} ,\nValor por hora: {listnomina[3]}\n")
            salariobruto = listnomina[3]* listnomina[2] #lista nomina
            if salariobruto < 1_160_000:
                transporte =  140_606
            else:
                transporte = 0
            eps = salariobruto * 0.04
            pension = salariobruto * 0.04
            descuento = eps + pension
            salarioneto = (salariobruto+transporte-eps-pension)
            print(f"su salario bruto es: ${salariobruto:,.0f} ,\nsu auxilio de transporte es: ${transporte:,.0f} ,\nsu descuento por eps y pension es: ${descuento:,.0f} ,\nsu salario neto es: ${salarioneto:,.0f}")
            #se muestre solo cada 5
            e+=1  #cada empleado le va sumando 1
            if e==5: #si e llega a 5 haga la pregunta
                op = int(input("desea seguir? 1,Si  2,No"))
                if op == 1: #vuelva a seguir con los empleados
                    e=0
                if op == 2:
                    break
        input()
    input("oprima una tecla para continuar")

def menu():
    while True:
        try:
            print("\n\n*** NOMINA ACME ***")
            print("\tMENU")
            print("1- Agregar empleado\n\
2- Modificar empleado\n\
3- Buscar empleado\n\
4- Eliminar empleado\n\
5- Listar empleados\n\
6- Listar nomina de un empleado\n\
7- Listar nomina de todos los empleados\n\
8- Salir\n")
            op = int(input("\t>> Escoja una opcion (1-8): "))
            if op < 1 or op > 8:
                msgError("Error. Opcion Invalida (de 1 a 8).")
                continue
            return op
        except ValueError:
            msgError("Error. Opcion Invalida (de 1 a 8).")
            continue

def main():
    lstEmpl = []
    while True:
        op = menu()
        if op == 1:
            agregarEmpleado(lstEmpl)
        elif op == 2:
            modificarEmpleado(lstEmpl)
        elif op == 3:
            buscarEmpleado(lstEmpl)
        elif op == 4:
            eliminarEmpleado(lstEmpl)
        elif op == 5:
            listarempleados(lstEmpl)
        elif op == 6:
            Listarnominadeempleado(lstEmpl)
        elif op == 7:
            Listarnominadetodosempleados(lstEmpl)
        elif op == 8:
            print("\n", "Gracias por usar el programa... Adios...".center(80))
            break

# Programa Principal
main()