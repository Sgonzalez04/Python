# funciones
# pueden tener nombres pero es pereferible colocar los que se asocien
# un programa es dividido por muchas funciones.

# es como un carro al que se le pueden cambiar las partes o agregar
# las partes son las funciones para que funcione

# deben poder reunirse y funcionar bien (acoplamiento y cohesion)


def suma(num1, num2):
    r = num1 + num2
    return r


# def para definir luego nombre, que necesita para funcionar,:
# procedimiento r= 1+2
# return es lo que debuelve y la variable de lo que debuelve

# lo puede dar un por un resultado o una fucion
resultado = suma(2, 4)
print(resultado)  # o print(suma(2, 4))
