from numpy import*
#lista de mejores productos

#Obtener las dimenciones del array del usuario 
array_vacio2=set()
filas=int(input("Ingrese el número de productos: "))
#crear un array vacio de dimensiones especificas
array_vacio2=empty((filas,2))
#llenar el array con datos ingresados por el usuario
for i in range(filas):
    valor=float(input("Ingrese  el costo: "))
    peso=float(input("Ingrese el peso: "))
    array_vacio2[i,0]=valor
    array_vacio2[i,1]=peso
print("array llenado: ")
print(array_vacio2)

def buscar_mejor_producto():
    mejor_producto=array_vacio2[0][0]
    menor_peso=array_vacio2[0][1]
    fila_max,columna_max=0,0
    for fila in range(len(array_vacio2)):
        if array_vacio2[fila][1] <= menor_peso and array_vacio2[fila][0]>=mejor_producto:
            menor_peso=array_vacio2[fila][1]
            fila_max,columna_max=fila,0
            print("el mejor producto deacuerdo el peso es:",menor_peso)
            mejor_producto=array_vacio2[fila][0]
            print("el que tiene mejor precio entre los mejores es", mejor_producto)
            mejores_productos=list[{mejor_producto,menor_peso}]
            fila_max,columna_max=fila,0
            print(mejores_productos,"mejores productos")
    mejores_productos=list[{mejor_producto,menor_peso}]
    print("el mejor producto de acuerdo el precio y peso es:", mejor_producto,"con peso de ",menor_peso)
    print("el mejor producto de acuerdo el precio se encuentra en la posicion: ",(fila_max,columna_max))
buscar_mejor_producto()


