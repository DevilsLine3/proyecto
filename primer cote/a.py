def saludar():
    print ("¡hola! Bienvenido a la función")
    print("ingerso a la primera función del programa")
    
saludar();#llamado de la función
saludar();

def sumar():
    num1=20;
    num2=30;
    resultado=num2+num1;
    return resultado

print("El resultado fue",sumar());

def sumar_parametros(num1,num2,num3):
    resultado =num1+num2+num3;
    return resultado;

num1=float(input("Dijite el valor del número 1: "))
num2=float(input("Dijite el valor del número 2: "))
num3=float(input("Dijite el valor del número 3: "))

print("El resultado fue de",sumar_parametros(35,120,65));
print("El resultado fue de",sumar_parametros(35,10,5));

print("El resultado fue de",sumar_parametros(num1,num2,num3))

def restar_parametros(num1,num2,num3):
    resultado=num1 - num2 - num3
    return resultado
print("El resultado fue de",restar_parametros(35,120,456))
print("el resultado fue de",restar_parametros(num1,num2,num3))

resultado_funcion3=sumar();



