partes_del_motor={
    "bloque del motor":2_000_000,
    "Cilindros":500_000,
    "Biela":750_000,
    "Pistones":1_000_000,
    "Anillos de compresion":1_000_000,
    "Cigueñal":2_000_000,
    "Árbol de levas":1_500_000,
    "Transmición":800_000,
    "Sistema de escape":850_000,
    "Sistema de refrigeración":1_500_000,
    "Sistema de alimentación de combustible":3_000_000,
    "Sistema de lubricación":1_000_000,
    "Sistema de encendido": 500_000
}
print("Bienvenido a nuestra sucursal de motores")
while True:
    print("\n formas de pago 1. Pago en efectivo 2. Pago con tarjeta 3. Pago a plazos 4. Salir")
    menu=int(input("Ingrese la forma de pago por favor: "))
    match menu:
        case 1:
            total_sin_descuento=sum(partes_del_motor.values())
            descuento=total_sin_descuento*0.10
            total=total_sin_descuento-descuento
            print("total sin el descuento: $", total_sin_descuento)
            print("Haz obtenido un descuento, el nuevo precio es de: $",total)
        case 2:
            total_sin_descuento=sum(partes_del_motor.values())
            descuento=total_sin_descuento*0.05
            total=total_sin_descuento-descuento
            print("total sin el descuento: $", total_sin_descuento)
            print("Haz obtenido un descuento, el nuevo precio es de: $", total)
        case 3:
            total_sin_descuento=sum(partes_del_motor.values())
            print("Total de su compra es de: $", total_sin_descuento)
        case 4:
            break