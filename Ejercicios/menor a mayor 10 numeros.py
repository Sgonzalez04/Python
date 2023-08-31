# se pide primero 1 numero como base
num = float(input("ingrese el 1 numero: "))

# se basa que el 1 numero es el mayor y el menor hasta ahora por ser el unico
mayor = num
menor = num

# se pide otros 9 numeros en bucle, se comienza desde 2 por que ya hay uno
for numb in range(2, 11):
    num = float(input(f"ingrese el numero {numb}: "))
    # si num es mayor al anterior se actualiza el numero mayor
    if num > mayor:
        mayor = num
    # si num es menor al anterior se actualiza el numero menor
    if num < menor:
        menor = numero
# se imprime resultado
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
