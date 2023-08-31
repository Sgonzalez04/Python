cant = int(input("cantidad de estudiantes: "))
est = {}
for i in range(1, cant + 1):
    datos = {}
    print("Datos del estudiantes #", i)
    cod = int(input("cod: "))
    if cod == 999:
        break
    nom = input("Nombre: ")
    not1 = round(
        float(input("nota 1(30%): ")), 1
    )  # round redondea y luego se le da uno para 1 decimal
    not2 = round(float(input("nota 2(30%): ")), 1)
    not3 = round(float(input("nota 3(40%): ")), 1)
    notaT = round((not1 * 0.3) + (not2 * 0.3) + (not3 * 0.4), 1)

    datos = {
        "nombre": nom,
        "nota 1": not1,
        "nota 2": not2,
        "nota 3": not3,
        "definitiva": notaT,
    }
    est[nom] = datos

print("=" * 40)
print("** notas **")
print("=" * 40)
for k, v in est.items():
    print(f"su nombre es: {v['nombre']}")  # se busca en la lista v el nomnre
    print(f"su nota definitiva es: {v['definitiva']}")
    if v["definitiva"] >= 3.0:
        print("Usted a: Aprobado")
    else:
        print("Usted a: Reprobado")
    print()
    print("siguiente")
    print()
