for pri in range(100, 501):
    esprimo = True
    for d in range(2, pri):
        if pri % d == 0:
            esprimo = False
            # no se coloca mas
            break

    if esprimo == True:
        # todo numero dividido en 10 que de 3 termina en 3 esto es valido para primos
        if pri % 10 == 3:
            continue
        print(pri, end=", ")
