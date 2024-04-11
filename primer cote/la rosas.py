saldo=100_000;

def depositar(monto):
    global saldo;
    saldo=saldo+monto;
    print("Se depositaron:",monto,"Saldo actual:$",saldo);
    
def retirar(monto):
    global saldo;
    if monto>saldo:
        print("Saldo insuficiente para retirar esa cantidad");
        
    else:
        saldo=saldo-monto;
        print("Se retiraron: ",monto,"Saldo actual:$",saldo);
        
def consultar_saldo():
    global saldo;
    print("Saldo actual:$",saldo)
#prueba de clave    
print("Estimado cliente,para ingresar a su cuenta")    
print("Digite la contraseña de 4 digitos y recuerda que solo tienes 3 intentos")
clavev=2023;
clave=int(input("Contraseña: "))
c=0;

while clave!= clavev:
    print("Contraseña incorrecta")
    print("Digite la contraseña de 4 digitos nuevamente")
    clave=int(input(""))
    c=c+1
    if c==2:
        print("Se excedio el limite de intentos")
        quit()
        
while True:
    
    print("\nOpciones");
    print("1.Depositar");
    print("2.Retirar");
    print("3.Consultar saldo");
    print("4.Salir");
    
    opcion=int(input("Seleccione una opcion:"))
    
    if opcion==1:
        monto=float(input("Ingrese el monto a depositar:"));
        depositar(monto)
        
    elif opcion==2:
        monto=float(input("Ingrese el monto a retirar:"));
        retirar(monto)
        
    elif opcion==3:
        consultar_saldo();
        
    elif opcion==4:
        print("Gracias por utilizar el simulador de cuenta bancaria");
        break
    else:
        print("opcion no valida, digite una opcion valida");
