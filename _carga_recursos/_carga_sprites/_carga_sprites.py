import os
import pygame as pg

dir_actual = os.getcwd()


# CARGA DE IMAGENES DE LA PLATFORMA
try:
    plataforma = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_platforma\plataforma.png"))
except:
    print("Eror")

# CARGA DE SPRITES DE EL JUGADOR
try:
    dino_jugador = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\Jugador\DinoSprites - doux.png"))
    
    # DINO PARADO RIGHT ----------------------------------------------------------------
    dino_jugador.set_clip((4,4,15,16))
    dino_stop_r = dino_jugador.subsurface(dino_jugador.get_clip())
    dino_stop_r = pg.transform.scale(dino_stop_r,(48,48))
    dino_jugador.set_clip((28,4,15,17))
    dino2_stop_r = dino_jugador.subsurface(dino_jugador.get_clip())
    dino2_stop_r = pg.transform.scale(dino2_stop_r,(48,48))
    dino_jugador.set_clip((52,4,15,17))
    dino3_stop_r = dino_jugador.subsurface(dino_jugador.get_clip())
    dino3_stop_r = pg.transform.scale(dino3_stop_r,(48,48))
    dino_jugador.set_clip((76,4,15,17))
    dino4_stop_r = dino_jugador.subsurface(dino_jugador.get_clip())
    dino4_stop_r = pg.transform.scale(dino4_stop_r,(48,48))
    
    # DINO PARADO LEFT ----------------------------------------------------------------
    dino_stop_l = pg.transform.flip(dino_stop_r,True,False)
    dino2_stop_l = pg.transform.flip(dino2_stop_r,True,False)
    dino3_stop_l = pg.transform.flip(dino3_stop_r,True,False)
    dino4_stop_l = pg.transform.flip(dino4_stop_r,True,False)
    
    # DINO CAMINANDO RIGHT ----------------------------------------------------------------
    dino_jugador.set_clip((100,4,15,16))
    dino_move_r = dino_jugador.subsurface(dino_jugador.get_clip())
    dino_move_r = pg.transform.scale(dino_move_r,(48,48))
    dino_jugador.set_clip((124,4,15,17))
    dino2_move_r = dino_jugador.subsurface(dino_jugador.get_clip())
    dino2_move_r = pg.transform.scale(dino2_move_r,(48,48))
    dino_jugador.set_clip((148,4,15,17))
    dino3_move_r = dino_jugador.subsurface(dino_jugador.get_clip())
    dino3_move_r = pg.transform.scale(dino3_move_r,(48,48))
    dino_jugador.set_clip((172,4,15,17))
    dino4_move_r = dino_jugador.subsurface(dino_jugador.get_clip())
    dino4_move_r = pg.transform.scale(dino4_move_r,(48,48))
    
    # DINO CAMINANDO LEFT ----------------------------------------------------------------
    dino_move_l = pg.transform.flip(dino_move_r,True,False)
    dino2_move_l = pg.transform.flip(dino2_move_r,True,False)
    dino3_move_l = pg.transform.flip(dino3_move_r,True,False)
    dino4_move_l = pg.transform.flip(dino4_move_r,True,False)
    
    # DINO CAYENDO RIGHT ----------------------------------------------------------------
    dino_jugador.set_clip((292,4,15,16))
    dino_cae_r = dino_jugador.subsurface(dino_jugador.get_clip())
    dino_cae_r = pg.transform.scale(dino_cae_r,(48,48))
    
    dino_cae_l = pg.transform.flip(dino_cae_r,True,False)
except:
    print("ONO")

try:
    set_coins = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_coins\coins.png"))
    
    set_coins.set_clip(0,0,100,100)
    coin1 = set_coins.subsurface(set_coins.get_clip())
    coin1 =pg.transform.scale(coin1,(25,25))
    
except:
    pass

try:
    vida = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_vida\_vida.png"))
    vida = pg.transform.scale(vida,(50,50))
except:
    pass

# CARGA DE SPRITES DE LOS ENEMIGOS
try:
    crudo_enemigo_1_1 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\lizard\Walk1.png"))
    crudo_enemigo_1_1.set_clip(80,110,60,45)
    enemy_1_1 = crudo_enemigo_1_1.subsurface(crudo_enemigo_1_1.get_clip())
    enemy_1_1 = pg.transform.scale(enemy_1_1,(40,60))
    
    crudo_enemigo_1_2 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\lizard\Walk2.png"))
    crudo_enemigo_1_2.set_clip(80,110,60,45)
    enemy_1_2 = crudo_enemigo_1_2.subsurface(crudo_enemigo_1_2.get_clip())
    enemy_1_2 = pg.transform.scale(enemy_1_2,(40,60))
    
    crudo_enemigo_1_3 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\lizard\Walk3.png"))
    crudo_enemigo_1_3.set_clip(80,110,60,45)
    enemy_1_3 = crudo_enemigo_1_3.subsurface(crudo_enemigo_1_3.get_clip())
    enemy_1_3 = pg.transform.scale(enemy_1_3,(40,60))
    
    crudo_enemigo_1_4 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\lizard\Walk4.png"))
    crudo_enemigo_1_4.set_clip(80,110,60,45)
    enemy_1_4 = crudo_enemigo_1_4.subsurface(crudo_enemigo_1_4.get_clip())
    enemy_1_4 = pg.transform.scale(enemy_1_4,(40,60))
    
    crudo_enemigo_1_5 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\lizard\Walk5.png"))
    crudo_enemigo_1_5.set_clip(80,110,60,45)
    enemy_1_5 = crudo_enemigo_1_5.subsurface(crudo_enemigo_1_5.get_clip())
    enemy_1_5 = pg.transform.scale(enemy_1_5,(40,60))

    crudo_enemigo_1_6 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\lizard\Walk6.png"))
    crudo_enemigo_1_6.set_clip(80,110,60,45)
    enemy_1_6 = crudo_enemigo_1_6.subsurface(crudo_enemigo_1_6.get_clip())
    enemy_1_6 = pg.transform.scale(enemy_1_6,(40,60))
    
    enemy_1_1_l = pg.transform.flip(enemy_1_1,True,False)
    enemy_1_2_l = pg.transform.flip(enemy_1_2,True,False)
    enemy_1_3_l = pg.transform.flip(enemy_1_3,True,False)
    enemy_1_4_l = pg.transform.flip(enemy_1_4,True,False)
    enemy_1_5_l = pg.transform.flip(enemy_1_5,True,False)
    enemy_1_6_l = pg.transform.flip(enemy_1_6,True,False)
    
    # ENEMIGOS NIVEL 2
    
    crudo_enemigo_2_1 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\jinn_animation\Flight1.png"))
    crudo_enemigo_2_1.set_clip(24,34,65,80)
    enemy_2_1 = crudo_enemigo_2_1.subsurface(crudo_enemigo_2_1.get_clip())
    enemy_2_1 = pg.transform.scale(enemy_2_1,(60,80))
    
    crudo_enemigo_2_2 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\jinn_animation\Flight2.png"))
    crudo_enemigo_2_2.set_clip(24,34,65,80)
    enemy_2_2 = crudo_enemigo_2_2.subsurface(crudo_enemigo_2_2.get_clip())
    enemy_2_2 = pg.transform.scale(enemy_2_2,(60,80))
    
    crudo_enemigo_2_3 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\jinn_animation\Flight3.png"))
    crudo_enemigo_2_3.set_clip(24,34,65,80)
    enemy_2_3 = crudo_enemigo_2_3.subsurface(crudo_enemigo_2_3.get_clip())
    enemy_2_3 = pg.transform.scale(enemy_2_3,(60,80))
    
    crudo_enemigo_2_4 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\jinn_animation\Flight4.png"))
    crudo_enemigo_2_4.set_clip(24,34,65,80)
    enemy_2_4 = crudo_enemigo_2_4.subsurface(crudo_enemigo_2_4.get_clip())
    enemy_2_4 = pg.transform.scale(enemy_2_4,(60,80))
    
    enemy_2_1_l = pg.transform.flip(enemy_2_1,True,False)
    enemy_2_2_l = pg.transform.flip(enemy_2_2,True,False)
    enemy_2_3_l = pg.transform.flip(enemy_2_3,True,False)
    enemy_2_4_l = pg.transform.flip(enemy_2_4,True,False)
    
    # ENEMIGOS NIVEL 3
    crudo_enemigo_3_1 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\medusa\Walk1.png"))
    crudo_enemigo_3_1.set_clip(18,38,60,60)
    enemy_3_1 = crudo_enemigo_3_1.subsurface(crudo_enemigo_3_1.get_clip())
    enemy_3_1 = pg.transform.scale(enemy_3_1,(60,35))
    
    crudo_enemigo_3_2 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\medusa\Walk2.png"))
    crudo_enemigo_3_2.set_clip(18,38,60,60)
    enemy_3_2 = crudo_enemigo_3_2.subsurface(crudo_enemigo_3_2.get_clip())
    enemy_3_2 = pg.transform.scale(enemy_3_2,(60,35))
    
    crudo_enemigo_3_3 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\medusa\Walk3.png"))
    crudo_enemigo_3_3.set_clip(18,38,60,60)
    enemy_3_3 = crudo_enemigo_3_3.subsurface(crudo_enemigo_3_3.get_clip())
    enemy_3_3 = pg.transform.scale(enemy_3_3,(60,35))
    
    crudo_enemigo_3_4 = pg.image.load(os.path.join(dir_actual,"recursos\Sprites\_enemigos\PNG\medusa\Walk4.png"))
    crudo_enemigo_3_4.set_clip(18,38,60,60)
    enemy_3_4 = crudo_enemigo_3_4.subsurface(crudo_enemigo_3_4.get_clip())
    enemy_3_4 = pg.transform.scale(enemy_3_4,(60,35))
    
    enemy_3_1_l = pg.transform.flip(enemy_3_1,True,False)
    enemy_3_2_l = pg.transform.flip(enemy_3_2,True,False)
    enemy_3_3_l = pg.transform.flip(enemy_3_3,True,False)
    enemy_3_4_l = pg.transform.flip(enemy_3_4,True,False)

except:
    pass