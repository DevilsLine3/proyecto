from numpy import*

def crear_matriz():
    filas = int(input("Digite el número de productos: "))
    matriz = []
    
    for i in range(filas):
        peso = float(input(f"Digite el peso del producto {i + 1}: "))
        precio = float(input(f"Digite el precio del producto {i + 1}: "))
        matriz.append([peso, precio])
    
    return matriz

def ordenar(producto):
    peso = producto[0]
    precio = -producto[1]
    return (peso, precio)

def seleccionar_productos(matriz, limite_peso):
    productos_seleccionados = []
    peso_total = 0
    precio_total = 0
    
    matriz_ordenada = sorted(matriz, key=ordenar)
    
    for peso, precio in matriz_ordenada:
        if peso_total + peso <= limite_peso:
            productos_seleccionados.append([peso, precio])
            peso_total += peso
            precio_total += precio
    
    return productos_seleccionados, peso_total, precio_total

matriz_productos = crear_matriz()
print("Matriz de productos:")
for fila in matriz_productos:
    print(fila)

limite_peso = 30  
productos_seleccionados, peso_total, precio_total = seleccionar_productos(matriz_productos, limite_peso)

print("Productos seleccionados:")
for producto in productos_seleccionados:
    print(f"Peso: {producto[0]} kg, Precio: ${producto[1]}")

print(f"Peso total de los productos seleccionados: {peso_total} kg")
print(f"Precio total de los productos seleccionados: ${precio_total}")
