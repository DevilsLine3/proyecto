saldo_inicial=500_000

def deposito_dinero():
    global saldo_inicial
    deposito=float(input("cual es la cantidad de dinero:"))
    saldo_inicial=saldo_inicial+deposito
    print("en tu cuenta hay:",saldo_inicial)

def retiro():
    global saldo_inicial
    retiro=float(input("ingrese la cantidad que desea retirar:"))
    while retiro > saldo_inicial:
        print("cantidad mayor del saldo")
        retiro=float(input("ingrese la cantidad que desea retirar:"))
    saldo_inicial=saldo_inicial-retiro
    print("retiro", retiro)
    print("saldo actual",saldo_inicial)

deposito_dinero()
retiro()