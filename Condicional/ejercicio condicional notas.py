# como redondear
import math

# redondear hacia arriba = math.ceil
ncuant = math.ceil(float(input("nota cuantitativa(0-100):")))


nom = input("nombre: ")
# sin redondear
# ncuant = float(input("nota cuantitativa(0-100):"))

# FORMA LARGA

# Si es menor a 60
# if ncuant >= 0 and ncuant < 60:
#    ncuanl = "D"
# NO SE COLOCA ADENTO POR QUE NO ES OTRA CONDICION
# elif ncuant >= 60 and ncuant < 80:
#    ncuanl = "C"
# elif ncuant >= 80 and ncuant < 90:
#    ncuanl = "B"
# elif ncuant >= 90 and ncuant <= 100:
#    ncuanl = "A"
# else:
#    print("error. nota invalida")
#    ncuanl = ""


# FORMA_ACORTADA

if ncuant < 0 or ncuant > 100:
    print("error nota invalida")
    ncual = ""
elif ncuant < 60:
    ncuanl = "D"
elif ncuant < 80:
    ncuanl = "C"
elif ncuant < 90:
    ncuanl = "B"
else:
    ncual = "A"

print("\n", "-" * 30)
print("nombre: ", nom)
print(f"nota cuantitativa {ncuant:.1f}")
print(f"nota cuanlitativa {ncuanl}")
