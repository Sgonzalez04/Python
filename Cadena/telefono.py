tel = input("ingrese telefono con formato(+codpais-num-ext): ")
parttle = tel.split("-") #separa todo por -

#validar
if len(parttle) == 3 and parttle[0].startswith("+") and \
    len(parttle[0]) == 3 and parttle[0][1:].isdigist() and \
        parttle [1]. isdigit() and len(parttle[2])==2 and \
            parttle[2].isdigit():
                print(parttle[1])
else:
    print("formato invalido")


#si pattele es 3 en la primera palabra tiene +
#si en parttle desde 0 tiene 3, si la lista comenzando desde 0 hasta el final de la parte 1(Se separa por -)
#si parte 2 del texto es digito y tiene la parte 3 es solo 2
#si la parte 3 del texto es un digito
# impirma la parte 2 