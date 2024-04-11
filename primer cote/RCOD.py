#Reutilizacion de codigo
def calcular_costo_total(precio_unitario,cantidad):
    return precio_unitario*cantidad
def aplicar_descuento(total,porcentaje_descuento):
    descuento=total*(porcentaje_descuento/100)
    return total-descuento
def imprimir_factura(producto,cantidad,precio_unitario,porcentaje_descuento):
    costo_total=calcular_costo_total(precio_unitario,cantidad)
    costo_descontado=aplicar_descuento(costo_total,porcentaje_descuento)
    print("Factura")
    print("Producto",producto)
    print("Cantidad",cantidad)
    print("Precio unitario",precio_unitario)
    print("Costo total",costo_total)
    print("porcentaje de descuento",porcentaje_descuento)
    print("Costo con descuento",costo_descontado)
#otras funciones relacionadas con el problema