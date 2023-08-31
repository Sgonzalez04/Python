# Solicitar al usuario que ingrese los dos números enteros positivos
n1 = int(input("Ingrese el primer número entero positivo: "))
n2 = int(input("Ingrese el segundo número entero positivo: "))

# Calcular la suma de los divisores propios de cada número
#inicia en 0 y va hasta n1
sumdivin1 = 0
for entpos in range(1, n1):
    if n1 % entpos == 0:
        sumdivin1 += entpos

sumdivin2 = 0
for entposi in range(1, n2):
    if n2 % entposi == 0:
        sumdivin2 += entposi

# Verificar si los números son amigos
if n1 == sumdivin2 and n2 == sumdivin1:
    print(f"{n1} y {n2} son números amigos.")
else:
    print(f"{n1} y {n2} NO son números amigos.")
