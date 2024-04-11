
peliculas={}


inicio=int(input("Si desea ingresar a nuestro servicio de peliculas digite 1, si no digite 2: "))
while inicio==1:   
    while True:
        contener=[]
        nombre=str(input("Estimado cliente, ingrese su nombre"))
        peliculas.setdefault(nombre)
        print(peliculas)
        for inte in range(2):
            print("seleccione un tipo de pelicula:")
            print("1/infantil")
            print("2/terror")
            print("3/romantica")
            print("4/accion")
            print("5/comedia")
            opc=int(input(""))
            if opc==1:
                p="pelicula infantil"
                cal=float(input("Califique la pelicula entre 1 A 5"))
                
            elif opc==2:
                p="pelicula de terror"
                cal=float(input("Califique la pelicula entre 1 A 5"))
                    
            elif opc==3:
                p="pelicula romantica"
                cal=float(input("Califique la pelicula entre 1 A 5"))
                    
                
            elif opc==4:
                p="pelicula de accion"
                cal=float(input("Califique la pelicula entre 1 A 5"))
                    
            elif opc==5:
                p="pelicula chistosa"
                cal=float(input("Califique la pelicula entre 1 A 5"))
            print(contener)
            contener.append({p,cal})
            print(contener)
            
        peliculas.update({nombre:contener})   
        print(peliculas)
        break
    inicio=int(input("Si desea ingresar a nuestro servicio de peliculas digite 1, si no digite 2: "))  
