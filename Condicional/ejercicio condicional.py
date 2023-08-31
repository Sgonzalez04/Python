
nom = input("nombre: ")

#input transforma int a entero
sal = int(input("salario: "))

#if es condicional al final se coloca puntos para que diga que pasa
if sal<= 1_200_000:
    aux = 120_000
#si no es cierto se coloca else y : para condicion
else:
    aux = 0

print("\n", "-"*30)
print("Nombre: ", nom)
print(f"salario: ${sal:,.0f}")
print(f"auxilio transporte: ${aux:,.0f}")