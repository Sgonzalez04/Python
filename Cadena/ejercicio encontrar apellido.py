#nom = "David Alfonso Gomez Pedraza"
# optener el primer apellido
#___primapel = nom.split()[2]  # el espacio 2 veces para hallar el apellido
#___print(primapel)

#___primapel = nom.split("o") #no incluye la o
#___print(primapel) 

cor="carlosrueda@gmail.com"
#primapel= cor.split("a")[1] #que dominios de correos son
primapel=cor.split("@")[1].split(".")[1].upper() #se pare todos los puntos y deme el 2 ".com"
#.upper pasa todo a mayuscula
print(primapel)