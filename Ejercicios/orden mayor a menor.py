num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercer numero: "))

# mayor
if num1 > num2 and num3:
    mayor = num1

elif num2 > num3 and num2:
    mayor = num2

elif num3 > num2 and num1:
    mayor = num3

# menor
if num1 < num2 and num3:
    menor = num1

elif num2 < num3 and num2:
    menor = num2

elif num3 < num2 and num1:
    menor = num3

# medio
# == diferenciar
if num1 < mayor and num1 > menor:
    medio = num1

elif num2 < mayor and num2 > menor:
    medio = num2

elif num3 < mayor and num3 > menor:
    medio = num3


print("el 1 es: ", mayor)
print("el 2 es: ", medio)
print("el 3 es: ", menor)


# if num1 >= num2 and num1 >=num3:
#    mayor = num1
#    if b >= c

# if num1 > num2:
#    if num1 > num3:
#        if num3 > num2:
#            resultado=f"{num1},{num3},{num2}"
#        else:
#            resultado=f"{num1},{num2},{num3}"
#    else:
#        result=f"{num3},{num1},{num2}"
# else:
#    if num2 > num3:
#        if num3 > num1:
#            resultado
