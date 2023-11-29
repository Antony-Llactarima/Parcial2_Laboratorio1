import json
import os

dir_actual = os.getcwd()

def cargar_puntajes():
    with open(os.path.join(dir_actual,"recursos\_puntajes\_maxPuntaje.json"),"r") as file:
        my_data = json.load(file)
    return my_data


def update_puntajes(puntaje_nuevo,nivel):
    if nivel == 1:
        list_score = cargar_puntajes()
        dict_score = list_score[0]
    elif nivel == 2:
        list_score = cargar_puntajes()
        dict_score = list_score[1]
    elif nivel == 3:
        list_score = cargar_puntajes()
        dict_score = list_score[2]
    
    cambio = False
    for i in range(5):
        if dict_score[str(i + 1)] <= puntaje_nuevo:
            aux = dict_score[str(i + 1)]
            dict_score[str(i + 1)] = puntaje_nuevo
            puntaje_nuevo = aux
            cambio = True
    if cambio:
        with open(os.path.join(dir_actual,"recursos\_puntajes\_maxPuntaje.json"),"w") as file:
            json.dump(list_score,file)
        print(list_score)


def mostrar_puntaje():
    list_score = cargar_puntajes()
    return list_score
