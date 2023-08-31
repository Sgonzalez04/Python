s = "yo soy tu padre"

print(s[7]) #imprime t
print(s[-8]) #Imprime t

# s[7] = "s" no se puede cambiar

#recorrido de la cadena por su indice
for i in range(len(s)):  #len es tamaño de cadena
    print(s[i], end=", ") 

print()

#recorrido de la cadena por sus elementos
for elem in s:
    print(elem, end=" - ")

