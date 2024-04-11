import random
def loteria (puntos):
    rangos_puntuacion={
        "puntos 1-5":{
            "reducciones":0.25,
            "otro":0.75
        },
        "puntos 6-10":{
            "recursos":0.1,
            "otro":0.55,
            "reducciones":0.35
        },
        "puntos 11-15":{
            "ubucacion precisa":0.5,
            "mejora de salud":0.5
        },
        "puntos 16-20":{
            "otro":0.7,
            "cofre":0.3
        },
        "puntos +21":{
            "OROOOOO":1
        }
    }
    
    probabilidad_total=0
    for rango, recompensas in rangos_puntuacion.items():
        probabilidad_rango=puntos.get(rango,0)
        for recompensa, probabilidad in recompensas.items():
            probabilidad_total += probabilidad_rango*probabilidad
    
    num_aleatorio=random.random()*probabilidad_total
    
    probabilidad_acumulada= 0
    
    for rango, recompensas in rangos_puntuacion.items():
        probabilidad_rango=puntos.get(rango,0)
        for recompensa, probabilidad in recompensas.items():
            probabilidad_acumulada+=probabilidad_rango*probabilidad
            if num_aleatorio<= probabilidad_acumulada:
                mensaje=f"Ganaste {recompensa} en el rango {rango}"
                return mensaje
puntos={
"puntos 1-5":0.493,
"puntos 6-10":0.229,
"puntos 11-15":0.15,
"puntos 16-20":0.06,
"puntos +21":0.007
}
num_intentos=int(input("dijite el numero de intentos: "))
for _ in range(num_intentos):
    resultado= loteria(puntos)
    print(resultado)
