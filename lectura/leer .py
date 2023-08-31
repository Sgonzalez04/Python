import io
print("digite el nombre del archivo")
nombre = input() #colocar nombre del archivo
try: #intenta leer el texto
    archivo_txt = open(nombre + 'txt','r',encoding='utf-8') #el nombre se escribe en txt, utf-8 es para que lea lineas especiales
    numlinea = int(input("ingrese la linea del archivo")) #linea del archivo que desea leer
    lineas= archivo_txt.readlines() #lo guarda en la variable lineas
    archivo_txt.close() #cierra el archivo tx-1
    print(lineas[numlinea - 1]) #en la variable lineas y lista num lineas comienze desde 1(comienza en 0 defecto)
except: #si no se cumple todo lo de try
    print("ingreso mal el nombre")