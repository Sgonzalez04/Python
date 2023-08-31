p = int(input("introdusca un numero para p: "))
q = int(input("introdusca un numero para q: "))

for p in range(0, 100):  # si p esta en rango de 0 a 100
    for q in range(0, 100):  # si q esta en rago de 0 a 100
        if p**3 + q**4 - 2 * p**2 < 680:  # si p^3 + q^4 - 2*p^2 y < 680 imprima
            print(f"p = {p}, q= {q}, p^3 + q^4 - 2*p^2 = {p**3 + q**4 - 2*p**2}")
