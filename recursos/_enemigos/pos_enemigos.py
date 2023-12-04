from Clases._personajes.enemigos import Enemigos

# FUNCION PARA CREAR ENEMIGOS
def crear_enemigos(nivel_enemigo,cant_enemigos):
    lista_enemigos = []
    for i in range(cant_enemigos):
        if nivel_enemigo == 1:
            lista_enemigos.append(Enemigos("1",1,3,[35,50],'right'))
        elif nivel_enemigo == 2:
            lista_enemigos.append(Enemigos("2",1,4,[50,60],'up'))
        elif nivel_enemigo == 3:
            lista_enemigos.append(Enemigos("3",1,10,[30,30],'right'))
    return lista_enemigos

# ENEMIGOS PARA EL NIVEL 1
list_enemy_1_1 = crear_enemigos(1,3)
# -----------------------------------------------
list_enemy_1_1[0].definir_posicion([640,520],[640,520])
list_enemy_1_1[1].definir_posicion([460,250],[460,250])
list_enemy_1_1[2].definir_posicion([0,220],[0,220])

# ENEMIGOS PARA EL NIVEL 2
list_enemy_1_2 = crear_enemigos(1,2)
list_enemy_2_2 = crear_enemigos(2,3)
list_enemy_3_2 = crear_enemigos(3,1)

# -----------------------------------------------
list_enemy_1_2[0].definir_posicion([0,150],[0,150])
list_enemy_1_2[1].definir_posicion([250,150],[250,150])
# -----------------------------------------------
list_enemy_2_2[0].definir_posicion([640,660],[640,660])
list_enemy_2_2[1].definir_posicion([440,660],[440,660])
list_enemy_2_2[2].definir_posicion([240,660],[240,660])
# -----------------------------------------------
list_enemy_3_2[0].definir_posicion([320,345],[320,345])


# ENEMIGOS PARA EL NIVEL 3
list_enemy_1_3 = crear_enemigos(1,2)
list_enemy_2_3 = crear_enemigos(2,4)
list_enemy_3_3 = crear_enemigos(3,1)
# -----------------------------------------------
list_enemy_1_3[0].definir_posicion([148,110],[148,110])
list_enemy_1_3[1].definir_posicion([632,110],[632,110])
# -----------------------------------------------
list_enemy_2_3[0].definir_posicion([130,600],[130,600])
list_enemy_2_3[1].definir_posicion([330,600],[330,600])
list_enemy_2_3[2].definir_posicion([690,600],[690,600])
list_enemy_2_3[3].definir_posicion([890,600],[890,600])
# -----------------------------------------------
list_enemy_3_3[0].definir_posicion([320,185],[320,185])


