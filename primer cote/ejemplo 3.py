from numpy import*

nuevo_vector=array([1,2,3,6,4,8])#vector
segundo_vector=array([6,8,7,6,9,3])

#matriz=array([[3,7,8,9],[10,15,20,30],[7,21,10,15]])

matriz=array([[4,5,9,4,10],[8,100,15,20,78],[5,89,45,78,5]])
matriz_2=array([[4,9,6],[2,1,3],[9,4,6],[6,7,5],[10,6,7]])

promedio=nuevo_vector.mean()
print(nuevo_vector.mean())

maximo=nuevo_vector.max()
print(maximo)
minimo=nuevo_vector.min()
print(minimo)
print("suma")
suma=nuevo_vector.sum()
print(suma)

print("cantidad de elementos")
cantidad_elementos=len(nuevo_vector)
print(cantidad_elementos)


print("suma de vectores")
suma_vectores=nuevo_vector+segundo_vector
print(suma_vectores)

print("multiplicacion escalar")
multi_escalar=segundo_vector*3
print(multi_escalar)

print("multiplicacion vectorial")
multi_vectorial=nuevo_vector*segundo_vector
print(multi_vectorial)

print("posicion del vector")
print(nuevo_vector[3])

for i in nuevo_vector:
    print(i)

print("matriz por escalar")
multiplicacion_matriz_escalar=matriz*2
print(multiplicacion_matriz_escalar)

print("multiplicacion de matrizes")
multiplicacion_matriz_matriz=dot(matriz,matriz_2)
print(multiplicacion_matriz_matriz)


print("buscar elemento en un vector")
if 6 in segundo_vector:
    print("elemento encontrado")
else:
    print("no se encuentra ese elemento")

print("buscar dentro de una matriz")
if 5 in matriz:
    print("elemeto econtrado")
else:
    print("no encontrado")

#fila y columma para matriz en python
fila,columna=where(matriz==10) 
print(fila,columna)

#