usuarios={};

nuevo={};

while True:
    califica={};
    print("\nOpciones:")
    print("1.Nombre")
    print("2.Película a votar y calificación")
    print("3.Salir")
    
    opcion=int(input("Seleccione una opción:  "));
    
    if opcion == 1:
        nombre_usuario=str(input("Digite su nombre: "))
        
        usuarios.setdefault(nombre_usuario,0);#pude ir solo el nombre del usuario y no pasa nada
        print(usuarios)
        
    elif opcion == 2:
        print("Recuerde,solo puede calificar 2 películas.")
        
        for calificaciones in range(2):
            
            print("\nOpciones:")
            print(" Película 1")
            print(" Película 2")
            print(" Película 3")
            print(" Película 4 ")
            print(" Película 5")
            pelicula=str(input("Digite la película que desea calificar: "))
            calificacion=float(input("Digite la calificación de 1.0 a 5.0: "))
        
        # Aqui irian mejor unas contadoras para que velga la rebundancia cuenten las veces que se han votado
        # cada pelicula los puede hacer con if("nom_peli"=="peli_1") y le va contando para el promedio 
        # y si no me equivoco tambien podria ir un conjunto donde agrege las calificaciones para ir haciendo
        # ese promedio
        
        
        califica.setdefault(pelicula,calificacion)#Aqui es mejor un .update({variable_1:variable_2})
        #                                         si lo quiere como diccionario 
        print(califica)
        
    elif opcion == 3:
        
        print("Gracias")
        break
    
    else:
        print("Opción no válida")
    #puede ponre aqui para que se valla llenando el dicionario de usuarios 
    #se opdnria asi usuario.update({nombre_usuario:califica})
    # y le pondria en terio asi {'justin': {'peli 1': '3', 'peli 2': '3'}}
    #y ya tendriamos el diccionario asi
#nuevo={usuarios,califica}
nuevo=(nombre_usuario,[pelicula,calificacion])
print(nuevo)


interseccion=set()

p1=[]
for usuario,pelicula in nuevo.items():
    if pelicula['pelicula'] == 'pelicula 1':
        p1.append(usuario)
    
print('película1',p1)

p2=[]
for usuario,pelicula in nuevo.items():
    if pelicula['pelicula'] == 'pelicula 2':
        p2.append(usuario)
    
print('película1',p2)   


p3=[]
for usuario,pelicula in nuevo.items():
    if pelicula['pelicula'] == 'pelicula 3':
        p3.append(usuario)
    
print('película1',p3)

p4=[]
for usuario,pelicula in nuevo.items():
    if pelicula['pelicula'] == 'pelicula 4':
        p4.append(usuario)
    
print('película1',p4)

p5=[]
for usuario,pelicula in nuevo.items():
    if pelicula['pelicula'] == 'pelicula 5':
        p5.append(usuario)
    
print('película1',p5)

interseccion=set(p1,p2,p3,p4,p5)


pr=set();#promedio
pr1=(p1.mean());  
pr2=(p2.mean());
pr3=(p3.mean());
pr4=(p4.mean());
pr5=(p5.mean());

print("El promedio de calificación de la película 1 es: ",p1)
print("El promedio de calificación de la película 2 es: ",p2)
print("El promedio de calificación de la película 3 es: ",p3)
print("El promedio de calificación de la película 4 es: ",p4)
print("El promedio de calificación de la película 5 es: ",p5)