# imprima numeros pares del 2 al 50 incluyendo 50

# for par in range (2,51,2):
#   print(par, end="-,-")

# IMPRIMER MULTIPLOS DE 5 MENORES DE 100
# for m in range (5, 100 ,5):
#   print(m, end=", ")

# indicar si un numero ingresado por el usuario es primo o no

n = int(input("numero: "))
# 1 es primo
if n > 1:
    esprimo = True
    # escane desde el 2 hasta el n si es divisible
    # el ultimo en range es cada cuanto cuenta12 978 189
    for d in range(2, n):
        if n % d == 0:
            esprimo = False
            break

    if esprimo == True:
        print("el numero es primo")
    else:
        print("el numero no es primo")
else:
    print("error. numero invalido, deben ser mayores a 1")
