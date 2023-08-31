def findlst(lst, elem):
    # encuentra el elemento y devuelve la posicion
    # devuelve none si no lo encuentra

    for i in range(len(lst)):  # len recorre por posicion y le da un numero
        if elem == lst[i]:  # si el elemento esta en la lista
            return i  # muestra la posicion en la q esta

    return None  # si no esta muestra none


def existLst(lst, elem):
    # devuelve true si existe en la lista
    # devuelve false si no existe en la lista
    for e in lst:
        if elem == e:
            return True  # si el elemento esta muestre true
    return False  # si no esta false
