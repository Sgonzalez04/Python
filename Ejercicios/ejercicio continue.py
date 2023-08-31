for i in range(20):
    if i % 5 == 0:
        # no coloca los numeros con multiplo de 5 funciona con lo que esta debajo de continue
        continue
    print(i, end=", ")
