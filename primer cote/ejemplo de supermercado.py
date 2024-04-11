from numpy import*
#crear el vector vacio y indicar el usuario su longuitud
numero_de_productos_agregar=int(input("Ingrese la cantidad de productos a ingresar: "))
nuevo_producto=array(numero_de_productos_agregar)
lista=[]#si quiero llenar el array con listas hay que dejarla afuera
print("bienvenido por favor ingrese el nuevo producto y su cantidad")
for i in range(numero_de_productos_agregar):
    nombre_producto=str(input("Nombre del producto: "))
    cantidad_producto=float(input("cantidad del producto: "))
    lista.append([nombre_producto,cantidad_producto])
    nuevo_producto=array([lista])
print(nuevo_producto)

eleccion=int(input("1. para agregar un nuevo producto  2. para no: "))
if eleccion ==1:
    nuevo_producto_almacen=int(input("Ingrese la cantidad de nuevos productos a agregar: "))
    for i in range(nuevo_producto_almacen):
        nombre_prpducto=str(input("Ingrese el nombre del nuevo producto: "))
        cantidad_producto=float(input("cantidad del producto: "))
        lista.append([nombre_prpducto,cantidad_producto])
        nuevo_producto=([lista])
    print(nuevo_producto)
elif eleccion==2:
    print("no agregarste ningun producto nuevo")

eleccion_2=int(input("1. para actualizar 2. para no"))
if eleccion_2==1:
    print(nuevo_producto)
    posicion=int(input("Ingrese la posicion del producto que desea cambiar: "))
    nombre_prpducto=str(input("Ingrese el nombre del nuevo producto: "))
    cantidad_producto=float(input("cantidad del producto: "))
    delete(nuevo_producto,posicion)
    print(nuevo_producto)
    lista.append([nombre_prpducto,cantidad_producto])
    
    #busca y elimina esa posicion
    nuevo_producto=([lista])
    #en teoria busca la posicion y la cambia pero no lo hace pero si agrega el nuevo valor
    print("Actualizacion del producto el producto se encuentra en una nueva posicion",nuevo_producto)
else:
    print("No se actualizo la base del los productos")
