
cant = int(input("cantidad de docentes"))
doc = {} #guarda docente
dic_cat= {1:25000, 2:30000, 3:40000, 4:45000, 5:60000} #diccionario categoria
valTotal = 0
for i in range (1, cant+1):
    datos={}
    print("Datos del docente #",i)
    ced= int(input("cedula: "))
    nom = input("Nombre: ")
    cat = int(input("Categoria (1 a 5): "))
    ht = int(input("horas trabajadas: "))
    valhono =dic_cat[cat]*ht
    
    datos = {
        "nombre": nom,
        "categoria": cat,
        "horas trabajadas": ht,
        "honorarios": valhono
    }

    doc[ced] = datos # repite los docentes pide los datos
    valhono += valhono #guarde los honorarios

print("=", *40)
print("** informe **")
print("="*40)
for k, v in doc.items():
    print(v["nombre"], "\t", f"${v['honorarios']:,.0f}")
    #diccionario nombre imprima honorarios
    #k no se coloca en print ya que no se necesita

print("=", *40)
print("** resumen **")
print("="*40)
print(f"valor total de honorarios ${valTotal:,.0f}")
