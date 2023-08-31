#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lenguaje)
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
#Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

matematicas=[]
Física=[]
Química=[]
Historia=[]
Lenguaje=[]

nota1 = float(input(f"ingrese la nota de matematicas (1 a 5): "))
matematicas.append(nota1) #agrega a la lista matematicas

nota2 = float(input(f"ingrese la nota de fisica (1 a 5): "))
Física.append(nota2) #agrega a la lista Física

nota3 = float(input(f"ingrese la nota de quimica (1 a 5): "))
Química.append(nota3) #agrega a la lista Química

nota4 = float(input(f"ingrese la nota de historia (1 a 5): "))
Historia.append(nota4) #agrega a la lista Historia

nota5 = float(input(f"ingrese la nota de lenguaje (1 a 5): "))
Lenguaje.append(nota5) #agrega a la lista Lenguaje

print()

print (f"Su nota en mateticas fue: {matematicas}")
print (f"Su nota en Física fue: {Física}")
print (f"Su nota en Química fue: {Química}")
print (f"Su nota en Historia fue: {Historia}")
print (f"Su nota en Lenguaje fue: {Lenguaje}")

print()

if nota1 <= 3:
    print("tiene que repetir matematicas")

if nota2 <= 3:
    print("tiene que repetir Física")

if nota3 <= 3:
    print("tiene que repetir Química")

if nota4 <= 3:
    print("tiene que repetir Historia")

if nota5 <= 3:
    print("tiene que repetir Lenguaje")