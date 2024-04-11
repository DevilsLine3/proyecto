from numpy import*

#Obtener la longitud del del array del usuario
longuitud=int(input("ingrese la longitud del arrray: "))

#crear un array vacio de la longuitud vacia
array_vacio=empty(longuitud)

#llenar el array con datos ingresados por le usuario
for i in range(longuitud):
    valor=float(input(f"Ingrese el valor para la posición {i}: "))
    array_vacio[i]=valor

print("array llenado")
print(array_vacio)

#Obtener las dimenciones del array del usuario 
filas=int(input("Ingrese el número del filas: "))
columnas=int(input("Ingrese el número de columnas: "))
#crear un array vacio de dimensiones especificas
array_vacio2=empty((filas,columnas))
#llenar el array con datos ingresados por el usuario
for i in range(filas):
    for j in range(columnas):
        valor=float(input(f"Ingrese el valor para la posición ({i},{j}): "))
        array_vacio2[i,j]=valor
print("array llenado: ")
print(array_vacio2)

#crear un array de una sola dimension
array_una_sola_dimension = array([5,2,8,1,9,3])
#encontrar el número mas grande 
maximo=array_una_sola_dimension[0]
#suponemos que el primer elemeto es el maximo
for num in array_una_sola_dimension:
    if num >maximo:
        maximo=num
print("el número más grande en el array es de: ",maximo)

#crear una matriz
matriz=array([[5,2,8],[1,9,3],[12,6,4]])
#iniciar el maximo y su posicion y su posicion
maximo =matriz[0][0]#busca el numero mas grande
fila_max,columna_max=0,0#muestra a posicion del numero mas grande

#encontrar el numero mas grande y su posicion
for fila in range(len(matriz)):
    for columna in range(len(matriz[0])):
        if matriz[fila][columna] > maximo:
            maximo=matriz[fila][columna]
            fila_max,columna_max=fila,columna
print("el numero mas grande en la matriz es: ", maximo)
print("se encuentra en la posicion: ",(fila_max,columna_max))