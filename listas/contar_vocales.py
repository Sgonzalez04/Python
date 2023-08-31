#contar cantidad de a, e, i, o ,u

n=int(input("cuantas letras desea ingresar: "))
lst = [] #lista para almacenar
for i in range (n):
    letra = input(f"ingrese la letra # {i+1}: ")
    lst.append(letra[0]) #agrega a la lista la letra

vocales = ["a", "e", "i", "o", "u"] #lista de vocales 0=a, 1=e
cantidad = [0]*5 #lista con 5 ceros se remplaza lo de arriba por 0

for letra in lst:
    for p in range(len(vocales)): #recorrer por indices
        if letra == vocales [p]: #recorre letras que se ingresaron
            cantidad [p] += 1 #se aumenta segun la cantidad que halla de vocales en 1 a la ubicacion
            break

for p in range(len(vocales)): #recorre por la lista de vocales la cantidad que hay en letras
    print(f"cantidad de {vocales[p]} es {cantidad[p]}")