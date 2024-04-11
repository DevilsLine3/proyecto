from numpy import *
# Solicitamos la capacidad máxima de peso del carrito
capacidad_maxima = float(input("Ingrese la capacidad máxima de peso del carrito: "))
# Definimos la cantidad de objetos que queremos ingresar
num_objetos = int(input("Ingrese la cantidad de objetos: "))
# Inicializamos una matriz para almacenar los pesos y valores de los objetos
objetos =  zeros((num_objetos, 2))
# Ingresamos el peso y el valor de cada objeto
for i in range(num_objetos):
    peso = float(input(f"Ingrese el peso del objeto {i + 1}: "))
    valor = float(input(f"Ingrese el valor del objeto {i + 1}: "))
    objetos[i] = [peso, valor]
# Ordenamos los objetos por valor en orden descendente
objetos = objetos[objetos[:, 1].argsort()[::-1]]
# Inicializamos una lista para almacenar los objetos seleccionados
objetos_seleccionados = []
# Llenamos el carrito con objetos mientras no excedamos la capacidad de peso
peso_actual = 0
valor_total = 0
for objeto in objetos:
    peso_objeto, valor_objeto = objeto
    if peso_actual + peso_objeto <= capacidad_maxima:
        objetos_seleccionados.append(objeto)
        peso_actual += peso_objeto
        valor_total += valor_objeto
# Imprimimos la combinación de objetos seleccionados
print("\nSeleccion de objetos seleccionados para maximizar el valor:")
for i, (peso, valor) in enumerate(objetos_seleccionados):
    print(f"Objeto {i + 1} - Peso: {peso}, Valor: {valor}")
print(f"Peso total de los productos del carrito: {peso_actual:.2f}")
print(f"Valor total de los productos del carrito: {valor_total:.2f}")