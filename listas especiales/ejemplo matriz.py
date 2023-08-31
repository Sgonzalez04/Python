import random #crea al azar

def impimirMat(m):
    for f in range(len(m)): #longitud de las filas
        for c in range(len(m[f])): #en cada fila cuantas columnas tiene
            print (m[f][c], end="\t") #imprima la fila y columna
        print("")

def prodMaxSem(m):
    vtasProd=[] #ventas de productos se almacena y comienza vacia
    for f in range(len(m)): #empieza 0, hace que se repita filas que hay
        suma = 0
        for c in range(len(m[f])): #suma las columnas
            suma+=m[f][c] #suma las filas con las columas
        vtasProd.append(suma)#se agrega el resultado de la suma
    
    vtasmax = max(vtasProd) #saca el que mas valio en las columas
    prodMaxVtas = vtasProd.index(vtasmax) #saca cual es la fila de 0 a #
    return prodMaxVtas

def llenarMatriz(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            m[f][c] = random.randint(18,119) #escoger: int(input("venta dia#", c+1))

            #Matriz con f columna de un numero al azar entre 18 y 119

def crearMatriz(fil, col):
    m = []#lista vacia
    for i in range (fil):
        c = [0]*col #comienza todo en 0
        m.append(c)
        
    return m
    #crear una lista con cantidad de columanas"col" (Semanas)
    #recorre por las filas"fil

mat = crearMatriz(5,7) #5 filas #7 columnas
impimirMat(mat)
llenarMatriz(mat)

print("\n el producto que genera")