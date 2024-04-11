valor =150_000;

def modificar():
    global valor
    valor=valor+50_000
    print("el valor de la variable es de:",valor)

def cambios():
    global valor
    valor=valor-10_000
    print("el valor de la varables es de:",valor)

modificar()
modificar()
cambios()