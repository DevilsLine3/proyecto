from numpy import*

materia1_cant_est=int(input("Ingrese la cantidad de estudiantes de la materia 1: "))
array_materia1_vacio=empty(materia1_cant_est)

for i in range(materia1_cant_est):
    calificacion=float(input(f"Ingrese la nota del estudiante: "))
    array_materia1_vacio[i]=calificacion
    promedio=array_materia1_vacio.mean()
print("notas de los estudiantes: ",array_materia1_vacio)
print("promedio de la materia: ",promedio)

materia2_cant_est=int(input("Ingrese la cantidad de estudiantes de la materia 2: "))
array_materia2_vacio=empty(materia2_cant_est)

for i in range(materia2_cant_est):
    calificacion=float(input(f"Ingrese la nota del estudiante: "))
    array_materia2_vacio[i]=calificacion
    promedio=array_materia2_vacio.mean()
print("notas de los estudiantes: ",array_materia2_vacio)
print("Promedio de la materia: ", promedio)

materia3_cant_est=int(input("Ingrese la cantidad de estudiantes de la materia 3: "))
array_materia3_vacio=empty(materia3_cant_est)

for i in range(materia3_cant_est):
    calificacion=float(input(f"Ingrese la nota del estudiante: "))
    array_materia3_vacio[i]=calificacion
    promedio=array_materia3_vacio.mean()
print("notas de los estudiantes: ",array_materia3_vacio)
print("Promedio de la materia: ", promedio)


nota_maxima1=array_materia1_vacio[0]
for maxima_calificacion in array_materia1_vacio:
    if maxima_calificacion > nota_maxima1:
        nota_maxima1=maxima_calificacion

print("la nota maxima es de: ",nota_maxima1)

nota_maxima2=array_materia2_vacio[0]
for maxima_calificacion in array_materia2_vacio:
    if maxima_calificacion > nota_maxima2:
        nota_maxima2=maxima_calificacion

print("la nota maxima es de: ",nota_maxima2)

nota_maxima3=array_materia3_vacio[0]
for maxima_calificacion in array_materia3_vacio:
    if maxima_calificacion > nota_maxima3:
        nota_maxima3=maxima_calificacion

print("la nota maxima es de: ",nota_maxima3)

max1=array_materia1_vacio.max()
max2=array_materia2_vacio.max()
max3=array_materia3_vacio.max()

nota_max=array([max1,max2,max3]).max()
print("la nota maxima de todas las materias es de: ",nota_max)