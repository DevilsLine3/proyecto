usuarios={};

contadora=0 #Cuenta las personas que calificaron.

#Contadoras para las películas.
cp1=0
cp2=0
cp3=0
cp4=0
cp5=0

#Contadora calificaciones para las películas.
cc1=0
cc2=0
cc3=0
cc4=0
cc5=0


while True:
    califica={}
    print("\nOpciones:")
    print("1.Nombre")
    print("2.Película a votar y calificación")
    print("3.Ver el promedio de calificaciones")
    print(".Salir")
    
    opcion=int(input("Seleccione una opción:  "));
    
    
    if opcion == 1:
        nombre_usuario=str(input("Digite su nombre: "))
        
        usuarios.setdefault(nombre_usuario);
        print(usuarios)
        
    elif opcion == 2:
        print("Recuerde,solo puede calificar 2 películas.")
        
        print("\nOpciones:")
        print(" Película 1")
        print(" Película 2")
        print(" Película 3")
        print(" Película 4 ")
        print(" Película 5")
        for calificaciones in range(2):
            pelicula=str(input("Digite la película que desea calificar: "))
            calificacion=float(input("Digite la calificación de 1.0 a 5.0: "))
            if (pelicula=="pelicula 1"):
                cp1=cp1+1
                cc1=cc1+calificacion
            elif(pelicula == "pelicula 2"):
                cp2=cp2+1
                cc2=cc2+calificacion
            
            elif(pelicula=="pelicula 3"):
                cp3=cp3+1
                cc3=cc3+calificacion
            
            elif(pelicula=="pelicula 4"):
                cp4=cp4+1
                cc4=cc4+calificacion
            
            elif(pelicula=="pelicula 5"):
                cp5=cp5+1
                cc5=cc5+calificacion
            
            else:
                print("No existe esta película, intenta nuevamente con una opción válida")
            contadora=contadora+1    
        califica.update({pelicula:calificacion}) 
        print(califica)
        usuarios.update({nombre_usuario:califica})
        print(usuarios)
    elif opcion == 3:
            
            print("El promedio de las calificaciones de todas las películas es: ")

#----------------------------------------------------Película 1----------------------------------------------
            
            if cp1 >=1:
                pp1=(cp1/contadora)
                print("Película 1: ", pp1,"Promedio de las personas que han visto esta pelicula")
                pc1=(cc1/cp1)
                print("El promedio de calificación de la película es de: ",pc1)
            else:
                print("Película 1: Ninguna persona califico esta película.")
                print("El promedio de calificaciones es de 0")

#----------------------------------------------------Película 2----------------------------------------------

            if cp2 >=1:
                pp2=(cp2/contadora)
                print("Película 2: ", pp2,"Promedio de las personas que han visto esta pelicula")
                pc2=(cc2/cp2)
                print("El promedio de calificación de la película es de: ",pc2)
            else:
                print("Película 2: Ninguna persona califico esta película.")
                print("El promedio de calificaciones es de 0")

#----------------------------------------------------Película 3----------------------------------------------
            
            if cp3 >=1:
                pp3=(cp3/contadora)
                print("Película 3: ", pp3,"Promedio de las personas que han visto esta pelicula")
                pc3=(cc3/cp3)
                print("El promedio de calificación de la película es de: ",pc3)
            else:
                print("Película 3: Ninguna persona califico esta película.")
                print("El promedio de calificaciones es de 0")
            
#----------------------------------------------------Película 4----------------------------------------------           
            if cp4 >=1:
                pp4=(cp4/contadora)
                print("Película 4: ", pp4,"Promedio de las personas que han visto esta pelicula")
                pc4=(cc4/cp4)
                print("El promedio de calificación de la película es de: ",pc4)
            else:
                print("Película 4: Ninguna persona califico esta película.")
                print("El promedio de calificaciones es de 0")

#----------------------------------------------------Película 5---------------------------------------------- 
            if cp5 >=1:
                pp5=(cp5/contadora)
                print("Película 5: ", pp5,"Promedio de las personas que han visto esta pelicula")
                pc5=(cc5/cp5)
                print("El promedio de calificación de la película es de: ",pc5)
            else:
                print("Película 5: Ninguna persona califico esta película.")
                print("El promedio de calificaciones es de 0")


    elif opcion == 4:
        print("Gracias")
        break
    else:
        print("Opción no válida")