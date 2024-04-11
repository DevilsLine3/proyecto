import random

looot_cofre={
"equipo_epico":0.28,
"equipo_legendario":0.04,
"rss":0.51,
"oro":0.10,
"reductores":0.07
}
lista=()
def recibir_recompensa(looot_cofre):
    recompensa_seleccionada=random.choices(
        list(looot_cofre.keys()),
        weights= list(looot_cofre.values())
    )[0]
    return recompensa_seleccionada

def loteria(Cantidad_cofre,cofre_nivel10,cofre_nivel11,cofre_nivel12):
    resultados={}
    for _ in range(Cantidad_cofre):
        recompensa = recibir_recompensa(looot_cofre)
        if recompensa in resultados:
            resultados[recompensa] += 1
        else:
            resultados[recompensa] = 1
    print("Resultado de la simulacion:")
    for recompensa, cantidad in resultados.items():
        print(f"{recompensa}: {cantidad} veces")
    if cofre_nivel10==True:
        Veces_oro=resultados['oro']
        Cantidad_oro=(Veces_oro*4000)
        print(Cantidad_oro)
        
    elif cofre_nivel11==True:
        Veces_oro=resultados['oro']
        Cantidad_oro=(Veces_oro*5000)
        print(Cantidad_oro)
        
    elif cofre_nivel12 == True:
        Veces_oro=resultados['oro']
        Cantidad_oro=(Veces_oro*6000)
        print(Cantidad_oro)



while True:
    opciones=int(input("\n1 continuar 2 salir: "))
    match opciones:
        case 1:
            Cantidad_cofre=int(input("\nCofres nivel 10: "))
            cofre_nivel10,cofre_nivel11,cofre_nivel12=True,False,False
            loteria(Cantidad_cofre,cofre_nivel10,cofre_nivel11,cofre_nivel12)
            
            Cantidad_cofre=int(input("\nCofres nivel 11: "))
            cofre_nivel10,cofre_nivel11,cofre_nivel12=False,True,False
            loteria(Cantidad_cofre,cofre_nivel10,cofre_nivel11,cofre_nivel12)
            
            Cantidad_cofre=int(input("\nCofres nivel 12: "))
            cofre_nivel10,cofre_nivel11,cofre_nivel12=False,False,True
            loteria(Cantidad_cofre,cofre_nivel10,cofre_nivel11,cofre_nivel12)
            
        case 2:
            break

