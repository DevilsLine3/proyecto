saldo=0.0

def depositar(monto):
    global saldo
    saldo=saldo+monto
    print("se depositaron: ",monto,"saldo actual: $",saldo)    

def retiro(monto):
    global saldo
    if monto > saldo:
        print("saldo insufieciente para retirar esa cantidad")
    else:
        saldo=saldo-monto
        print("se retiraron: ",monto,"saldo actual: $ ",saldo)

def consultar_saldo():
    global saldo
    print("saldo actual: $",saldo)

print("Bienvenido tienes 3 intentos para ingresar la contraseña de 3 dijitos")
contador=1
prueba_contraseña=1568
#prueba_contraseña = int(input("contraseña de prueba: "))
while contador<=3:
    contraseña=int(input("contraseña: "))
    if contraseña==prueba_contraseña:
        print("contraseña aceptada")
        contador=4
        while True:
            print("\nOpciones:")
            print("1. depositar")
            print("2. retirar")
            print("3. consultar saldo")
            print("4. salir")
            opcion = int(input("seleccione una opción: "))
            if opcion ==1:
                contraseña=int(input("dijite su contraseña: "))
                if contraseña==prueba_contraseña:
                    print("contraseña aceptada")
                    monto = float(input("ingrese el monto a depositar: "))
                    depositar(monto)
                else:
                    print("contraseña equivocada")
                    print("saliendo de la sesion...")
                    break
            elif opcion == 2:
                contraseña=int(input("dijite su contraseña: "))
                if contraseña==prueba_contraseña:
                    print("contraseña aceptada")
                    monto = float(input("ingrese el monto a retirar: "))
                    retiro(monto)
                else:
                    print("contraseña equivocada")
                    print("saliendo de la sesion...")
                    break
            elif opcion == 3:
                contraseña=int(input("ingrese la contraseña: "))
                if contraseña==prueba_contraseña:
                    print("contraseña aceptada")
                    consultar_saldo()
                else:
                    print("contraseña equivocada")
                    print("saliendo de la sesion...")
                    break
            elif opcion == 4:
                print("gracias por utilizar la simulacion")
                break
            else: 
                print("opcion no valida. por favor, elija una valida")
    else:
        contador_desendente=3-contador
        print("contraseña erronea tienes ",contador_desendente,"intentos")
        contador=contador+1