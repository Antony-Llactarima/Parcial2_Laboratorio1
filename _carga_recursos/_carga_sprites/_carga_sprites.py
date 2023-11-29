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