from numpy import*
dias_de_actividad=7
semana_cont_pasos=empty(dias_de_actividad)
lista=[]
total_pasos=0
dic={}
for i in range(7):
    nombre_semana=str(input("Ingrese el dia de la semana: "))
    dias_pasos=int(input("Ingrese la cantidad de pasos: "))
    lista.append([nombre_semana,dias_pasos])
    semana_cont_pasos=lista
    total_pasos=total_pasos+dias_pasos
    
    dic.update({nombre_semana:dias_pasos})#se guarda en un diccionario para que sea mas facil buscar despues
dia_mayor_pasos=max(dic.values())#busca el valor maximo del los values del diccionario
a=list(dic.keys())[list(dic.values()).index(dia_mayor_pasos)]#busca la key del diccionario deacuerdo el valor de la misma
print(semana_cont_pasos)
print("total de pasos en la semana",total_pasos)
print("El dia de mayor pasos fue",a,"con ",dia_mayor_pasos,"pasos")