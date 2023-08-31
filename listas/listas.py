# listas

lista_numeros = [10, 15, 20, 30, 40]
lista_numeros = [2]
rta = 20

lista_nombres = ["sergio", "catalina", "silvia", "ivan", "elsa"]
lista_nombres[0, 2]
rta = "sergio, catalina"

lista_pares = list(range(2, 20, 2))
lista_pares_rta = [2, 4, 6, 8, 10, 12, 14, 16, 18]

lista = [10, 20, "juan", 30, "sergio"]

lista.append(40)
[10, 20, "juan", 30, "sergio", 40]
lista.append("paula")
[10, 20, "juan", 30, "sergio", 40, "páula"]
lista.extend([60, 80])
[10, 20, "juan", 30, "sergio", 40, "páula", 60, 80]
lista.insert(1, "luis")
[10, "luis", "juan", 30, "sergio", 40, "páula", 60, 80]
lista.pop(4)
30
[10, 20, "juan", "sergio", 40, "páula", 60, 80]
lista.remove("sergio")
[10, 20, "juan", 40, "páula", 60, 80]
