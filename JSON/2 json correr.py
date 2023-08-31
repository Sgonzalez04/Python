import json
with open('jsonprueba.json') as prueba:
    data=json.load(prueba)
    #se debe correr en la  terminal ubicacion correcta|
    for usuario in data["clients"]:
        print("***clients***")
        print("primer nombre:", usuario['first_name'])
        print("ultimo nombre:", usuario['last_name'])
        print("edad:", usuario['age'])
        print("cantidad:", usuario['amount'])
        print()
    
    for usuario in data["precios"]:
        print("***precios***")
        print("precio:", usuario['precio'])
        print("edad:", usuario['age'])
        print("cantidad:", usuario['amount'])
        print()

        