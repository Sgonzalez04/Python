#Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre
#y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*)
#Al finalizar se mostrará los siguientes datos:
#Todos los alumnos mayores de edad
#el que es mayor de edadd

cant=int(input("introdusca la cantidad de alumnos: "))
edad="0"

for i in range(cant):
    print(f"El alumno #{i+1}")
    nom= input("Intodusca el nombre del alumno (Si introduce * termina): ")
    if nom == "*":
        print("Programa terminado")
        break
    edadn= input("Introdusca la edad del alumno: ")
    
    if edadn > edad:
        edad=edadn
        mayoredad = edadn
        mayornom = nom
        
print(f"el nombre del mayor es {mayornom} y su edad es {mayoredad}")
