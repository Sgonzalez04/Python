num = int(input("ingrese el digito: "))

if num < 0 or num >= 10000000000:
    print("error digito invalida")
elif num < 10:
    numt = 1
elif num < 100:
    numt = 2
elif num < 1000:
    numt = 3
elif num < 10000:
    numt = 4
elif num < 100000:
    numt = 5
elif num < 1000000:
    numt = 6
elif num < 10000000:
    numt = 7
elif num < 100000000:
    numt = 8
elif num < 1000000000:
    numt = 9
elif num < 10000000000:
    numt = 10

print("su cantidad de dijitos es: ", numt)
