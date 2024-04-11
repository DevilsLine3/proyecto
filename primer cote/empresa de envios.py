from numpy import*
#camiones de tranporte y su peso maximo
print("Bienvenido por favor ingrese los siguientes datos: ")
carga_max=float(input("Ingrese la carga maxima del camion 1: "))
carga_max2=float(input("Ingrese la carga maxima del camion 2: "))
carga_max3=float(input("Ingrese la carga maxima del camion 3: "))
#numero de cajas de envio por prioridad
cajas_en_total=int(input("Ingree la cantidad de paquetes en total: "))
#Llenado de diccionarios deacuerdo la prioridad
Envio_priori_1=[]
Envio_priori_2=[]
Envio_priori_3=[]
cont1,cont2,cont3=0,0,0
for N_cajas in range(cajas_en_total):
    caja_prioridad_1 = int(input("Ingrese la cantidad de cajas de la prioridad 1: "))
    if caja_prioridad_1<=cajas_en_total:
        for N_cajas_p1 in range(caja_prioridad_1):
            peso=int(input("Ingrese el peso del paquete"))
            nombre_paq=(f"paquete numero{N_cajas_p1+1}")
            cont1=cont1+1
            Envio_priori_1.append([nombre_paq,peso])
            cajas_en_total=cajas_en_total-caja_prioridad_1
    else:
        print("error")
    print(Envio_priori_1)
    caja_prioridad_2 = int(input("Ingrese la cantidad de cajas de la prioridad 2: "))
    if caja_prioridad_2 <=cajas_en_total:
        for N_cajas_p2 in range(caja_prioridad_2):
            peso=int(input("Ingrese el peso del paquete"))
            nombre_paq=(f"paquete numero{N_cajas_p2+1}")
            cont2=cont2+1
            Envio_priori_2.append([nombre_paq,peso])
            cajas_en_total=cajas_en_total-caja_prioridad_2
    else:
        print("error")
    print(Envio_priori_2)
    caja_prioridad_3 = int(input("Ingrese la cantidad de cajas de la prioridad 3: "))
    if caja_prioridad_3<=cajas_en_total:
        for N_cajas_p3 in range(caja_prioridad_3):
            peso=int(input("Ingrese el peso del paquete"))
            cont3=cont3+1
            nombre_paq=(f"paquete numero{N_cajas_p3+1}")
            Envio_priori_3.append([nombre_paq,peso])
            cajas_en_total=cajas_en_total-caja_prioridad_3
    else:
        print("error")
    print(Envio_priori_3)
