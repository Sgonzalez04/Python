print("hola mundo".upper())  # convierte todo en mayuscula

print("HOLA MUNDO".lower())  # convierte todo en minuscula

print("hola mundo".capitalize())  # convierte la primera en mayuscula

print("hola mundo".count("mundo"))  # cuenta cantas veces aparece la palabra o numero en una cadena

a= "Hola"
print(a.find("la",1,4)) #busca la palabra en la cadena si no la encuentra de -1
#cuenta de 1 hasta 3 la ultima no se incliuye
#rta = posicion 2


print("hola mundo mundo mundo" .rfind("mundo"))
#rta la ultima en donde esta es 17

c="100"
c.isdigit #si esta todo en numeros?

d="qwetr"#si esta todo en letras?
d.isalnum

b="ABC10034po"
b.isalpha()# si es solo alfabetico o letras

"Hola Mundo" .istitle() #si esta la primera palabra de todo en mayuscula

"hola  mundo" .startswitch("mola") #si la cadena empieza con la subcadena

"hola mundo" .endswith("mundo") #si la cadena termina con lo de la subcadena

",".join ("hola mundo") #en la mitad de cada uno se coloca ","

"     hola mundo    ".strip()#quita espacios al principio y al final

"hola mundo mundo mundo mundo mundo".replace("mundo"," ",4) #remplaza la primera por la segunda, 4 veces


