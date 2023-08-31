# hallar promedio de notas (0 a 5.0) hasta que la nota
# sea -1 o cualquier otro numero negativo termina de pedir notas

suma = 0.0
nota = 0
cant = 0

while nota >= 0:  # comienzo ciclo hasta que pida nota menor a -1
    nota = float(input("ingrese la nota: "))  # pide notas

#si es mayor de 6 imprime y pregunta
    while nota > 5: 
        if nota > 5:  # si es verdad imprime error
            print("error. Ingrese una nota(0.0 a 5.0) o -1 para terminar")
            nota = float(input("ingrese una nota: ")) #se coloca para que no se repita
# no se coloca break ya que la condicion de parada esta en >5 si es true si se necesita
    if nota > 0:
        cant += 1
        suma += nota #Sumatoria: +=

prom = round(suma / cant, 1) #round redondea o aproxima
print(f"El promedio es: {prom:.1f}")
