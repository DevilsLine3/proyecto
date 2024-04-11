from numpy import*
filas=int(input("Ingrese el número de estudiantes: "))
columnas=int(input("Ingrese el número de materias: "))

array_vacio=empty((filas,columnas))

for i in range(filas):
    for j in range(columnas):
        valor=float(input(f"Ingrese la nota de la materia({j}): "))
        array_vacio[i,j]=valor
print(array_vacio)
suma_todo=sum(array_vacio)
print("la suma de todos los elementos es: ",suma_todo)
prom_todo=mean(array_vacio)
print("promedio",prom_todo)

suma_por_columna=sum(array_vacio,axis=0)
print("suma por filas",suma_por_columna)

suma_por_filas=sum(array_vacio,axis=1)
print("suma de columnas",suma_por_filas)

prom_columna=mean(array_vacio,axis=0)
print("promedio de columna",prom_columna)

prom_fila=mean(array_vacio,axis=1)
print("promedio de las filas",prom_fila)