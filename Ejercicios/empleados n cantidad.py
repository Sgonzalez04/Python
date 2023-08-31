cant= int(input("ingrese cantidad de empleados: "))

#se coloca el base
nom1 = input("nombre: ")

sal1 = int(input("salario: "))

if sal1<= 1_200_000:
    aux = 120_000
else:
    aux = 0

print("\n", "-"*30)
print("Nombre: ", nom1)
print(f"salario: ${sal1:,.0f}")
print(f"auxilio transporte: ${aux:,.0f}")

#ciclo para empleados repeticion
for emple in range(2, cant+1):

    nom = input("nombre: ")

    sal = int(input("salario: "))

    if sal<= 1_200_000:
        aux = 120_000
    else:
        aux = 0

#codigos mayor menor
    mayor = sal1
    menor = sal1
    namemayor = nom1
    namemenor = nom1

#condicion mayor menor
    if sal > mayor:
        mayor = sal  
        namemayor = nom
    if sal < menor:
        menor = sal 
        namemenor = nom

    print("\n", "-"*30)
    print("Nombre: ", nom)
    print(f"salario: ${sal:,.0f}")
    print(f"auxilio transporte: ${aux:,.0f}")
print(f"El número mayor es: {mayor} , y el nombre del que gana mas es: {namemayor}")
print(f"El número menor es: {menor} , y el nombre del que gana menos es: {namemenor}")