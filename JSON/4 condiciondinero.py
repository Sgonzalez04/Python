import json
with open('ahorradores.json') as prueba:
    data=json.load(prueba)
    for usuario in data["cliente"]:
        dinero = usuario['Saldo']
        condicion=35000000
        if dinero > condicion:
            print("***clients***")
            print("Numero de cuenta:", usuario['NumCuenta'])
            print("saldo:", usuario['Saldo'])
            print()
