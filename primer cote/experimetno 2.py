from numpy import*
goles_afavor_equipo_1,goles_afavor_equipo_2,goles_afavor_equipo_3,goles_afavor_equipo_4=0,0,0,0
goles_encontra_equipo_1,goles_encontra_equipo_2,goles_encontra_equipo_3,goles_encontra_equipo_4=0,0,0,0
cont_puntos_equipo_1,cont_puntos_equipo_2,cont_puntos_equipo_3,cont_puntos_equipo_4=0,0,0,0
cant_equipo_1,cant_equipo_2,cant_equipo_3,cant_equipo_4=0,0,0,0
while True:
    print("1. Llenado de partidos y mostrar ganador")
    print("2. Salir")
    menu=int(input("Opciones: "))
    
    match menu:
        case 1:
            print("Ingrese el resultado del partido entre Equipo 1 y Equipo 2:")
            cant_equipo_1=int(input("Ingrese la cantidad de goles del Equipo 1: "))
            cant_equipo_2=int(input("Ingrese la cantidad de goles del Equipo 2: "))
            if (cant_equipo_1>cant_equipo_2):
                puntos_equipo_1=2
                puntos_equipo_2=0
                #contadora a favor 
                goles_afavor_equipo_1=goles_afavor_equipo_1+cant_equipo_1
                goles_afavor_equipo_2=goles_afavor_equipo_2+cant_equipo_2
                #contadora encontra
                goles_encontra_equipo_2=goles_encontra_equipo_2+cant_equipo_1
                goles_encontra_equipo_1=goles_encontra_equipo_1+cant_equipo_2
                #contadora de puntos
                cont_puntos_equipo_1=cont_puntos_equipo_1+puntos_equipo_1
                cont_puntos_equipo_2=cont_puntos_equipo_2+puntos_equipo_2
            elif(cant_equipo_2>cant_equipo_1):
                puntos_equipo_2=2
                puntos_equipo_1=0
                #goles a favor
                goles_afavor_equipo_2=goles_afavor_equipo_2+cant_equipo_2
                goles_afavor_equipo_1=goles_afavor_equipo_1+cant_equipo_1
                #goles encontra
                goles_encontra_equipo_1=goles_encontra_equipo_1+cant_equipo_2
                goles_encontra_equipo_2=goles_encontra_equipo_2+cant_equipo_1
                #contadora de puntos
                cont_puntos_equipo_1=cont_puntos_equipo_1+puntos_equipo_1
                cont_puntos_equipo_2=cont_puntos_equipo_2+puntos_equipo_2
            elif(cant_equipo_1==cant_equipo_2):
                puntos_equipo_1=1
                puntos_equipo_2=1
                #goles a favor
                goles_afavor_equipo_1=goles_afavor_equipo_1+cant_equipo_1
                goles_afavor_equipo_2=goles_afavor_equipo_2+cant_equipo_2
                #goles encontra
                goles_encontra_equipo_1=goles_encontra_equipo_1+cant_equipo_2
                goles_encontra_equipo_2=goles_encontra_equipo_2+cant_equipo_1
                #contadora de puntos
                cont_puntos_equipo_1=cont_puntos_equipo_1+puntos_equipo_1
                cont_puntos_equipo_2=cont_puntos_equipo_2+puntos_equipo_2
                print("Goles a favor")
            print(goles_afavor_equipo_1,"favor equi1")
            print(goles_afavor_equipo_2,"favor equi 2")
            print(goles_afavor_equipo_3,"favor equi 3")
            print(goles_afavor_equipo_4,"favor equi 4")
            print("goles encontra")
            print(goles_encontra_equipo_1,"contra 1")
            print(goles_encontra_equipo_2,"contra 2")
            print(goles_encontra_equipo_3,"contra 3")
            print(goles_encontra_equipo_4,"contra 4")
            print("Ingrese el resultado del partido entre Equipo 1 y Equipo 3:")
            cant_equipo_1=int(input("Ingrese la cantidad de goles del Equipo 1: "))
            cant_equipo_3=int(input("Ingrese la cantidad de goles del Equipo 3: "))
            if (cant_equipo_1>cant_equipo_3):
                puntos_equipo_1=2
                puntos_equipo_3=0
                #contadora a favor 
                goles_afavor_equipo_1=goles_afavor_equipo_1+cant_equipo_1
                #contadora encontra
                goles_encontra_equipo_3=goles_encontra_equipo_3+cant_equipo_3
                #contadora de puntos
                cont_puntos_equipo_1=cont_puntos_equipo_1+puntos_equipo_1
                cont_puntos_equipo_3=cont_puntos_equipo_3+puntos_equipo_3
            elif(cant_equipo_3>cant_equipo_1):
                puntos_equipo_3=2
                puntos_equipo_1=0
                #contadora a favor 
                goles_afavor_equipo_3=goles_afavor_equipo_3+cant_equipo_3
                #contadora encontra
                goles_encontra_equipo_1=goles_encontra_equipo_1+cant_equipo_1
                #contadora de puntos
                cont_puntos_equipo_1=cont_puntos_equipo_1+puntos_equipo_1
                cont_puntos_equipo_3=cont_puntos_equipo_3+puntos_equipo_3
            elif(cant_equipo_1==cant_equipo_3):
                puntos_equipo_1=1
                puntos_equipo_3=1
                goles_afavor_equipo_1=goles_afavor_equipo_1+cant_equipo_1
                goles_afavor_equipo_3=goles_afavor_equipo_3+cant_equipo_3
                #contadora de puntos
                cont_puntos_equipo_1=cont_puntos_equipo_1+puntos_equipo_1
                cont_puntos_equipo_3=cont_puntos_equipo_3+puntos_equipo_3
                print("Goles a favor")
            print(goles_afavor_equipo_1)
            print(goles_afavor_equipo_2)
            print(goles_afavor_equipo_3)
            print(goles_afavor_equipo_4)
            print("goles encontra")
            print(goles_encontra_equipo_1)
            print(goles_encontra_equipo_2)
            print(goles_encontra_equipo_3)
            print(goles_encontra_equipo_4)
            print("Ingrese el resultado del partido entre Equipo 1 y Equipo 4:")
            cant_equipo_1=int(input("Ingrese la cantidad de goles del Equipo 1: "))
            cant_equipo_4=int(input("Ingrese la cantidad de goles del Equipo 4: "))
            if (cant_equipo_1>cant_equipo_4):
                puntos_equipo_1=2
                puntos_equipo_4=0
                #contadora a favor 
                goles_afavor_equipo_1=goles_afavor_equipo_1+cant_equipo_1
                #contadora encontra
                goles_encontra_equipo_4=goles_encontra_equipo_4+cant_equipo_4
                #contadora de puntos
                cont_puntos_equipo_1=cont_puntos_equipo_1+puntos_equipo_1
                cont_puntos_equipo_4=cont_puntos_equipo_4+puntos_equipo_4
            elif(cant_equipo_4>cant_equipo_1):
                puntos_equipo_4=2
                puntos_equipo_1=0
                #contadora a favor 
                goles_afavor_equipo_4=goles_afavor_equipo_4+cant_equipo_4
                #contadora encontra
                goles_encontra_equipo_1=goles_encontra_equipo_1+cant_equipo_1
                #contadora de puntos
                cont_puntos_equipo_1=cont_puntos_equipo_1+puntos_equipo_1
                cont_puntos_equipo_4=cont_puntos_equipo_4+puntos_equipo_4
            elif(cant_equipo_1==cant_equipo_4):
                puntos_equipo_1=1
                puntos_equipo_4=1
                goles_afavor_equipo_1=goles_afavor_equipo_1+cant_equipo_1
                goles_afavor_equipo_4=goles_afavor_equipo_4+cant_equipo_4
                #contadora de puntos
                cont_puntos_equipo_1=cont_puntos_equipo_1+puntos_equipo_1
                cont_puntos_equipo_4=cont_puntos_equipo_4+puntos_equipo_4
                print("Goles a favor")
            print(goles_afavor_equipo_1)
            print(goles_afavor_equipo_2)
            print(goles_afavor_equipo_3)
            print(goles_afavor_equipo_4)
            print("goles encontra")
            print(goles_encontra_equipo_1)
            print(goles_encontra_equipo_2)
            print(goles_encontra_equipo_3)
            print(goles_encontra_equipo_4)
            print("Ingrese el resultado del partido entre Equipo 2 y Equipo 3:")
            cant_equipo_2=int(input("Ingrese la cantidad de goles del Equipo 2: "))
            cant_equipo_3=int(input("Ingrese la cantidad de goles del Equipo 3: "))
            if (cant_equipo_2>cant_equipo_3):
                puntos_equipo_2=2
                puntos_equipo_3=0
                #contadora a favor 
                goles_afavor_equipo_2=goles_afavor_equipo_2+cant_equipo_2
                #contadora encontra
                goles_encontra_equipo_3=goles_encontra_equipo_3+cant_equipo_3
                #contadora de puntos
                cont_puntos_equipo_2=cont_puntos_equipo_2+puntos_equipo_2
                cont_puntos_equipo_3=cont_puntos_equipo_3+puntos_equipo_3
            elif(cant_equipo_3>cant_equipo_2):
                puntos_equipo_3=2
                puntos_equipo_2=0
                #contadora a favor 
                goles_afavor_equipo_3=goles_afavor_equipo_3+cant_equipo_3
                #contadora encontra
                goles_encontra_equipo_2=goles_encontra_equipo_4+cant_equipo_2
                #contadora de puntos
                cont_puntos_equipo_2=cont_puntos_equipo_2+puntos_equipo_2
                cont_puntos_equipo_3=cont_puntos_equipo_3+puntos_equipo_3
            elif(cant_equipo_2==cant_equipo_3):
                puntos_equipo_3=1
                puntos_equipo_2=1
                goles_afavor_equipo_2=goles_afavor_equipo_2+cant_equipo_2
                goles_afavor_equipo_3=goles_afavor_equipo_3+cant_equipo_3
                #contadora de puntos
                cont_puntos_equipo_2=cont_puntos_equipo_2+puntos_equipo_2
                cont_puntos_equipo_3=cont_puntos_equipo_3+puntos_equipo_3
            print("Goles a favor")
            print(goles_afavor_equipo_1)
            print(goles_afavor_equipo_2)
            print(goles_afavor_equipo_3)
            print(goles_afavor_equipo_4)
            print("goles encontra")
            print(goles_encontra_equipo_1)
            print(goles_encontra_equipo_2)
            print(goles_encontra_equipo_3)
            print(goles_encontra_equipo_4)
            print("Ingrese el resultado del partido entre Equipo 2 y Equipo 4:")
            cant_equipo_2=int(input("Ingrese la cantidad de goles del Equipo 2: "))
            cant_equipo_4=int(input("Ingrese la cantidad de goles del Equipo 4: "))
            if (cant_equipo_2>cant_equipo_4):
                puntos_equipo_2=2
                puntos_equipo_4=0
                #contadora a favor 
                goles_afavor_equipo_2=goles_afavor_equipo_2+cant_equipo_2
                #contadora encontra
                goles_encontra_equipo_4=goles_encontra_equipo_4+cant_equipo_4
                #contadora de puntos
                cont_puntos_equipo_2=cont_puntos_equipo_2+puntos_equipo_2
                cont_puntos_equipo_4=cont_puntos_equipo_4+puntos_equipo_4
            elif(cant_equipo_4>cant_equipo_2):
                puntos_equipo_4=2
                puntos_equipo_2=0
                #contadora a favor 
                goles_afavor_equipo_4=goles_afavor_equipo_4+cant_equipo_4
                #contadora encontra
                goles_encontra_equipo_2=goles_encontra_equipo_2+cant_equipo_2
                #contadora de puntos
                cont_puntos_equipo_2=cont_puntos_equipo_2+puntos_equipo_2
                cont_puntos_equipo_4=cont_puntos_equipo_4+puntos_equipo_4
            elif(cant_equipo_2==cant_equipo_4):
                puntos_equipo_2=1
                puntos_equipo_4=1
                goles_afavor_equipo_2=goles_afavor_equipo_2+cant_equipo_2
                goles_afavor_equipo_4=goles_afavor_equipo_4+cant_equipo_4
                #contadora de puntos
                cont_puntos_equipo_2=cont_puntos_equipo_2+puntos_equipo_2
                cont_puntos_equipo_4=cont_puntos_equipo_4+puntos_equipo_4
            print("Goles a favor")
            print(goles_afavor_equipo_1)
            print(goles_afavor_equipo_2)
            print(goles_afavor_equipo_3)
            print(goles_afavor_equipo_4)
            print("goles encontra")
            print(goles_encontra_equipo_1)
            print(goles_encontra_equipo_2)
            print(goles_encontra_equipo_3)
            print(goles_encontra_equipo_4)
            print("Ingrese el resultado del partido entre Equipo 3 y Equipo 4:")
            cant_equipo_3=int(input("Ingrese la cantidad de goles del Equipo 3: "))
            cant_equipo_4=int(input("Ingrese la cantidad de goles del Equipo 4: "))
            if (cant_equipo_3>cant_equipo_4):
                puntos_equipo_3=2
                puntos_equipo_4=0
                #contadora a favor 
                goles_afavor_equipo_3=goles_afavor_equipo_3+cant_equipo_3
                #contadora encontra
                goles_encontra_equipo_4=goles_encontra_equipo_4+cant_equipo_4
                #contadora de puntos
                cont_puntos_equipo_3=cont_puntos_equipo_3+puntos_equipo_3
                cont_puntos_equipo_4=cont_puntos_equipo_4+puntos_equipo_4
            elif(cant_equipo_4>cant_equipo_3):
                puntos_equipo_4=2
                puntos_equipo_3=0
                #contadora a favor 
                goles_afavor_equipo_4=goles_afavor_equipo_4+cant_equipo_4
                #contadora encontra
                goles_encontra_equipo_3=goles_encontra_equipo_3+cant_equipo_3
                #contadora de puntos
                cont_puntos_equipo_3=cont_puntos_equipo_3+puntos_equipo_3
                cont_puntos_equipo_4=cont_puntos_equipo_4+puntos_equipo_4
            elif(cant_equipo_4==cant_equipo_3):
                puntos_equipo_4=1
                puntos_equipo_3=1
                goles_afavor_equipo_4=goles_afavor_equipo_4+cant_equipo_4
                goles_afavor_equipo_3=goles_afavor_equipo_3+cant_equipo_3
                #contadora de puntos
                cont_puntos_equipo_3=cont_puntos_equipo_3+puntos_equipo_3
                cont_puntos_equipo_4=cont_puntos_equipo_4+puntos_equipo_4
                print("Goles a favor")
            print(goles_afavor_equipo_1)
            print(goles_afavor_equipo_2)
            print(goles_afavor_equipo_3)
            print(goles_afavor_equipo_4)
            print("goles encontra")
            print(goles_encontra_equipo_1)
            print(goles_encontra_equipo_2)
            print(goles_encontra_equipo_3)
            print(goles_encontra_equipo_4)
            array_vacio_paridos=array([[goles_afavor_equipo_1,goles_encontra_equipo_1,cont_puntos_equipo_1],
                                    [goles_afavor_equipo_2,goles_encontra_equipo_2,cont_puntos_equipo_2],
                                    [goles_afavor_equipo_3,goles_encontra_equipo_3,cont_puntos_equipo_3],
                                    [goles_afavor_equipo_4,goles_encontra_equipo_4,cont_puntos_equipo_4]])
            def ganador():
                mejor_equipo=array_vacio_paridos[0][2]
                fila_max,columna_max=0,2
                for fila in range(len(array_vacio_paridos)):
                        if array_vacio_paridos[fila][2] > mejor_equipo:
                            mejor_equipo=array_vacio_paridos[fila][2]
                            fila_max,columna_max=fila,2
                print(array_vacio_paridos)
                print("el Ganador es :", mejor_equipo)
                print("el Ganador se encuentra en la posicion: ",(fila_max,columna_max))
            ganador()
        case 2:
            break
print("Goles a favor")
print(goles_afavor_equipo_1)
print(goles_afavor_equipo_2)
print(goles_afavor_equipo_3)
print(goles_afavor_equipo_4)
print("goles encontra")
print(goles_encontra_equipo_1)
print(goles_encontra_equipo_2)
print(goles_encontra_equipo_3)
print(goles_encontra_equipo_4)